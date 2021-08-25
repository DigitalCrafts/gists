SELECT
    item_code,
    item_description
FROM
    items
WHERE
    logical_expression_1 = condition_1 
    AND logical_expression_2 <= condition_2
    AND logical_expression_3 >= condition_3
    AND ...