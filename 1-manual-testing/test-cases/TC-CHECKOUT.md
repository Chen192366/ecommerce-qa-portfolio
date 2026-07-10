# 测试用例 — 结算流程模块 (TC-CHECKOUT)

| 编号 | 模块 | 场景 | 前置条件 | 操作步骤 | 预期结果 | 优先级 |
|---|---|---|---|---|---|---|
| TC-CHK-001 | 结算 | 信息填写页加载 | 购物车有商品且已点击 Checkout | 1. 进入结算信息页 | 显示 First Name / Last Name / Postal Code 三个输入框 + Cancel / Continue 按钮 | P0 |
| TC-CHK-002 | 结算 | 合法信息提交 | 在结算信息页 | 1. 输入 First Name: "Zhang"<br>2. Last Name: "San"<br>3. Postal Code: "100000"<br>4. 点击 Continue | 跳转至订单确认页 `/checkout-step-two.html` | P0 |
| TC-CHK-003 | 结算 | First Name 为空 | 在结算信息页 | 1. First Name 留空<br>2. 其他填写完整<br>3. 点击 Continue | 显示错误提示 "First Name is required" | P0 |
| TC-CHK-004 | 结算 | Last Name 为空 | 在结算信息页 | 1. Last Name 留空<br>2. 其他填写完整<br>3. 点击 Continue | 显示错误提示 "Last Name is required" | P0 |
| TC-CHK-005 | 结算 | Postal Code 为空 | 在结算信息页 | 1. Postal Code 留空<br>2. 其他填写完整<br>3. 点击 Continue | 显示错误提示 "Postal Code is required" | P0 |
| TC-CHK-006 | 结算 | 全部为空 | 在结算信息页 | 1. 不填任何信息<br>2. 点击 Continue | 显示错误提示 "First Name is required" | P1 |
| TC-CHK-007 | 结算 | Cancel 取消 | 在结算信息页 | 1. 点击 Cancel | 返回购物车页 | P1 |
| TC-CHK-008 | 结算 | 订单确认页 | 已填写合法信息并提交 | 1. 查看确认页 | 显示商品清单、总金额（不含税+税后）、支付信息（SauceCard）、Finish 按钮 | P0 |
| TC-CHK-009 | 结算 | Finish 完成订单 | 在订单确认页 | 1. 点击 Finish | 跳转至完成页 `/checkout-complete.html`，显示 "Thank you for your order!" | P0 |
| TC-CHK-010 | 结算 | 完成页返回首页 | 在完成页 | 1. 点击 "Back Home" | 返回商品列表页 `/inventory.html` | P1 |
| TC-CHK-011 | 结算 | 重复提交订单 | 刚完成一笔订单 | 1. 重新加入商品<br>2. 走完整结算流程 | 能正常生成新订单（无订单号冲突） | P2 |
| TC-CHK-012 | 结算 | 特殊字符信息 | 在结算信息页 | 1. First Name: "A!@#$%"<br>2. Last Name: "B^&*()"<br>3. Postal Code: "abc-123"<br>4. 点击 Continue | 正常通过（SauceDemo 不校验格式） | P2 |

## 评审记录

| 版本 | 日期 | 评审人 | 备注 |
|---|---|---|---|
| v1.0 | 2026-07-10 | — | 初始版本 |
