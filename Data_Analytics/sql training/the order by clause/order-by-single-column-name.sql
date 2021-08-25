SELECT  
    facility_name,    -- index = 1
    item_code,        -- index = 2
    item_description, -- index = 3
    gross_weight,     -- index = 4
    density           -- index = 5
FROM
    items   
WHERE
    customer_name = 'CONAGRA FROZEN FDS'  
    AND gross_weight  <  10  
ORDER BY  
    gross_weight
