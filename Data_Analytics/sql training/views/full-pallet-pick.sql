SELECT 
    ...
    FLOOR(ABS(ia.units) / (im.billing_stack_qty * im.tie * im.high)) as "full_pallet_pick"
    ...
FROM items AS im
INNER JOIN inventory_activity AS ia ON im.item_code = ia.item_code
    AND im.facility_id = ia.facility_id
    AND im.customer_id = ia.customer_id