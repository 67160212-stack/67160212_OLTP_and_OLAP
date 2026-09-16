SELECT 
    SUM(amount) AS revenue, 
    COUNT(DISTINCT order_id) AS orders, 
    ROUND(CAST(SUM(amount) AS FLOAT) / COUNT(DISTINCT order_id), 2) AS aov, 
    ROUND(AVG(amount), 2) AS avg_line 
FROM sales;