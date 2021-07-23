SELECT
    ia.filter_date AS "Date",
    SUM(FLOOR(ABS(ia.units) / (im.billing_stack_qty * im.tie * im.high ))) AS "full_pallet_pick"
FROM items AS im
INNER JOIN inventory_activity AS ia ON
	im.item_code = ia.item_code
    AND im.facility_id = ia.facility_id
    AND im.customer_id = ia.customer_id
WHERE
    im.facility_id = 'GA-ATL-TW'
    AND ia.filter_date BETWEEN '10-01-2020' AND '11-30-2020'
GROUP BY
    ia.filter_date
ORDER BY
    1