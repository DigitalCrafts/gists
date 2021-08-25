SELECT
    item_code,
    item_description,
    facility_name,
    gross_weight,
    density
FROM
    items
WHERE
    customer_name = 'CONAGRA FROZEN FDS'
    AND (gross_weight < 10 OR density < 100)