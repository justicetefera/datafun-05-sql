BEGIN TRANSACTION;

-- JT custom bootstrap: create store table
CREATE TABLE IF NOT EXISTS store (
    store_id TEXT PRIMARY KEY,
    store_name TEXT NOT NULL,
    city TEXT NOT NULL,
    region TEXT NOT NULL
);

-- JT custom bootstrap: create sale table
CREATE TABLE IF NOT EXISTS sale (
    sale_id TEXT PRIMARY KEY,
    store_id TEXT NOT NULL,
    product_category TEXT NOT NULL,
    quantity INTEGER NOT NULL,
    amount DOUBLE NOT NULL,
    sale_date TEXT NOT NULL
);

COMMIT;
