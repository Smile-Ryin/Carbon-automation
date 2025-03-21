# Carbonis

## 这是一个挑战杯项目：Corbonis零碳——基自动化碳报告生成系统

该系统创新性地融合了区块链、LLM、Agent和RAG技术，致力于解决当前碳核算的不精确性、数据隐私保护难题，以及国家在企业碳核算与报告提交方面缺乏统一标准的痛点。通过智能化手段，本项目能够帮助企业高效完成数字化碳管理，优化碳排放数据的存证、核算、审核及报告生成过程，确保数据的真实性、可追溯性和标准化，助力企业高效完成碳管理，为“双碳”目标的实现提供有力技术支撑。以下是其核心功能列表：
</br> </br>

**1. 数据收集**: 
  设置多源接口，允许从服务器传输数据。


**2. 模型支持**: 
  训练并微调DeepSeek-R1-Distill-Qwen-1.5B模型，以进行碳管理和系统调控。


**3. RAG Pipeline**: 
  广泛的 RAG 功能，涵盖从文档摄入到检索的所有内容，支持从 PDF、PPT 和其他常见文档格式中提取文本的开箱即用的支持。

**4. Agent 智能体**: 
  基于 LLM 函数调用或 ReAct 定义 Agent，并为 Agent 添加预构建或自定义工具。本模型为 企业设置了多种 Agent 。

**5. LLMOps**: 
  随时间监视和分析应用程序日志和性能。您可以根据生产数据和标注持续改进提示、数据集和模型。

**6. 后端即服务**: 
  预计 Carbonis 的功能都将带有相应的 API，到时您可以轻松地将 Carbonis 集成到自己的业务逻辑中。

### 验证依赖项

本模型依赖以下工具和库：

- [Node.js v18.x (LTS)](http://nodejs.org)
- [pnpm](https://pnpm.io/)
- [Python](https://www.python.org/) version 3.11.x or 3.12.x

### 后端（未完成）

Carbonis 的后端使用 Python 编写，使用 [Flask](https://flask.palletsprojects.com/en/3.0.x/) 框架。它使用 [SQLAlchemy](https://www.sqlalchemy.org/) 作为 ORM，使用 [Celery](https://docs.celeryq.dev/en/stable/getting-started/introduction.html) 作为任务队列。授权逻辑通过 Flask-login 进行处理。

```
[api/]
├── constants             // 用于整个代码库的常量设置。
├── controllers           // API 路由定义和请求处理逻辑。
├── core                  // 核心应用编排、模型集成和工具。
├── events                // 事件处理和处理。
├── fields                // 用于序列化/封装的字段定义。
├── libs                  // 可重用的库和助手。
├── migrations            // 数据库迁移脚本。
├── models                // 数据库模型和架构定义。
├── services              // 指定业务逻辑。
├── storage               // 私钥存储。
├── tasks                 // 异步任务和后台作业的处理。
└── tests
```

### 前端（部分完成）

该网站使用基于 Typescript 的 [Next.js](https://nextjs.org/) 模板进行引导，并使用 [Tailwind CSS](https://tailwindcss.com/) 进行样式设计。[React-i18next](https://react.i18next.com/) 用于国际化。

```
[web/]
├── app                   // 布局、页面和组件
│   ├── (commonLayout)    // 整个应用通用的布局
│   ├── (shareLayout)     // 在特定会话中共享的布局
│   ├── activate          // 激活页面
│   ├── components        // 页面和布局共享的组件
│   ├── install           // 安装页面
│   ├── signin            // 登录页面
│   └── styles            // 全局共享的样式
├── assets                // 静态资源
├── bin                   // 构建步骤运行的脚本
├── config                // 可调整的设置和选项
├── context               // 应用中不同部分使用的共享上下文
├── dictionaries          // 语言特定的翻译文件
├── docker                // 容器配置
├── hooks                 // 可重用的钩子
├── i18n                  // 国际化配置
├── models                // 描述数据模型和 API 响应的形状
├── public                // 如 favicon 等元资源
├── service               // 定义 API 操作的形状
├── test
├── types                 // 函数参数和返回值的描述
└── utils                 // 共享的实用函数
```