# SQL 测试结果报告

## 数据库信息

| 项目 | 值 |
|---|---|
| 数据库名 | ecommerce_test |
| 引擎 | MySQL 8.0.34 InnoDB |
| 表数量 | 5 (users, products, orders, order_items, cart) |
| 模拟数据行数 | users: 10 / products: 10 / orders: 7 / order_items: 8 / cart: 5 |

## 执行结果

### 一、数据完整性校验 (data-integrity.sql)

| 查询 | 目的 | 预期 | 实际 | 状态 |
|---|---|---|---|---|
| EMPTY_EMAIL | 邮箱为空 | 0 行 | 0 行 | PASS |
| DUP_USERNAME | 用户名重复 | 0 行 | 0 行 | PASS |
| NEGATIVE_PRICE_OR_STOCK | 负价格/负库存 | 0 行 | 0 行 | PASS |
| ORDER_AMOUNT_MISMATCH | 订单金额不一致 | 0 行 | 0 行 | PASS |
| ORPHAN_ORDER_ITEMS | 孤儿订单明细 | 0 行 | 0 行 | PASS |
| ORPHAN_CART_USER | 孤儿购物车(用户) | 0 行 | 0 行 | PASS |
| ORPHAN_CART_PRODUCT | 孤儿购物车(商品) | 0 行 | 0 行 | PASS |

### 二、业务逻辑验证 (business-logic.sql)

| 查询 | 目的 | 结果摘要 | 状态 |
|---|---|---|---|
| TOP 3 消费用户 | 用户消费排名 | Bob ($207.98) > Eve ($89.99) > Zhang San ($55.97) | PASS |
| 热门商品排行 | 商品销量排名 | Monitor (1) / Backpack (1) / Bike Light (1) ... | PASS |
| 库存预警 | 低库存商品 | Monitor (5) / Chair (10) / Keyboard (15) / Mouse (20) | PASS |
| 订单状态占比 | 各状态比例 | completed: 57.1%, pending: 14.3%, cancelled: 28.6% | PASS |
| 无效用户检测 | 注册>30天无订单 | 3 用户 | PASS |
| 潜在流失用户 | 有购物车无订单 | 持续关注中 | PASS |

### 三、异常数据发现 (anomaly-detection.sql)

| 查询 | 目的 | 结果 |
|---|---|---|
| 重复订单检测 | 同一时刻多订单 | 未发现异常 |
| Postal Code 格式异常 | 非数字格式 | 未发现异常 (空字段已排除) |
| 收货人信息不一致 | 订单姓名 vs 用户姓名 | 全部一致 |
| 高取消率预警 | 取消率 > 50% | 取消率 50%，需关注用户 Bob 的取消行为 |
| 购物车失效商品 | 库存为 0 的商品在购物车 | 未发现 |
| 订单金额偏差 | 明细汇总 vs total_amount | 全部精确匹配 |

## 结论

- 模拟数据库未发现数据完整性违规
- 业务逻辑查询结果符合设计预期
- 发现 1 条需关注的现象：用户 Bob 有 1 笔取消订单（order#6），取消率为 50%，需进一步分析取消原因
- 库存预警建议：Monitor 和 Chair 库存偏低，建议补货
