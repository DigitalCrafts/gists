SELECT
    item_code,
    item_description
FROM 
    items
WHERE
    item_description LIKE '%CHICKEN%' --`item_description` must contain the word `CHICKEN`