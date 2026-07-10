-- ============================================
-- 业务逻辑验证查询
-- 目的：验证业务规则是否正确落地
-- ============================================

USE ecommerce_test;

-- 1. 统计各用户订单数及消费总额（TOP 3 消费用户）
SELECT u.username,
       u.first_name,
       u.last_name,
       COUNT(o.id)               AS order_count,
       COALESCE(SUM(o.total_amount), 0) AS total_spent
FROM users u
LEFT JOIN orders o ON u.id = o.user_id AND o.status = 'completed'
GROUP BY u.id, u.username, u.first_name, u.last_name
ORDER BY total_spent DESC
LIMIT 3;

-- 2. 热门商品排行（按销量和销售额）
SELECT p.name,
       SUM(oi.quantity)            AS total_sold,
       SUM(oi.quantity * oi.unit_price) AS total_revenue
FROM products p
JOIN order_items oi ON p.id = oi.product_id
JOIN orders o ON oi.order_id = o.id AND o.status != 'cancelled'
GROUP BY p.id, p.name
ORDER BY total_sold DESC;

-- 3. 库存预警：库存低于 20 的商品
SELECT id, name, stock
FROM products
WHERE stock < 20
ORDER BY stock ASC;

-- 4. 各状态订单占比
SELECT status,
       COUNT(*)   AS order_count,
       ROUND(COUNT(*) * 100.0 / (SELECT COUNT(*) FROM orders), 2) AS percentage
FROM orders
GROUP BY status;

-- 5. 无效用户检测：注册超过 30 天但从没有过任何订单
SELECT u.id, u.username, u.email, u.created_at
FROM users u
LEFT JOIN orders o ON u.id = o.user_id
WHERE o.id IS NULL
  AND u.created_at < DATE_SUB(NOW(), INTERVAL 30 DAY);

-- 6. 有商品在购物车但无任何订单的用户（潜在流失用户）
SELECT u.id, u.username, COUNT(c.id) AS cart_items
FROM users u
JOIN cart c ON u.id = c.user_id
LEFT JOIN orders o ON u.id = o.user_id
WHERE o.id IS NULL
GROUP BY u.id, u.username;
