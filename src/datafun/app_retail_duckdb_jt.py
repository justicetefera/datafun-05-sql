"""
JT Retail Pipeline (DuckDB)
Author: Justice
Purpose:
- Run JT KPI SQL files for DuckDB.
"""

from datafun.shared import (
    get_paths,
    log_paths,
    log_run_end,
    log_run_start,
    run_sql_scripts,
)

# SQL scripts to run (same as SQLite)

query_files = [
    # 1. Clean + bootstrap
    "jt_retail_clean.sql",
    "jt_sales_bootstrap.sql",
    "jt_load_csv.sql",
    # 2. Views (semantic layer)
    "jt_views.sql",
    # 3. Debug (optional but helpful)
    "jt_debug_sale_count.sql",
    "jt_debug_store_count.sql",
    "jt_debug_sale_peek.sql",
    "jt_debug_store_peek.sql",
    # 4. KPI scripts
    "jt_kpi_revenue_by_region.sql",
    "jt_kpi_sales_aggregate.sql",
    "jt_kpi_sales_by_category.sql",
    "jt_kpi_revenue_by_store.sql",
    "jt_kpi_top_selling_product_categories.sql",
    "jt_kpi_store_performance_ranking.sql",
    # 5. Materialized KPI table
    "jt_kpi_table.sql",
]


def main():
    log_run_start("JT Pipeline (DuckDB)")

    paths = get_paths("duckdb")
    log_paths(paths)

    run_sql_scripts(paths, query_files)

    log_run_end()


if __name__ == "__main__":
    main()
