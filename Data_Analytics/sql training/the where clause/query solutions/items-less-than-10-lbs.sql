SELECT
    facility_name,
    customer_name,
    item_code,
    item_description,
    gross_weight
FROM
    items
WHERE
    gross_weight < 10