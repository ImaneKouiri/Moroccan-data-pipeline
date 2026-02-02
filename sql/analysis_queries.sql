-- 1. Sanity check: number of rows

SELECT COUNT(*) AS total_rows
FROM socio_economic_indicators;

-- 2. List available indicators

SELECT DISTINCT indicator_name, indicator_code
FROM socio_economic_indicators
ORDER BY indicator_name;

-- 3. Population evolution over time

SELECT year, value AS population
FROM socio_economic_indicators
WHERE indicator_code = 'SP.POP.TOTL'
ORDER BY year;

-- 4. GDP evolution (current USD)

SELECT year, value AS gdp_usd
FROM socio_economic_indicators
WHERE indicator_code = 'NY.GDP.MKTP.CD'
ORDER BY year;

-- 5. Unemployment rate trend

SELECT year, value AS unemployment_rate
FROM socio_economic_indicators
WHERE indicator_code = 'SL.UEM.TOTL.ZS'
ORDER BY year;

-- 6. Average value per indicator (sanity check)

SELECT
    indicator_name,
    ROUND(AVG(value), 2) AS average_value
FROM socio_economic_indicators
GROUP BY indicator_name
ORDER BY indicator_name;
