SELECT
    customer_name,
    item_code,
    item_description,
    gross_weight
FROM
    items
WHERE
    gross_weight <= 10
    AND (customer_name = 'CONAGRA FROZEN FDS' OR customer_name = 'Venture Foods LLC')