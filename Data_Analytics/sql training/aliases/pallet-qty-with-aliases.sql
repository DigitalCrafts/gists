SELECT
    item_code AS "Item code",
    item_description AS "Item description",
    facility_name AS "Facility name",
    customer_name AS "Customer name",
    tie AS "Tie",
    high AS "High",
    billing_stack_qty AS "BSQ",
    tie * high * billing_stack_qty AS "Pallet qty"
FROM
    items AS im
WHERE
    facility_id = 'GA-ATL-TW'