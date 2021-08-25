-- Query 1
SELECT DISTINCT
    item_code,
    item_description
FROM
    items


-- Query 2
SELECT LIMIT DISTINCT
    item_code,
    item_description
FROM
    items


-- Query 3
SELECT 
    facility_name,
    item_code,
    item_description
FROM DISTINCT
    items