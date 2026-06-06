-- Count rows in sale table
SELECT 'sale' AS table_name, COUNT(*) AS row_count FROM sale;

-- Count rows in store table
SELECT 'store' AS table_name, COUNT(*) AS row_count FROM store;

-- Peek at first 5 sale rows
SELECT * FROM sale LIMIT 5;

-- Peek at first 5 store rows
SELECT * FROM store LIMIT 5;
