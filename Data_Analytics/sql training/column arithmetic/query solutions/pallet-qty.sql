SELECT
    item_code,
    item_description,
    facility_name,
    customer_name,
    tie,
    high,
    billing_stack_qty,
    tie * high * billing_stack_qty
FROM
    items
WHERE
    facility_name = 'Atlanta - Tradewater (JDAWMS2)'