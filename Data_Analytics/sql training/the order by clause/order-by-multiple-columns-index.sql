SELECT  
    facility_name,     -- index = 1
    item_code,         -- index = 2 
    item_description,  -- index = 3
    customer_name,     -- index = 4
    gross_weight       -- index = 5
FROM  
    items
WHERE
    gross_weight < 10
ORDER BY
    1, 2  