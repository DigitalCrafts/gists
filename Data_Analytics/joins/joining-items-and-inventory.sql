SELECT
    ...
FROM items AS im
INNER JOIN inventory_activity AS ia ON im.item_code = ia.item_code
    AND im.customer_id = ia.customer_id
    AND im.facility_id = ia.facility_id