-- JT KPI: Sales Aggregate
DROP TABLE IF EXISTS kpi_sales_aggregate;

CREATE TABLE kpi_sales_aggregate AS
SELECT
    COUNT(*) AS sale_count,
    SUM(amount) AS total_revenue,
    ROUND(AVG(amount), 2) AS avg_sale_amount
FROM sale;
