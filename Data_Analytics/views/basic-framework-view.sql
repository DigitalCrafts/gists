CREATE VIEW globali3pl.basic_framework AS
SELECT
    im.item_code,
    im.facility_id,
    im.customer_id,
    ia.units,
    FLOOR(ABS(ia.units) / (im.billing_stack_qty * im.tie * im.high)) AS "full_pallet_pick"
    ia.filter_date
FROM
    items AS im INNER JOIN inventory_activity AS ia ON 
        ia.item_code = im.item_code
        AND ia.facility_id = im.facility_id
        AND ia.customer_id = im.customer_id
WHERE
    im.facility_id = 'GA-ATL-TW'
    AND ia.filter_date BETWEEN '10-01-2020' AND '11-30-2020'
    AND ia.activity_type = 'ORDER'
    AND ia.units < 0;