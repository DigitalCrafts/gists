SELECT
    im.item_code AS "Item code",
    im.item_description AS "Item description",
    im.customer_name AS "Customer name",
    ia.units AS "Units",
    ia.gross_weight AS "Gross weight",
    ia.filter_date AS "Date received"
FROM items AS im
INNER JOIN inventory_activity AS ia ON im.item_code = ia.item_code
    AND im.customer_id = ia.customer_id
    AND im.facility_id = ia.facility_id
WHERE
    ia.facility_id = 'GA-ATL-TW'
    AND im.item_code = 'L0008-01'
    AND ia.activity_type = 'RECEIPT'
    AND ia.gross_weight >= 1700