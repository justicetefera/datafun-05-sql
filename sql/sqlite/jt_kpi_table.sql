-- Drop existing KPI table
DROP TABLE IF EXISTS jt_kpi_all;

-- Create a materialized KPI table
CREATE TABLE jt_kpi_all AS

-- KPI 1: Revenue by Region
SELECT
    'revenue_by_region' AS kpi_name,
    region AS key1,
    NULL AS key2,
    sale_count,
    total_revenue,
    avg_sale_amount
FROM kpi_revenue_by_region

UNION ALL

-- KPI 2: Sales Aggregate
SELECT
    'sales_aggregate',
    NULL,
    NULL,
    sale_count,
    total_revenue,
    avg_sale_amount
FROM kpi_sales_aggregate

UNION ALL

-- KPI 3: Sales by Category
SELECT
    'sales_by_category',
    product_category,
    NULL,
    sale_count,
    total_revenue,
    avg_sale_amount
FROM kpi_sales_by_category

UNION ALL

-- KPI 4: Revenue by Store
SELECT
    'revenue_by_store',
    store_id,
    store_name,
    sale_count,
    total_revenue,
    avg_sale_amount
FROM kpi_revenue_by_store

UNION ALL

-- KPI 5: Top Selling Categories
SELECT
    'top_selling_categories',
    product_category,
    NULL,
    sale_count,
    total_revenue,
    avg_sale_amount
FROM kpi_top_selling_product_categories

UNION ALL

-- KPI 6: Store Performance Ranking
SELECT
    'store_performance_ranking',
    store_id,
    store_name,
    sale_count,
    total_revenue,
    avg_sale_amount
FROM kpi_store_performance_ranking;
