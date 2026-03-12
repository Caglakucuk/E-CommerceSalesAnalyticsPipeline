--TOP 10 SATIŞ YAPAN ÜRÜN KATEGORİSİ--
SELECT
p.product_category,
COUNT(f.sales_id) AS total_sales
FROM fact_sales f
JOIN dim_product p
ON f.product_id =p.product_id
GROUP BY p.product_category
ORDER BY total_sales DESC
LIMIT 10;

-- AYLIK SATIŞ TRENDI--
SELECT
d.year,
d.month,
COUNT (f.sales_id) AS total_sales,
SUM(f.price) AS total_revenue
FROM fact_sales f
JOIN dim_date d
ON f.date_id=d.date_id
GROUP BY d.year, d.month
ORDER BY d.year, d.month;

-- EN ÇOK SATIŞ YAPAN 10 ŞEHİR(MÜŞTERİ BAZLI)
SELECT 
    c.customer_city,
    COUNT(f.sales_id) AS total_sales
FROM fact_sales f
JOIN dim_customer c
    ON f.customer_id = c.customer_id
GROUP BY c.customer_city
ORDER BY total_sales DESC
LIMIT 10;

--EN ÇOK GELİR GETİREN SATICI
SELECT
s.seller_id,
s.seller_city,
SUM(f.price) AS total_revenue
FROM fact_sales f
JOIN dim_seller s
ON f.seller_id = s.seller_id
GROUP BY s.seller_id, s.seller_city
ORDER BY total_revenue DESC
LIMIT 10;