SELECT
    facility_name,
    COUNT(item_code)
FROM
    items
GROUP BY
    facility_name