# SQL + SQLite Retail Data Pipeline

[![Workflow Guide](https://img.shields.io/badge/Pro--Guide-pro--analytics--02-green)](https://justicetefera.github.io/pro-analytics-02/workflow-b-apply-example-project/)
[![Python 3.14](https://img.shields.io/badge/python-3.14%2B-blue?logo=python)](./pyproject.toml)
[![MIT](https://img.shields.io/badge/license-see%20LICENSE-yellow.svg)](./LICENSE)

> Professional Python project: relational data and SQL analytics.

Data analytics requires a variety of skills.
This project builds capabilities through working projects.

## This Project

This project reflects that every component — Environment setup, SQL logic, Python automation, logging, and repository workflow are built and executed as a working pipeline.
It produces real outputs, cleaned tables, validated row counts, debug queries, KPI tables, and exported artifacts.

The logs show the full lifecycle of the pipeline running end‑to‑end, including environment details, SQL execution order, row counts, and successful KPI materialization.

This project extends a relational data and SQL pipeline by moving beyond simple `SELECT` queries to creating KPI tables that support deeper analysis. Analysts are typically highly skilled at both SQL and Python, and this work strengthens both.

- **retail** - a store records many sales (the worked example)
- **library** - a library branch manages many checkouts
- **shelter** - a shelter manages many animal adoptions
- **civic_event** - an event manages many attendees

The retail dataset includes two related tables in a 1‑to‑many relationship: stores and sales. This pipeline processes the raw data, builds views, validates counts, and generates KPI tables that summarize store performance, revenue, and product trends.

## Working Files

- **data/raw/\*** - raw CSV input files
- **data/processed/** - processed data outputs, if created
- **artifacts/** - generated database files, logs, or reports
- **docs/** - the project narrative and documentation
- **sql/** - SQL query files
- **src/datafun/** - Python orchestration scripts
- **pyproject.toml** - update project metadata
- **zensical.toml** - update documentation site metadata

## Instructions

Follow the [step-by-step workflow guide](https://justicetefera.github.io/datafun-05-sql/) to complete:


1. Phase 1. **Start & Run**
2. Phase 2. **Change Authorship**
3. Phase 3. **Read & Understand**
4. Phase 4. **Modify**
5. Phase 5. **Apply**

## Success

Running the examples should create generated database files in `artifacts/`.

A new file `project.log` will appear in the root project folder

## Command Reference
Follow the guide for the **full instructions**.

<details>
<summary>Show command reference</summary>

### In a machine terminal (open in your `Repos` folder)

After you get a copy of this repo in your own GitHub account,
open a machine terminal in your `Repos` folder:

```shell
# Replace username with YOUR GitHub username.
git clone https://github.com/justicetefera/datafun-05-sql

cd datafun-05-sql
code .
```

### In a VS Code terminal

These are listed for convenience.
For best results, follow the detailed instructions in
[Workflow B: Apply Example Project](https://justicetefera.github.io/datafun-05-sql/workflow-b-apply-example-project/)


```shell
uv self update
uv python pin 3.14
uv lock --upgrade
uv sync --extra dev --extra docs --upgrade

uvx pre-commit install

git add -A
uvx pre-commit run --all-files
# repeat if changes were made
uvx pre-commit run --all-files

# run the example pipelines (duckdb and sqlite)
uv run python -m datafun.app_retail_duckdb_case
uv run python -m datafun.app_retail_sqlite_case

# do chores
uv run ruff format .
uv run ruff check . --fix
uv run python -m pyright
uv run python -m pytest
uv run python -m zensical build

# save progress
git add -A
git commit -m "update"
git push -u origin main
```

</details>

## Notes

- Use the **UP ARROW** and **DOWN ARROW** in the terminal to scroll through past commands.
- Use `CTRL+f` to find (and replace) text within a file.
- You do not need to add to or modify `tests/`. They are provided for example only.
- Many files are silent helpers. Explore as you like, but nothing is required.
- You do NOT not to understand everything; understanding builds naturally over time.

## Troubleshooting >>>

If you see something like this in your terminal: `>>>` or `...`
You accidentally started Python interactive mode.
It happens.
Press `Ctrl+c` (both keys together) or `Ctrl+Z` then `Enter` on Windows.

## DuckDB Output

```shell
2026-06-07 05:00:22,612 | INFO | JT | ##################
2026-06-07 05:00:22,613 | INFO | JT | ### RUN START ####
2026-06-07 05:00:22,613 | INFO | JT | ##################
2026-06-07 05:00:22,613 | INFO | JT | project=JT Pipeline (SQLite)
2026-06-07 05:00:22,613 | INFO | JT | repo_dir=datafun-05-sql
2026-06-07 05:00:22,614 | INFO | JT | python=3.14.5
2026-06-07 05:00:22,662 | INFO | JT | os=Windows 11
2026-06-07 05:00:22,662 | INFO | JT | shell=powershell
2026-06-07 05:00:22,662 | INFO | JT | cwd=C:\Users\JTEFE\Repos\datafun-05-sql
2026-06-07 05:00:22,662 | INFO | JT | github_actions=False
2026-06-07 05:00:22,663 | INFO | JT | START main()
2026-06-07 05:00:22,663 | INFO | JT | ROOT_DIR: C:\Users\JTEFE\Repos\datafun-05-sql
2026-06-07 05:00:22,663 | INFO | JT | SQL_DIR: C:\Users\JTEFE\Repos\datafun-05-sql\sql\sqlite
2026-06-07 05:00:22,664 | INFO | JT | DB_PATH: C:\Users\JTEFE\Repos\datafun-05-sql\artifacts\sqlite\retail.db
2026-06-07 05:00:22,665 | INFO | JT | RUN SQL script: C:\Users\JTEFE\Repos\datafun-05-sql\sql\sqlite\jt_retail_clean.sql
2026-06-07 05:00:22,714 | INFO | JT | DONE SQL script: C:\Users\JTEFE\Repos\datafun-05-sql\sql\sqlite\jt_retail_clean.sql
2026-06-07 05:00:22,715 | INFO | JT | Loading CSV data into SQLite...
2026-06-07 05:00:22,718 | INFO | JT | CSV data loaded successfully.
2026-06-07 05:00:22,718 | INFO | JT | RUN SQL script: C:\Users\JTEFE\Repos\datafun-05-sql\sql\sqlite\jt_views.sql
2026-06-07 05:00:22,889 | INFO | JT | DONE SQL script: C:\Users\JTEFE\Repos\datafun-05-sql\sql\sqlite\jt_views.sql
2026-06-07 05:00:22,890 | INFO | JT |
2026-06-07 05:00:22,891 | INFO | JT | RUN SQL query: C:\Users\JTEFE\Repos\datafun-05-sql\sql\sqlite\jt_debug_sale_count.sql
2026-06-07 05:00:22,891 | INFO | JT | ====================================
2026-06-07 05:00:22,892 | INFO | JT | jt_debug_sale_count.sql
2026-06-07 05:00:22,892 | INFO | JT | ====================================
2026-06-07 05:00:22,893 | INFO | JT | sale_rows
2026-06-07 05:00:22,894 | INFO | JT | 30
2026-06-07 05:00:22,896 | INFO | JT |
2026-06-07 05:00:22,896 | INFO | JT | RUN SQL query: C:\Users\JTEFE\Repos\datafun-05-sql\sql\sqlite\jt_debug_store_count.sql
2026-06-07 05:00:22,897 | INFO | JT | ====================================
2026-06-07 05:00:22,898 | INFO | JT | jt_debug_store_count.sql
2026-06-07 05:00:22,899 | INFO | JT | ====================================
2026-06-07 05:00:22,900 | INFO | JT | store_rows
2026-06-07 05:00:22,900 | INFO | JT | 3
2026-06-07 05:00:22,901 | INFO | JT |
2026-06-07 05:00:22,901 | INFO | JT | RUN SQL query: C:\Users\JTEFE\Repos\datafun-05-sql\sql\sqlite\jt_debug_sale_peek.sql
2026-06-07 05:00:22,901 | INFO | JT | ====================================
2026-06-07 05:00:22,901 | INFO | JT | jt_debug_sale_peek.sql
2026-06-07 05:00:22,901 | INFO | JT | ====================================
2026-06-07 05:00:22,902 | INFO | JT | sale_id, store_id, product_category, quantity, amount, sale_date
2026-06-07 05:00:22,902 | INFO | JT | SA001, S001, Clothing, 2, 120.0, 2026-01-05
2026-06-07 05:00:22,902 | INFO | JT | SA002, S001, Food, 5, 45.0, 2026-01-06
2026-06-07 05:00:22,902 | INFO | JT | SA003, S002, Outdoors, 1, 250.0, 2026-01-07
2026-06-07 05:00:22,902 | INFO | JT | SA004, S002, Food, 3, 30.0, 2026-01-08
2026-06-07 05:00:22,902 | INFO | JT | SA005, S003, Clothing, 1, 60.0, 2026-01-09
2026-06-07 05:00:22,903 | INFO | JT |
2026-06-07 05:00:22,903 | INFO | JT | RUN SQL query: C:\Users\JTEFE\Repos\datafun-05-sql\sql\sqlite\jt_debug_store_peek.sql
2026-06-07 05:00:22,903 | INFO | JT | ====================================
2026-06-07 05:00:22,903 | INFO | JT | jt_debug_store_peek.sql
2026-06-07 05:00:22,903 | INFO | JT | ====================================
2026-06-07 05:00:22,904 | INFO | JT | store_id, store_name, city, region
2026-06-07 05:00:22,904 | INFO | JT | S001, North Market, Duluth, North
2026-06-07 05:00:22,904 | INFO | JT | S002, Lakeside Shop, Ely, North
2026-06-07 05:00:22,904 | INFO | JT | S003, Central Plaza, Mankato, South
2026-06-07 05:00:22,905 | INFO | JT | RUN SQL script: C:\Users\JTEFE\Repos\datafun-05-sql\sql\sqlite\jt_kpi_revenue_by_region.sql
2026-06-07 05:00:22,968 | INFO | JT | DONE SQL script: C:\Users\JTEFE\Repos\datafun-05-sql\sql\sqlite\jt_kpi_revenue_by_region.sql
2026-06-07 05:00:22,968 | INFO | JT | RUN SQL script: C:\Users\JTEFE\Repos\datafun-05-sql\sql\sqlite\jt_kpi_sales_aggregate.sql
2026-06-07 05:00:23,041 | INFO | JT | DONE SQL script: C:\Users\JTEFE\Repos\datafun-05-sql\sql\sqlite\jt_kpi_sales_aggregate.sql
2026-06-07 05:00:23,042 | INFO | JT | RUN SQL script: C:\Users\JTEFE\Repos\datafun-05-sql\sql\sqlite\jt_kpi_sales_by_category.sql
2026-06-07 05:00:23,111 | INFO | JT | DONE SQL script: C:\Users\JTEFE\Repos\datafun-05-sql\sql\sqlite\jt_kpi_sales_by_category.sql
2026-06-07 05:00:23,112 | INFO | JT | RUN SQL script: C:\Users\JTEFE\Repos\datafun-05-sql\sql\sqlite\jt_kpi_revenue_by_store.sql
2026-06-07 05:00:23,179 | INFO | JT | DONE SQL script: C:\Users\JTEFE\Repos\datafun-05-sql\sql\sqlite\jt_kpi_revenue_by_store.sql
2026-06-07 05:00:23,180 | INFO | JT | RUN SQL script: C:\Users\JTEFE\Repos\datafun-05-sql\sql\sqlite\jt_kpi_top_selling_product_categories.sql
2026-06-07 05:00:23,249 | INFO | JT | DONE SQL script: C:\Users\JTEFE\Repos\datafun-05-sql\sql\sqlite\jt_kpi_top_selling_product_categories.sql
2026-06-07 05:00:23,250 | INFO | JT | RUN SQL script: C:\Users\JTEFE\Repos\datafun-05-sql\sql\sqlite\jt_kpi_store_performance_ranking.sql
2026-06-07 05:00:23,317 | INFO | JT | DONE SQL script: C:\Users\JTEFE\Repos\datafun-05-sql\sql\sqlite\jt_kpi_store_performance_ranking.sql
2026-06-07 05:00:23,319 | INFO | JT | RUN SQL script: C:\Users\JTEFE\Repos\datafun-05-sql\sql\sqlite\jt_kpi_table.sql
2026-06-07 05:00:23,387 | INFO | JT | DONE SQL script: C:\Users\JTEFE\Repos\datafun-05-sql\sql\sqlite\jt_kpi_table.sql
2026-06-07 05:00:23,388 | INFO | JT | RUN SQL script: C:\Users\JTEFE\Repos\datafun-05-sql\sql\sqlite\jt_export_kpi_table.sql
2026-06-07 05:00:23,456 | INFO | JT | DONE SQL script: C:\Users\JTEFE\Repos\datafun-05-sql\sql\sqlite\jt_export_kpi_table.sql
2026-06-07 05:00:23,457 | INFO | JT | #################################
2026-06-07 05:00:23,457 | INFO | JT | ##### Executed successfully! ####
2026-06-07 05:00:23,458 | INFO | JT | #################################

```
#### This project demonstrated the strength of SQL for working with structured relational data in SQLite.
#### The 1‑to‑many relationship between stores and sales made SQL the ideal tool for joins, aggregations, and KPI calculations. Once the SQL scripts were organized, modifying or adding new transformations was straightforward.
#### Python acted as the controller for the entire workflow — loading CSVs, executing SQL scripts, validating row counts, and generating logs.  This structure makes the workflow predictable, repeatable, and easy to extend.
