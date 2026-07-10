-- ============================================
-- 模拟电商测试数据
-- ============================================

USE ecommerce_test;

-- 用户数据
INSERT INTO users (username, password, first_name, last_name, email, postal_code, status) VALUES
('standard_user',     'secret_sauce', 'Zhang',  'San',    'zhangsan@test.com',   '100000', 'active'),
('locked_out_user',   'secret_sauce', 'Li',     'Si',     'lisi@test.com',       '200000', 'locked'),
('problem_user',      'secret_sauce', 'Wang',   'Wu',     'wangwu@test.com',     '300000', 'active'),
('glitch_user',       'secret_sauce', 'Zhao',   'Liu',    'zhaoliu@test.com',    '400000', 'active'),
('test_user_01',      'pass123',      'Alice',  'Chen',   'alice@test.com',      '510000', 'active'),
('test_user_02',      'pass123',      'Bob',    'Brown',  'bob@test.com',        '610000', 'active'),
('test_user_03',      'pass123',      'Carol',  'Davis',  'carol@test.com',      '710000', 'inactive'),
('test_user_04',      'pass123',      'David',  'Evans',  'david@test.com',      NULL,     'active'),
('test_user_05',      'pass123',      'Eve',    'Foster', 'eve@test.com',        '810000', 'active'),
('test_user_06',      'pass123',      'Frank',  'Green',  'frank@test.com',      '',        'active');

-- 商品数据
INSERT INTO products (name, description, price, image_url, stock) VALUES
('Sauce Labs Backpack',       'carry.allTheThings() with the sleek, streamlined Sly Pack',                   29.99, '/img/sauce-backpack.jpg',     50),
('Sauce Labs Bike Light',     'A red light is not the desired state in testing but it helps to ride safe',  9.99,  '/img/bike-light.jpg',       100),
('Sauce Labs Bolt T-Shirt',   'Get your testing superhero on with the bolt t-shirt',                      15.99, '/img/bolt-t-shirt.jpg',      75),
('Sauce Labs Fleece Jacket',  'Its every testers dream to have this jacket',                              49.99, '/img/sauce-pullover.jpg',    30),
('Sauce Labs Onesie',         'Rib snap infant onesie for testing',                                       7.99,  '/img/red-onesie.jpg',       200),
('Test.allTheThings() T-Shirt','This classic t-shirt is perfect for test automation engineers',            15.99, '/img/red-tatt.jpg',          60),
('Sauce Labs Chair',          'Ergonomic chair for test engineers who sit all day',                       89.99, '/img/chair.jpg',             10),
('Sauce Labs Monitor',        'A 27-inch monitor with perfect color accuracy for test reports',           199.99,'/img/monitor.jpg',           5),
('Sauce Labs Keyboard',       'Mechanical keyboard with Cherry MX switches',                             129.99,'/img/keyboard.jpg',         15),
('Sauce Labs Mouse',          'Wireless mouse with 16000 DPI sensor',                                    59.99, '/img/mouse.jpg',            20);

-- 正常订单数据
INSERT INTO orders (user_id, total_amount, tax, status, first_name, last_name, postal_code) VALUES
(1, 29.99,  2.40, 'completed', 'Zhang', 'San',   '100000'),
(1, 25.98,  2.08, 'completed', 'Zhang', 'San',   '100000'),
(2, 15.99,  1.28, 'completed', 'Li',    'Si',    '200000'),
(5, 49.99,  4.00, 'pending',   'Alice', 'Chen',  '510000'),
(6, 199.99, 16.00,'completed', 'Bob',   'Brown', '610000'),
(6, 7.99,   0.64, 'cancelled', 'Bob',   'Brown', '610000'),
(9, 89.99,  7.20, 'completed', 'Eve',   'Foster','810000');

-- 订单明细
INSERT INTO order_items (order_id, product_id, quantity, unit_price) VALUES
(1, 1, 1, 29.99),
(2, 2, 1, 9.99),
(2, 3, 1, 15.99),
(3, 3, 1, 15.99),
(4, 4, 1, 49.99),
(5, 8, 1, 199.99),
(6, 5, 1, 7.99),
(7, 7, 1, 89.99);

-- 购物车数据
INSERT INTO cart (user_id, product_id, quantity) VALUES
(1, 2, 2),
(1, 3, 1),
(5, 6, 1),
(5, 10, 1),
(6, 7, 1);
