CREATE OR REPLACE TABLE sale AS
SELECT * FROM read_csv_auto('data/sale.csv');

CREATE OR REPLACE TABLE store AS
SELECT * FROM read_csv_auto('data/store.csv');
