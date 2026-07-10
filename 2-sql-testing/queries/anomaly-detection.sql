-- ============================================
-- 异常数据发现查询
-- 目的：发现数据中的异常模式和潜在 Bug
-- ============================================

USE ecommerce_test;

-- 1. 同一用户同一时间创建多个订单（可能的重复提交 Bug）
SELECT user_id, created_at, COUNT(*) AS duplicate_count
FROM orders
GROUP BY user_id, created_at
HAVING COUNT(*) > 1;

-- 2. postal_code 格式异常（非纯数字或为空）
SELECT id, username, postal_code
FROM users
WHERE postal_code IS NOT NULL
  AND postal_code != ''
  AND postal_code NOT REGEXP '^[0-9]+$';

-- 3. 订单信息与用户档案不一致（收货姓名与注册姓名不同）
SELECT o.id AS order_id,
       o.first_name AS order_first_name,
       o.last_name  AS order_last_name,
       u.first_name AS user_first_name,
       u.last_name  AS user_last_name
FROM orders o
JOIN users u ON o.user_id = u.id
WHERE o.first_name != u.first_name OR o.last_name != u.last_name;

-- 4. 被取消的订单数量超过已完成订单的 50%（高取消率预警）
SELECT
    SUM(CASE WHEN status = 'cancelled' THEN 1 ELSE 0 END) AS cancelled_count,
    SUM(CASE WHEN status = 'completed' THEN 1 ELSE 0 END) AS completed_count,
    ROUND(
        SUM(CASE WHEN status = 'cancelled' THEN 1 ELSE 0 END) * 100.0 /
        NULLIF(SUM(CASE WHEN status = 'completed' THEN 1 ELSE 0 END), 0),
        2
    ) AS cancel_ratio_pct
FROM orders;

-- 5. 购物车中存在已停售或库存为 0 的商品
SELECT c.id, c.user_id, p.name, p.stock, c.quantity
FROM cart c
JOIN products p ON c.product_id = p.id
WHERE p.stock = 0;

-- 6. 使用 SQL 聚合找出"问题用户"：该用户订单价格与 order_items 明细总和偏差 > 0.01
SELECT o.user_id,
       u.username,
       o.id AS order_id,
       o.total_amount,
       SUM(oi.quantity * oi.unit_price) AS item_total,
       ABS(o.total_amount - SUM(oi.quantity * oi.unit_price)) AS discrepancy
FROM orders o
JOIN order_items oi ON o.id = oi.order_id
JOIN users u ON o.user_id = u.id
GROUP BY o.user_id, u.username, o.id, o.total_amount
HAVING discrepancy > 0.01;
