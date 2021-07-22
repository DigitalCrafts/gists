SELECT
    im.customer_id AS "Customer ID",
    im.customer_name AS "Customer name",
    ia.activity_type AS "Activity type",
    ia.units AS "No. of units",
    ia.filter_date AS "Activity date"
FROM
    items AS im
    INNER JOIN inventory_activity AS ia ON ia.item_code = im.item_code 
        AND ia.customer_id = im.customer_id 
        AND ia.facility_id = im.facility_id
WHERE
    ia.facility_id = 'GA-ATL-TW'
    AND im.item_code = 'L0008-01'
    AND ia.filter_date BETWEEN '11-01-2020' AND '11-30-2020'
ORDER BY
    2, 5