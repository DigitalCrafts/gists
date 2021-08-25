SELECT
    ...
FROM
    items AS im
    INNER JOIN inventory_activity AS ia
    ON ia.item_code = im.item_code 
        AND ia.customer_id = im.customer_id 
        AND ia.facility_id = im.facility_id
WHERE
    ...