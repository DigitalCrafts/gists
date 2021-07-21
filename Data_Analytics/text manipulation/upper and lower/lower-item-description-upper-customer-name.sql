SELECT
    item_code,
    UPPER(item_description) AS "item_description",
    LOWER(customer_name) AS "customer_name",
    facility_name,
    gross_weight,
    density
FROM
    items
WHERE
    facility_id = 'GA-ATL-TW'
LIMIT
    100