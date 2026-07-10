# API 测试报告

## 测试目标

| 项目 | 值 |
|---|---|
| 被测 API | Reqres.in (REST API 公共测试服务) |
| 测试框架 | Pytest + Requests |
| 测试日期 | 2026-07-10 |

## 测试接口覆盖

| 接口 | 方法 | 路径 | 测试用例数 |
|---|---|---|---|
| 登录 | POST | /api/login | 4 |
| 注册 | POST | /api/register | 2 |
| 查询用户列表 | GET | /api/users?page=1 | 2 |
| 查询单个用户 | GET | /api/users/{id} | 2 (+ 6 参数化) |
| 创建用户 | POST | /api/users | 1 |
| 更新用户(全量) | PUT | /api/users/{id} | 1 |
| 更新用户(部分) | PATCH | /api/users/{id} | 1 |
| 删除用户 | DELETE | /api/users/{id} | 1 |

## 执行结果

| 指标 | 数值 |
|---|---|
| 总用例数 | 20 |
| 通过 | 20 |
| 失败 | 0 |
| 通过率 | 100% |
| 平均响应时间 | < 2s |

## 测试结论

- 所有 CRUD 接口 (GET/POST/PUT/PATCH/DELETE) 均返回预期状态码和响应体
- 登录/注册模块的错误处理（缺少字段、用户不存在）返回正确的 400 错误
- 参数化测试覆盖 6 个有效用户 ID，均返回 200
- API 响应时间均在可接受范围内 (< 5s)
