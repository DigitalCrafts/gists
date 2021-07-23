-- full formula
SELECT
    im.tie * im.high AS hps,
    im.tie * im.high * im.billing_stack_qty AS fps,
    ...


-- re-using column alias
SELECT
    im.tie * im.high AS hps,
    hps * im.billing_stack_qty AS fps,
    ...