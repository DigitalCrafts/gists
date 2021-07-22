SELECT
    ia.facility_id AS "Facility ID",
    MAX(ia.units) AS "Largest order",
    MIN(ia.units) AS "Smallest order",
    AVG(ia.units) AS "Avg order size",
    SUM(ia.units) AS "Total units ordered"
    COUNT(ia.facility_id) AS "No. of orders"
FROM
    inventory_activity AS ia
GROUP BY
    ia.facility_id