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
LIMIT
    100


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
    gross_weight <= 10
LIMIT
    100


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
    customer_name = 'CONAGRA FROZEN FDS'
    AND gross_weight >= 100 
    AND gross_weight < 500


-- Query 4
SELECT
    facility_name,
    customer_name,
    item_code,
    item_description,
    gross_weight,
    storage_type
FROM
    items
ORDER BY
    gross_weight DESC
LIMIT
    10


-- Query 5
SELECT
    facility_name,
    customer_name,
    item_code,
    item_description,
    gross_weight,
    storage_type
    FROM
    items
WHERE
    storage_type = 'Freezer'
ORDER BY
    gross_weight DESC
LIMIT
    10


-- Query 6
SELECT
    facility_name,
    customer_name,
    item_code,
    item_description,
    density,
    gross_weight,
    storage_type
FROM
    items
WHERE
    density < 10
    AND gross_weight >= 200
ORDER BY
    facility_name,
    gross_weight DESC
LIMIT
    10


-- Query 7
SELECT
    facility_name,
    customer_name,
    item_code,
    item_description,
    density,
    gross_weight,
    storage_type
FROM
    items
WHERE
    facility_id = 'GA-ATL-TW'
    AND storage_type = 'Freezer'
    AND ((gross_weight >= 100 AND gross_weight <= 500) OR density < 20)
ORDER BY
    customer_name,
    gross_weight DESC
LIMIT
    10