SELECT COUNT(*) AS total_rows, SUM(quantity * unit_price) AS total_revenue FROM fact_sales
UNION ALL
SELECT COUNT(*) AS total_rows, SUM(amount) AS total_revenue FROM sales;