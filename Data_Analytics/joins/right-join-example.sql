-- Using our example database
SELECT
    im.item_code,
    im.item_description,
    ia.activity,
    ia.units
FROM
    items AS im
    RIGHT JOIN inventory_activity AS ia ON im.item_code = ia.item_code