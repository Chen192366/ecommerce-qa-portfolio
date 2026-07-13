# Postman API 测试集合

## 文件说明

| 文件 | 说明 |
|---|---|
| `reqres-api-tests.json` | Postman Collection v2.1，包含 20 条 API 测试用例 |
| `reqres-env.json` | 环境变量配置（base_url） |

## 导入步骤

1. 打开 Postman，点击 **Import** → **Upload Files**
2. 选中 `reqres-api-tests.json` 和 `reqres-env.json` 同时导入
3. 右上角环境切换为 **Reqres 测试环境**
4. 点击 **Runner** → 选择该集合 → **Run**

## 覆盖接口

| 模块 | 接口 | 用例数 | 状态码断言 |
|---|---|---|---|
| Auth | POST /api/login | 4 | 200, 400 |
| Auth | POST /api/register | 2 | 200, 400 |
| Users | GET /api/users | 2 | 200 |
| Users | GET /api/users/{id} | 4 | 200, 404 |
| Users | POST /api/users | 1 | 201 |
| Users | PUT /api/users/{id} | 1 | 200 |
| Users | PATCH /api/users/{id} | 1 | 200 |
| Users | DELETE /api/users/{id} | 1 | 204 |
| 参数化 | GET /api/users/{1-6} | 6 | 200 |

共 **20 条** 测试用例，每条均包含 `pm.response` 断言脚本，执行结果一目了然。
