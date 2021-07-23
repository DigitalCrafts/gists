SELECT
	bfw.filter_date AS "Date",
    SUM(bfw.full_pallet_pick) AS "No. full pallet picks"
FROM
	items AS im
    INNER JOIN basic_framework AS bfw ON im.item_code = bfw.item_code
		AND im.customer_id = bfw.customer_id
        AND im.facility_id = bfw.facility_id
GROUP BY
	bfw.filter_date
ORDER BY
	1