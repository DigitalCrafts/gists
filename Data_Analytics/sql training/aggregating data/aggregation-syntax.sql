SELECT
    group_by_column,
    FUNCTION(aggregate_column) -- MIN(), MAX(), AVG(), COUNT(), SUM()
FROM
    table_name
WHERE
    some_conditions
GROUP BY
    group_by_column
ORDER BY
    some_columns