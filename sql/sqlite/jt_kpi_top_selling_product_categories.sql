-- JT KPI: Top Selling Product Categories
DROP TABLE IF EXISTS kpi_top_selling_product_categories;

CREATE TABLE kpi_top_selling_product_categories AS
SELECT
    product_category,
    COUNT(*) AS sale_count,
    SUM(amount) AS total_revenue,
    ROUND(AVG(amount), 2) AS avg_sale_amount
FROM sale
GROUP BY product_category
ORDER BY total_revenue DESC;
