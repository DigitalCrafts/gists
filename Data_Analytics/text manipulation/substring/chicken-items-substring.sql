SELECT
    item_code,
    item_description,
    facility_name,
    customer_name
FROM
    items
WHERE
    LOWER(SUBSTRING(item_description, 1, 15)) LIKE '%chicken%'
    AND facility_id = 'GA-ATL-TW'
LIMIT
    100