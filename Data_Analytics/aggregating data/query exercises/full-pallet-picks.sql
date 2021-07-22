SELECT
	im.item_code,
    im.customer_id,
    im.facility_id,
    ia.activity_type,
	ia.units,
    FLOOR(ABS(ia.units) / (im.billing_stack_qty * im.tie * im.high)) AS "full_pallet_pick",
    ia.filter_date
FROM items AS im
INNER JOIN inventory_activity AS ia ON (
	im.item_code = ia.item_code
    AND im.facility_id = ia.facility_id
    AND im.customer_id = ia.customer_id)
WHERE
    im.facility_id = 'GA-ATL-TW'
    AND ia.filter_date BETWEEN '11-01-2020' AND '11-30-2020'