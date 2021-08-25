SELECT
    item_code,
    item_description,
    facility_name,
    customer_name,
    gross_weight,
    CASE
        WHEN gross_weight < 10 THEN 'Not heavy'
        WHEN gross_weight < 25 THEN 'Getting heavier'
        WHEN gross_weight < 50 THEN 'Almost too heavy'
        ELSE 'Way too heavy for me'
    END AS "weight_category"
FROM
    items