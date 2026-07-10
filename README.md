# E-Commerce QA Portfolio

端到端软件测试项目，覆盖完整软件测试生命周期（STLC），针对 SauceDemo 电商平台执行手动测试、SQL 数据验证、API 接口测试及 Selenium Web 自动化测试。

## 测试对象

[SauceDemo](https://www.saucedemo.com/) — 国际 QA 测试标准练习站点，包含登录、商品浏览、购物车、结算等完整电商流程。

## 技术栈

| 层 | 工具 |
|---|---|
| 语言 | Python 3.13 |
| Web 自动化 | Selenium 4.x + Page Object Model |
| 测试框架 | Pytest |
| API 测试 | Requests |
| 数据库 | MySQL 8.0 |
| 报告 | pytest-html |

## 项目结构

```
├── README.md
├── requirements.txt
├── 1-manual-testing/          # 测试计划 + 用例 + 总结
├── 2-sql-testing/             # 建表/数据/SQL查询/结果报告
├── 3-api-testing/             # API 接口自动化测试
├── 4-automation/              # Selenium POM Web 自动化
│   ├── pages/                 # Page Object 页面类
│   ├── tests/                 # 自动化测试用例
│   └── reports/               # HTML 测试报告
├── 5-bug-reports/             # 缺陷报告
└── 6-screenshots/             # 测试截图证据
```

## 快速开始

```bash
pip install -r requirements.txt
```

### 运行 SQL 测试

```bash
mysql -u root -p < 2-sql-testing/schema.sql
mysql -u root -p < 2-sql-testing/seed-data.sql
# 然后在 MySQL 中逐个执行 queries/ 下的 SQL 文件
```

### 运行自动化测试

```bash
cd 4-automation
pytest --html=reports/report.html --self-contained-html
```

### 运行 API 测试

```bash
cd 3-api-testing
pytest -v
```
