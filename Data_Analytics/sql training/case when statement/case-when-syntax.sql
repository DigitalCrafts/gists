SELECT
    column_1,
    CASE 
        WHEN first_logical_expression_on_column_1 THEN result_1
        WHEN second_logical_expression_on_column_1 THEN result_2
        WHEN third_logical_expression_on_column_1 THEN result_3
        ...
        ELSE result_final
    END AS "CASE WHEN column" -- it is best practice to give case/when columns an alias!
FROM
    ...