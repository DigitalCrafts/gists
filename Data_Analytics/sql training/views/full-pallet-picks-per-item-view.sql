SELECT
    bfw.item_code AS "Item code",
    im.item_description AS "Description",
    SUM(bfw.full_pallet_pick) AS "No. full pallet picks"
FROM
    items AS im
    INNER JOIN basic_framework AS bfw ON im.item_code = bfw.item_code
        AND im.customer_id = bfw.customer_id
        AND im.facility_id = bfw.facility_id
GROUP BY
    bfw.item_code,
    im.item_description
ORDER BY
    3 DESC