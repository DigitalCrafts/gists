SELECT
    ...
FROM
    ...
WHERE
    -- match records which begin with 'pattern'
    text_column LIKE 'pattern%' 

    -- match records which end with 'pattern' 
    text_column LIKE '%pattern'

    -- match records which contain 'pattern'  
    text_column LIKE '%pattern%'

    -- match records which contain 'first_pattern' and 'second_pattern' 
    text_column LIKE '%first_pattern%second_pattern%'