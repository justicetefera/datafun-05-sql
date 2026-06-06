-- Drop views if they exist
DROP VIEW IF EXISTS jt_sales_clean;
DROP VIEW IF EXISTS jt_store_clean;

-- Clean sales view
CREATE VIEW jt_sales_clean AS
SELECT
    sale_id,
    store_id,
    product_category,
    quantity,
    amount,
    sale_date
FROM sale
WHERE amount > 0;

-- Clean store view
CREATE VIEW jt_store_clean AS
SELECT
    store_id,
    store_name,
    city,
    region
FROM store;
