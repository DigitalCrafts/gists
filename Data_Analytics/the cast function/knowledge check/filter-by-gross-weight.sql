-- Query 1
SELECT
    item_code,
    item_description,
    gross_weight
FROM
    items
WHERE
    gross_weight < 10


-- Query 2
SELECT
    item_code,
    item_description,
    CAST(gross_weight AS NUMERIC)
FROM
    items
WHERE
    gross_weight < 10


-- Query 3
SELECT
    item_code,
    item_description,
    gross_weight
FROM
    items
WHERE
    CAST(gross_weight AS NUMERIC) < 10