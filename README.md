# 电商平台 QA 全流程测试

![Python](https://img.shields.io/badge/Python-3.13-blue)
![Selenium](https://img.shields.io/badge/Selenium-4.45-green)
![Pytest](https://img.shields.io/badge/Pytest-9.x-orange)
![Requests](https://img.shields.io/badge/Requests-2.34-purple)
![MySQL](https://img.shields.io/badge/MySQL-8.0-4479A1)
![License](https://img.shields.io/badge/License-MIT-yellow)

基于 SauceDemo 电商平台的端到端软件测试实战项目，覆盖**完整软件测试生命周期（STLC）**。  
目标是展示从需求分析到缺陷闭环的完整质量保障能力。

---

## 项目结构

```
├── 1-manual-testing/        # 测试计划 + 43条手工用例 + 测试总结
├── 2-sql-testing/           # 5表建表 + 18条数据审计查询 + 结果报告
├── 3-api-testing/           # 20条 Pytest+Requests API 自动化用例
├── 4-automation/            # Selenium POM 框架 + 22条 UI 自动化用例
├── 5-bug-reports/           # 3份规范缺陷报告
├── 6-screenshots/           # 测试截图
└── 7-postman/               # Postman API 测试集合（15条用例）
```

## 测试覆盖

| 模块 | 手工用例 | 自动化用例 | 覆盖类型 |
|---|---|---|---|
| 登录 | 11条（含SQL注入/XSS） | 4条参数化 | 正向 + 反向 + 边界值 |
| 商品列表 | 12条 | 8条 | 排序 / 筛选 / 添加移除 |
| 购物车 | 8条 | 4条 | 增删改 / 持久化 / 导航 |
| 结算流程 | 12条 | 6条（含端到端） | 表单校验 / 订单完成 / 登出 |

## 技术栈

- **测试框架**：Pytest 9.x + pytest-html
- **Web 自动化**：Selenium 4.x + Page Object Model
- **API 测试**：Requests + Pytest + Postman
- **数据库**：MySQL 8.0 + mysql-connector-python
- **设计模式**：POM（BasePage + 4个页面对象）

## 快速开始

```bash
pip install -r requirements.txt
```

### 运行自动化测试

```bash
cd 4-automation
pytest --html=reports/report.html --self-contained-html -v
```

### SQL 测试

```bash
mysql -u root -p < 2-sql-testing/schema.sql
mysql -u root -p < 2-sql-testing/seed-data.sql
# 在 MySQL 中逐条执行 queries/ 下的 SQL 文件
```

### API 测试（代码方式）

```bash
cd 3-api-testing
pytest -v
```

### API 测试（Postman 图形化方式）

1. 打开 Postman，导入 `7-postman/reqres-api-tests.json`
2. 运行集合即可看到 15 条用例执行结果

## 项目亮点

 **STLC 全流程闭环**：从测试计划到缺陷报告，五个环节贯通
 **SQL 三层次数据审计**：数据完整性 + 业务逻辑 + 异常发现
 **API + UI 双维度自动化**：35条 API（Pytest 20条 + Postman 15条）+ 22条 UI 自动化用例
 **POM 分层架构**：BasePage → 4个页面对象 → 独立测试层
**参数化测试**：一条用例覆盖多组输入，提高测试效率
**企业级缺陷报告**：含复现步骤、影响范围、修复建议
