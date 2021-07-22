SELECT
    facility_name,
    COUNT(DISTINCT customer_id)
FROM
    items
GROUP BY
    facility_name
ORDER BY
    2