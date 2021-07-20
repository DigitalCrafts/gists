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
    OR customer_name = 'Venture Foods LLC'
    OR customer_name = 'LAMB WESTON / CONAGRA FOODS'