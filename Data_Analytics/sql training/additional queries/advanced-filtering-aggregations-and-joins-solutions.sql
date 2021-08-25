-- Query 1
SELECT
    item_code,
    item_description,
    expirary_date
FROM
    inventory_activity
WHERE
    facility_id = 'GA-ATL-TW'
    AND expirary_date BETWEEN '11-01-2020' AND '11-30-2020'


-- Query 2
SELECT
    facility_name,
    customer_name,
    item_code,
    item_description,
    gross_weight
FROM
    items
WHERE
    facility_id = 'GA-ATL-TW'
    AND gross_weight NOT BETWEEN 100 AND 1000


-- Query 3
SELECT
    ia.customer_id AS "Customer ID",
    MAX(ia.units) AS "Largest order",
    MIN(ia.units) AS "Smallest order",
    AVG(ia.units) AS "Avg order size",
    SUM(ia.units) AS "Total units ordered"
    COUNT(ia.facility_id) AS "No. of orders"
FROM
    inventory_activity AS ia
GROUP BY
    ia.customer_id
WHERE
    ia.filter_date BETWEEN '01-01-2020' AND '12-31-2020'


-- Query 4
SELECT
    im.facility_id AS "Facility",
    ia.activity_type AS "Activity type",
    SUM(ia.gross_weight) AS "Total weight",
    COUNT(im.item_code) AS "# of activities"
FROM items AS im
    INNER JOIN inventory_activity AS ia ON im.item_code = ia.item_code
    AND im.customer_id = ia.customer_id
    AND im.facility_id = ia.facility_id
WHERE
    im.customer_id = '29244'
    AND ia.filter_date BETWEEN '11-01-2020' AND '11-30-2020'
GROUP BY
    im.customer_id,
    im.facility_id,
    ia.activity_type


-- Query 5
SELECT
    ia.filter_date,
    SUM(ABS(ia.units)) AS "units_received",
    SUM(ABS(ia.gross_weight)) AS "weight_received"
FROM
    inventory_activity AS ia
WHERE
    facility_id = 'GA-ATL-TW'
    AND ia.item_code = 'L0008-01'
    AND ia.activity_type = 'RECEIPT'
    AND ia.filter_date BETWEEN '01-01-2020' AND '12-31-2020'
GROUP BY
    ia.filter_date
ORDER BY
    ia.filter_date


-- Query 6
SELECT
    facility_name AS "Facility",
    customer_name AS "Customer name",
    COUNT(*) AS "Number of items"
FROM
    items
WHERE
    customer_id IN ('29244','29248','85252')
GROUP BY
    facility_name,
    customer_name
ORDER BY
    3


-- Query 7
SELECT 
    im.facility_name,
    CASE 
        WHEN UPPER(im.item_description) LIKE '%CHICKEN%' THEN 'Chicken'
        WHEN UPPER(im.item_description) LIKE '%COOKIE%' THEN 'Cookie'
        WHEN UPPER(im.item_description) LIKE '%PIE%' THEN 'Pie'
        WHEN UPPER(im.item_description) LIKE '%PIZZA%' THEN 'Pizza'
        WHEN UPPER(im.item_description) LIKE '%POTATO%' THEN 'Potato'
    ELSE 'Other' 
    END AS item_category,
    SUM(ia.gross_weight) AS "weight"
FROM items AS im
    INNER JOIN inventory_activity AS ia ON im.item_code = ia.item_code
    AND im.customer_id = ia.customer_id
    AND im.facility_id = ia.facility_id
WHERE
    ia.activity_type = 'RECEIPT'
    AND ia.filter_date BETWEEN '10-01-2020' AND '10-31-2020'
GROUP BY
    item_category,
    im.facility_name
ORDER BY
    3


-- Query 8
SELECT
    ia.filter_date AS "Date",
    SUM(
    CASE WHEN ia.activity_type = 'RECEIPT' THEN ia.gross_weight ELSE 0 END
    - CASE WHEN ia.activity_type = 'ORDER' AND ia.units < 0 THEN ABS(ia.gross_weight) ELSE 0 END) AS "Gross weight change"
FROM
    inventory_activity AS ia
WHERE
    ia.facility_id = 'GA-ATL-TW'
    AND ia.filter_date  BETWEEN '10-01-2020' AND '11-30-2020'
GROUP BY
    ia.filter_date
ORDER BY
    1