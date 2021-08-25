SELECT
    ia.activity_type AS "Activity type",
    SUM(ia.units) AS "No. of units",
    COUNT(ia.item_code) AS "No. of activities",
    AVG(ia.units) AS "Avg no. of units"
FROM
    ...