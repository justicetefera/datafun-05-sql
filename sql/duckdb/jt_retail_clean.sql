-- JT Retail Clean Script
-- Drops and recreates the retail tables for a fresh JT pipeline run.

BEGIN TRANSACTION;

DROP TABLE IF EXISTS sale;
DROP TABLE IF EXISTS store;

CREATE TABLE store (
    store_id TEXT PRIMARY KEY,
    store_name TEXT NOT NULL,
    city TEXT NOT NULL,
    region TEXT NOT NULL
);

CREATE TABLE sale (
    sale_id TEXT PRIMARY KEY,
    store_id TEXT NOT NULL,
    product_category TEXT NOT NULL,
    quantity INTEGER NOT NULL,
    amount DOUBLE NOT NULL,
    sale_date TEXT NOT NULL
);

COMMIT;
