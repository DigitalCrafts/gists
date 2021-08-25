-- Query 1
SELECT
    item_code,
    item_description,
    facility_name,
    customer_name
FROM
    items
WHERE
    item_code IN [127800001, 127800002, 127800003]


-- Query 2
SELECT
    item_code,
    item_description,
    facility_name,
    customer_name
FROM
    items
WHERE
    item_code IN (127800001 OR 127800002 OR 127800003)


-- Query 3
SELECT
    item_code,
    item_description,
    facility_name,
    customer_name
FROM
    items
WHERE
    item_code IN (127800001, 127800002, 127800003)