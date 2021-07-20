SELECT
    item_code,
    item_description,
    facility_name,
    customer_name,
    unit_height,
    unit_width,
    unit_height * unit_width
FROM
    items
WHERE
    customer_name = 'CONAGRA FROZEN FDS'