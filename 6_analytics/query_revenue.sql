-- Revenue analytics over the enriched sales fact table.
-- Intended to be run after creating a Spark SQL temp view:
-- fact_sales_enriched.createOrReplaceTempView("fact_sales_enriched")

-- 1. Revenue by product category
SELECT
    category,
    COUNT(*) AS total_orders,
    SUM(quantity) AS total_units_sold,
    ROUND(SUM(quantity * price), 2) AS total_revenue,
    ROUND(AVG(quantity * price), 2) AS avg_order_value
FROM fact_sales_enriched
GROUP BY category
ORDER BY total_revenue DESC;

-- 2. Revenue by region
SELECT
    region,
    COUNT(*) AS total_orders,
    SUM(quantity) AS total_units_sold,
    ROUND(SUM(quantity * price), 2) AS total_revenue
FROM fact_sales_enriched
GROUP BY region
ORDER BY total_revenue DESC;

-- 3. Top products by revenue
SELECT
    product_id,
    product_name,
    category,
    COUNT(*) AS order_count,
    SUM(quantity) AS units_sold,
    ROUND(SUM(quantity * price), 2) AS total_revenue
FROM fact_sales_enriched
GROUP BY product_id, product_name, category
ORDER BY total_revenue DESC
LIMIT 10;

-- 4. Monthly revenue trend
SELECT
    YEAR(sale_date) AS sale_year,
    MONTH(sale_date) AS sale_month,
    COUNT(*) AS total_orders,
    ROUND(SUM(quantity * price), 2) AS monthly_revenue
FROM fact_sales_enriched
GROUP BY YEAR(sale_date), MONTH(sale_date)
ORDER BY sale_year, sale_month;