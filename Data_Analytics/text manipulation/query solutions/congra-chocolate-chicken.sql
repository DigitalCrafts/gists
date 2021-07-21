SELECT
    customer_name,
    item_code,
    item_description,
    CASE 
        WHEN LOWER(SUBSTRING(storage_type,1,1)) = 'f' THEN 'Freezer'
        WHEN LOWER(SUBSTRING(storage_type,1,1)) = 'c' THEN 'Cooler'
        ELSE 'Other'
	END AS "storage_category",
    tie,
    high,
    billing_stack_qty
FROM
    items
WHERE
    customer_id = '29244'
    AND LOWER(SUBSTRING(storage_type,1,1)) IN ('c','f')
    AND (LOWER(SUBSTRING(item_description, 20)) LIKE '%chicken%' OR LOWER(SUBSTRING(item_description, 1, 20)) LIKE '%chocolate%')
LIMIT
    100;