SELECT
    im.facility_name,
    COUNT(DISTINCT im.item_code) AS "No. distincts items received"
FROM items AS im
INNER JOIN inventory_activity AS ia ON im.item_code = ia.item_code
    AND im.facility_id = ia.facility_id
    AND im.customer_id = ia.customer_id
WHERE
    ia.activity_type = 'RECEIPT'
    AND LOWER(im.storage_type) LIKE 'f%'
    AND ia.filter_date BETWEEN '11-01-2020' AND '11-30-2020'