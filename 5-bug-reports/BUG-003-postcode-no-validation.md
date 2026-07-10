# BUG-003 — Postal Code 字段未做格式校验

## 基本信息

| 字段 | 值 |
|---|---|
| Bug ID | BUG-003 |
| 模块 | 结算流程 (Checkout) |
| 严重等级 | Minor |
| 优先级 | P2 |
| 状态 | Open |
| 报告日期 | 2026-07-10 |
| 报告人 | Chen192366 |
| 环境 | Windows 11 / Chrome 最新版 / SauceDemo |

## 复现步骤

1. 使用 standard_user 登录
2. 添加 1 件商品到购物车，点击 Checkout
3. 在结算信息页执行以下测试：

| 测试输入 | 步骤 |
|---|---|
| Postal Code: "abc-def" | 填写并点 Continue → 通过 |
| Postal Code: "!@#$%^" | 填写并点 Continue → 通过 |
| Postal Code: "abcdefgh" | 填写并点 Continue → 通过 |
| Postal Code: "12345" | 填写并点 Continue → 通过 |

## 预期结果

Postal Code 字段应校验输入格式（如仅允许数字、限制长度 5-10 位），对非法格式给出提示。

## 实际结果

Postal Code 字段接受任何字符输入（字母、特殊符号、混合），无格式校验。

## 截图

> 参见 `../6-screenshots/BUG-003-postcode-validation.png`

## 影响范围

- 用户可能提交格式错误的邮政编码，导致物流配送地址无效
- 数据库可能存入脏数据，后续数据分析时产生偏差

## 建议修复

在 Postal Code 输入框增加前端 + 后端双重校验：
- 前端：正则表达式限制输入字符类型和长度
- 后端：在 API 层再次验证，返回明确的错误信息

推荐正则（中国邮政编码）：`^\d{6}$`
推荐正则（美国邮政编码）：`^\d{5}(-\d{4})?$`
