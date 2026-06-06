-- JT KPI: Revenue by Store
DROP TABLE IF EXISTS kpi_revenue_by_store;

CREATE TABLE kpi_revenue_by_store AS
SELECT
    s.store_id,
    s.store_name,
    s.city,
    s.region,
    COUNT(sa.sale_id) AS sale_count,
    SUM(sa.amount) AS total_revenue,
    ROUND(AVG(sa.amount), 2) AS avg_sale_amount
FROM store s
JOIN sale sa ON s.store_id = sa.store_id
GROUP BY
    s.store_id,
    s.store_name,
    s.city,
    s.region
ORDER BY total_revenue DESC;
