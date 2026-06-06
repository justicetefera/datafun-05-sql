"""
JT Retail Pipeline (SQLite)
Author: Justice
Purpose:
- Run JT KPI SQL files for SQLite.
"""

from datafun.shared import (
    get_paths,
    log_paths,
    log_run_end,
    log_run_start,
    run_sql_scripts,
)


def main():
    # Start banner + environment info
    log_run_start("JT Pipeline (SQLite)")

    # Resolve paths for SQLite engine
    paths = get_paths(engine="sqlite")
    log_paths(paths)

    # SQL scripts to run in order
    query_files = [
        "jt_retail_clean.sql",
        "jt_sales_bootstrap.sql",
        "jt_views.sql",
        "jt_debug_sale_count.sql",
        "jt_debug_store_count.sql",
        "jt_debug_sale_peek.sql",
        "jt_debug_store_peek.sql",
        "jt_kpi_revenue_by_region.sql",
        "jt_kpi_sales_aggregate.sql",
        "jt_kpi_sales_by_category.sql",
        "jt_kpi_revenue_by_store.sql",
        "jt_kpi_top_selling_product_categories.sql",
        "jt_kpi_store_performance_ranking.sql",
        "jt_kpi_table.sql",
        "jt_export_kpi_table.sql",
    ]

    # Execute SQL scripts
    run_sql_scripts(paths, query_files)

    # End banner
    log_run_end()


if __name__ == "__main__":
    main()
