SELECT
    -- Basic operators
    column1 + column2,
    column1 - column2,
    column1 * column2,
    column1 / column2,

    -- You can also multiply by constants
    column1 + 2*column2,

    -- You can use as many columns and operators as you'd like
    column1 + column2 / column3 - column4

    -- You can round up or down by using the FLOOR() and CEIL() functions
    FLOOR(column1 * column2),
    CEILING(column1 * column2),

    -- Additionally, you can find the absolute value with the ABS() function
    ABS(column2)
FROM
    ...