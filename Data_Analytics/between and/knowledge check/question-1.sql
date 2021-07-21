-- Query 1
SELECT
    facility_name,
    customer_name,
    item_code,
    item_description,
    gross_weight,
    density
FROM
    items
WHERE
    facility_id = 'GA-ATL-TW'
    AND density BETWEEN 20 AND 30
    OR gross_weight BETWEEN 30 AND 50


-- Query 2
SELECT
    facility_name,
    customer_name,
    item_code,
    item_description,
    gross_weight,
    density
FROM
    items
WHERE
    facility_id = 'GA-ATL-TW'
    AND (density IN (20, 30) OR gross_weight IN (30, 50))


-- Query 3
SELECT
    facility_name,
    customer_name,
    item_code,
    item_description,
    gross_weight,
    density
FROM
    items
WHERE
    facility_id = 'GA-ATL-TW'
    AND (density BETWEEN 20 AND 30 OR gross_weight BETWEEN 30 AND 50)