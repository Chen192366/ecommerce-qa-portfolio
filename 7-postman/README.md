# Postman API 测试集合

## 文件说明

| 文件 | 说明 |
|---|---|
| `reqres-api-tests.json` | Postman Collection v2.1，包含 16 条 API 测试用例 |

## 导入步骤

1. 打开 Postman，点击 **Import** → **Upload Files**
2. 选中 `reqres-api-tests.json` 导入
3. 点击 **Runner** → 选择该集合 → **Run**

> 无需导入环境变量，URL 已直接写在请求中。

## 覆盖接口

| 模块 | 接口 | 用例数 |
|---|---|---|
| 用户列表 | GET /users | 1 |
| 单个用户 | GET /users/{id} | 3 |
| 创建用户 | POST /users | 1 |
| 全量更新 | PUT /users/{id} | 1 |
| 部分更新 | PATCH /users/{id} | 1 |
| 删除用户 | DELETE /users/{id} | 1 |
| 参数化 | GET /users/{1-5} | 5 |
| 文章列表 | GET /posts | 1 |
| 单个文章 | GET /posts/{id} | 1 |
| 创建文章 | POST /posts | 1 |

共 **16 条** 测试用例，均基于 **JSONPlaceholder** 公共 REST API。
