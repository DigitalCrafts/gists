SELECT
    im.item_code,
    im.facility_id,
    im.customer_id,
    im.tie,
    im.high,
    ia.activity_type,
    ia.units,
    ia.gross_weight,
    ia.filter_date
FROM
    items as im
    INNER JOIN inventory_activity as ia 
    ON ia.item_code = im.item_code
        AND ia.facility_id = im.facility_id
        AND ia.customer_id = im.customer_id
WHERE
    im.facility_id = 'GA-ATL-TW'
    AND ia.filter_date BETWEEN '10-01-2020' AND '11-30-2020'