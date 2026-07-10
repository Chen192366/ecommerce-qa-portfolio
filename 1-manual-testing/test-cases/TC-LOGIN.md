# 测试用例 — 登录模块 (TC-LOGIN)

| 编号 | 模块 | 场景 | 前置条件 | 操作步骤 | 预期结果 | 优先级 |
|---|---|---|---|---|---|---|
| TC-LOGIN-001 | 登录 | 合法用户名+密码 | 在登录页 | 1. 输入 standard_user<br>2. 输入 secret_sauce<br>3. 点击 Login | 跳转至商品列表页 `/inventory.html`，URL 不含 error | P0 |
| TC-LOGIN-002 | 登录 | 错误密码 | 在登录页 | 1. 输入 standard_user<br>2. 输入 wrong_password<br>3. 点击 Login | 停留在登录页，显示红色错误提示 "Username and password do not match" | P0 |
| TC-LOGIN-003 | 登录 | 错误用户名 | 在登录页 | 1. 输入 invalid_user<br>2. 输入 secret_sauce<br>3. 点击 Login | 显示错误提示 "Username and password do not match" | P1 |
| TC-LOGIN-004 | 登录 | 用户名为空 | 在登录页 | 1. 用户名为空<br>2. 输入 secret_sauce<br>3. 点击 Login | 显示错误提示 "Username is required" | P1 |
| TC-LOGIN-005 | 登录 | 密码为空 | 在登录页 | 1. 输入 standard_user<br>2. 密码为空<br>3. 点击 Login | 显示错误提示 "Password is required" | P1 |
| TC-LOGIN-006 | 登录 | 两者均为空 | 在登录页 | 1. 不输入任何内容<br>2. 点击 Login | 显示错误提示 "Username is required" | P2 |
| TC-LOGIN-007 | 登录 | 锁定用户登录 | 在登录页 | 1. 输入 locked_out_user<br>2. 输入 secret_sauce<br>3. 点击 Login | 显示错误提示 "Sorry, this user has been locked out" | P0 |
| TC-LOGIN-008 | 登录 | 用户名大小写敏感 | 在登录页 | 1. 输入 Standard_User(大写S)<br>2. 输入 secret_sauce<br>3. 点击 Login | 显示错误提示 "Username and password do not match" | P2 |
| TC-LOGIN-009 | 登录 | 密码大小写敏感 | 在登录页 | 1. 输入 standard_user<br>2. 输入 Secret_Sauce(大写S)<br>3. 点击 Login | 显示错误提示 "Username and password do not match" | P2 |
| TC-LOGIN-010 | 登录 | SQL注入尝试 | 在登录页 | 1. 输入 ' OR '1'='1<br>2. 输入 ' OR '1'='1<br>3. 点击 Login | 显示错误提示，不能绕过登录 | P2 |
| TC-LOGIN-011 | 登录 | XSS 尝试 | 在登录页 | 1. 输入 `<script>alert(1)</script>`<br>2. 输入任意密码<br>3. 点击 Login | 正常显示错误提示，不执行脚本 | P2 |

## 评审记录

| 版本 | 日期 | 评审人 | 备注 |
|---|---|---|---|
| v1.0 | 2026-07-10 | — | 初始版本 |
