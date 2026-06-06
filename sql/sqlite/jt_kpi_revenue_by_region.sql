-- JT KPI: Revenue by Region
DROP TABLE IF EXISTS kpi_revenue_by_region;

CREATE TABLE kpi_revenue_by_region AS
SELECT
    s.region,
    COUNT(sa.sale_id) AS sale_count,
    SUM(sa.amount) AS total_revenue,
    ROUND(AVG(sa.amount), 2) AS avg_sale_amount
FROM store s
JOIN sale sa ON s.store_id = sa.store_id
GROUP BY s.region
ORDER BY total_revenue DESC;
