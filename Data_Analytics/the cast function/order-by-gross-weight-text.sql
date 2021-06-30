SELECT
    facility_name,
    item_code,
    item_description,
    customer_name,
    gross_weight
FROM
    items
ORDER BY
    gross_weight DESC