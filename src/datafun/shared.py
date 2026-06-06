"""
Shared utilities for JT pipelines.
"""

import csv
import logging
import os
from pathlib import Path
import platform
import sqlite3

import duckdb

# ---------------------------------------------------------
# Logging
# ---------------------------------------------------------


def get_logger(name: str) -> logging.Logger:
    from pathlib import Path

    # Determine repo root
    ROOT_DIR = Path(__file__).resolve().parents[1]
    LOG_FILE = ROOT_DIR / "project.log"

    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)

    # Prevent duplicate handlers if get_logger() is called multiple times
    if logger.handlers:
        return logger

    # Formatter
    formatter = logging.Formatter("%(asctime)s | %(levelname)s | JT | %(message)s")

    # Console handler
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)

    # File handler
    file_handler = logging.FileHandler(LOG_FILE, mode="a", encoding="utf-8")
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    return logger


# 🔥 Initialize shared logger ONCE

logger = get_logger("JT")


# ---------------------------------------------------------
# Pretty Logging Helpers
# ---------------------------------------------------------


def log_run_start(project_name: str):
    logger.info("##################")
    logger.info("### RUN START ####")
    logger.info("##################")
    logger.info(f"project={project_name}")
    logger.info(f"repo_dir={Path.cwd().name}")
    logger.info(f"python={platform.python_version()}")
    logger.info(f"os={platform.system()} {platform.release()}")
    logger.info(f"shell={os.environ.get('SHELL', 'powershell')}")
    logger.info(f"cwd={Path.cwd()}")
    logger.info(f"github_actions={os.environ.get('GITHUB_ACTIONS', 'False')}")
    logger.info("START main()")


def log_paths(paths: dict):
    logger.info(f"ROOT_DIR: {paths['root']}")
    logger.info(f"SQL_DIR: {paths['sql_dir']}")
    logger.info(f"DB_PATH: {paths['db_path']}")


def log_query_header(sql_file: str):
    logger.info("")
    logger.info(f"RUN SQL query: {sql_file}")
    logger.info("====================================")
    logger.info(Path(sql_file).name)
    logger.info("====================================")


def log_run_end():
    logger.info("#################################")
    logger.info("##### Executed successfully! ####")
    logger.info("#################################")
    logger.info("END main()")


# ---------------------------------------------------------
# Paths
# ---------------------------------------------------------


def get_paths(engine: str):
    root = Path(__file__).resolve().parents[2]

    return {
        "root": root,
        "sql_dir": root / "sql" / engine,
        "db_path": root
        / "artifacts"
        / engine
        / ("retail.db" if engine == "sqlite" else "retail.duckdb"),
    }


# ---------------------------------------------------------
# SQL Runner
# ---------------------------------------------------------


def run_sql_scripts(paths, query_files):
    sql_dir = paths["sql_dir"]
    db_path = paths["db_path"]

    # Connect to correct engine
    if "duckdb" in str(db_path):
        conn = duckdb.connect(str(db_path))
        engine = "duckdb"
    else:
        conn = sqlite3.connect(str(db_path))
        engine = "sqlite"

    for file in query_files:
        script_path = sql_dir / file
        sql_text = script_path.read_text()

        # Detect SELECT even if comments or blank lines appear first
        clean_sql = "\n".join(
            line
            for line in sql_text.splitlines()
            if not line.strip().startswith("--") and line.strip() != ""
        )

        is_query = clean_sql.strip().lower().startswith("select")
        # SPECIAL: After JT bootstrap, load CSVs into SQLite
        if file == "jt_sales_bootstrap.sql" and engine == "sqlite":
            logger.info("Loading CSV data into SQLite...")

            store_csv = paths["root"] / "data" / "raw" / "retail" / "store.csv"
            sale_csv = paths["root"] / "data" / "raw" / "retail" / "sale.csv"

            # Load store.csv
            with Path(store_csv).open(newline="") as f:
                reader = csv.DictReader(f)
                for row in reader:
                    conn.execute(
                        "INSERT INTO store (store_id, store_name, city, region) VALUES (?, ?, ?, ?)",
                        (
                            row["store_id"],
                            row["store_name"],
                            row["city"],
                            row["region"],
                        ),
                    )

            # Load sale.csv
            with Path(sale_csv).open(newline="") as f:
                reader = csv.DictReader(f)
                for row in reader:
                    conn.execute(
                        "INSERT INTO sale (sale_id, store_id, product_category, quantity, amount, sale_date) VALUES (?, ?, ?, ?, ?, ?)",
                        (
                            row["sale_id"],
                            row["store_id"],
                            row["product_category"],
                            int(row["quantity"]),
                            float(row["amount"]),
                            row["sale_date"],
                        ),
                    )

            logger.info("CSV data loaded successfully.")
            continue

        if is_query:
            # Pretty header
            log_query_header(str(script_path))

            try:
                # DuckDB: execute normally
                if engine == "duckdb":
                    result = conn.execute(sql_text)
                else:
                    # SQLite: execute SELECT normally
                    result = conn.execute(sql_text)

                # Print column names
                col_names = [desc[0] for desc in result.description]
                logger.info(", ".join(col_names))

                # Print rows
                for row in result.fetchall():
                    logger.info(", ".join(str(x) for x in row))

            except Exception as e:
                logger.error(f"Error running {file}: {e}")

        else:
            # Non-query script (clean + bootstrap)
            logger.info(f"RUN SQL script: {script_path}")

            try:
                if engine == "duckdb":
                    conn.execute(sql_text)
                else:
                    conn.executescript(sql_text)

                logger.info(f"DONE SQL script: {script_path}")

            except Exception as e:
                logger.error(f"Error running {file}: {e}")

    conn.close()
