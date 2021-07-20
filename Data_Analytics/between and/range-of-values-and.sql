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