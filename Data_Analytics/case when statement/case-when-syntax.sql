SELECT
    column_1,
    CASE 
        WHEN condition_1 THEN result_1
        WHEN condition_2 THEN result_2
        WHEN condition_3 THEN result_3
        ...
        ELSE result_final
    END AS "CASE WHEN column"
FROM
    ...