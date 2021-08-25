SELECT
    ia.activity_type AS "Activity type",
    SUM(ia.units) AS "No. of units",
    COUNT(ia.item_code) AS "No. of activities",
    AVG(ia.units) AS "Avg no. of units"
FROM
    items AS im
    INNER JOIN inventory_activity AS ia
    ON ia.item_code = im.item_code 
        AND ia.customer_id = im.customer_id 
        AND ia.facility_id = im.facility_id
WHERE
    ia.facility_id = 'GA-ATL-TW'
    AND im.item_code = 'L0008-01'
    AND ia.filter_date BETWEEN '11-01-2020' AND '11-30-2020'
GROUP BY
    ia.activity_type
ORDER BY
    1, 4