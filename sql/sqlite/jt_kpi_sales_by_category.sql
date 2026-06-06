-- JT KPI: Sales by Category
DROP TABLE IF EXISTS kpi_sales_by_category;

CREATE TABLE kpi_sales_by_category AS
SELECT
    product_category,
    COUNT(*) AS sale_count,
    SUM(amount) AS total_revenue,
    ROUND(AVG(amount), 2) AS avg_sale_amount
FROM sale
GROUP BY product_category
ORDER BY total_revenue DESC;
