SELECT
    item_code,
    item_description,
    facility_name,
    gross_weight,
    CASE WHEN
        storage_type IN ("Freezer", "FREEZER", "F", "f") THEN "Freezer"
        ELSE "Non-freezer"
    END AS "storage_type"
FROM
    items
WHERE
    facility_id = 'GA-ATL-TW'