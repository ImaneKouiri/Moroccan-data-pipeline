CREATE TABLE IF NOT EXISTS socio_economic_indicators (
    id SERIAL PRIMARY KEY,
    country VARCHAR(50),
    indicator_code VARCHAR(50),
    indicator_name TEXT,
    year INT,
    value NUMERIC,
    source VARCHAR(100)
);
