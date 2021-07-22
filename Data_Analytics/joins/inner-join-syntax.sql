SELECT
    table_1.column_1,
    table_1.column_2,
    table_2.column_1,
    table_2.column_2,
    ...
FROM 
    table_1
    INNER JOIN table_2 ON table_1.primary_key = table_2.foreign_key