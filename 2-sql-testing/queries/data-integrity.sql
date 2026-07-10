-- ============================================
-- 数据完整性校验查询
-- 目的：验证数据库中无脏数据、孤儿记录、约束违规
-- ============================================

USE ecommerce_test;

-- 1. 检查用户表：必填字段为空
-- 预期结果：0 行（postal_code 和 email 可为空或空字符串的业务场景除外）
SELECT 'EMPTY_EMAIL' AS check_type, id, username
FROM users
WHERE email IS NULL OR email = '';

-- 2. 检查用户表：username 唯一性
-- 预期结果：0 行
SELECT 'DUP_USERNAME' AS check_type, username, COUNT(*) AS cnt
FROM users
GROUP BY username
HAVING COUNT(*) > 1;

-- 3. 检查商品表：负价格或负库存
-- 预期结果：0 行
SELECT 'NEGATIVE_PRICE_OR_STOCK' AS check_type, id, name, price, stock
FROM products
WHERE price < 0 OR stock < 0;

-- 4. 检查订单表：total_amount 不等于 order_items 汇总
-- 预期结果：0 行
SELECT 'ORDER_AMOUNT_MISMATCH' AS check_type,
       o.id AS order_id,
       o.total_amount,
       SUM(oi.quantity * oi.unit_price) AS calculated_total
FROM orders o
JOIN order_items oi ON o.id = oi.order_id
GROUP BY o.id, o.total_amount
HAVING o.total_amount != SUM(oi.quantity * oi.unit_price);

-- 5. 检查孤儿订单明细：order_items 引用了不存在的订单
-- 预期结果：0 行
SELECT 'ORPHAN_ORDER_ITEMS' AS check_type, oi.id, oi.order_id
FROM order_items oi
LEFT JOIN orders o ON oi.order_id = o.id
WHERE o.id IS NULL;

-- 6. 检查孤儿购物车：cart 引用了不存在的用户或商品
-- 预期结果：0 行
SELECT 'ORPHAN_CART_USER' AS check_type, c.id, c.user_id
FROM cart c
LEFT JOIN users u ON c.user_id = u.id
WHERE u.id IS NULL;

SELECT 'ORPHAN_CART_PRODUCT' AS check_type, c.id, c.product_id
FROM cart c
LEFT JOIN products p ON c.product_id = p.id
WHERE p.id IS NULL;
