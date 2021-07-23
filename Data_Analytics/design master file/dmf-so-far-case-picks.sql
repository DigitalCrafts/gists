SELECT
	im.item_code,
    im.customer_id,
    im.facility_id,
    ia.filter_date,

    -- input variables
    ABS(ia.units) AS "N",
    ABS(ia.gross_weight) AS "gw",
    im.tie AS "t",
    im.high AS "h",
    im.billing_stack_qty AS "bsq",
    t * h AS "hps",
    hps * bsq AS "fps",

    -- full pallet picks
    FLOOR(N / fps) AS "fpp",
    fpp * fps AS "fpq",
    CASE WHEN fpp >= 1 THEN 1 ELSE 0 END AS "fpl",

    -- half pallet picks
    FLOOR((N - fpq) / hps) AS "hpp", 
    hpp * hps AS "hpq",
    CASE WHEN hpp >= 1 THEN 1 ELSE 0 END AS "hpl",

    -- layer picks
    FLOOR((N - fpq - hpq) / t) AS "lp",
    lp * t AS "lpq",
    CASE WHEN lp >= 1 THEN 1 ELSE 0 END AS "lpl",

    -- case picks
    N - fpq - hpq - lpq AS "cpq",
    cASE WHEN cpq >= 1 THEN 1 ELSE 0 END AS "cpl",
        
FROM items AS im
INNER JOIN inventory_activity AS ia ON
	im.item_code = ia.item_code
    AND im.facility_id = ia.facility_id
    AND im.customer_id = ia.customer_id
where
	ia.activity_type = 'ORDER'