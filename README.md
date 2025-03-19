# Carbonis

## 这是一个用于挑战杯项目的代码框架


本模型是一个开源的 LLM 应用开发平台。其直观的界面结合了 AI 工作流、RAG 管道、Agent、模型管理、可观测性功能等，让您可以快速从原型到生产。以下是其核心功能列表：
</br> </br>

**1. 工作流**: 
  在画布上构建和测试功能强大的 AI 工作流程，利用以下所有功能以及更多功能。



**2. 模型支持**: 
  与数百种专有/开源 LLMs 以及数十种推理提供商和自托管解决方案无缝集成，涵盖 GPT、Mistral、Llama3 以及任何与 OpenAI API 兼容的模型。

![providers-v5](图片)


**3. Prompt IDE**: 
  用于制作提示、比较模型性能以及向基于聊天的应用程序添加其他功能（如文本转语音）的直观界面。

**4. RAG Pipeline**: 
  广泛的 RAG 功能，涵盖从文档摄入到检索的所有内容，支持从 PDF、PPT 和其他常见文档格式中提取文本的开箱即用的支持。

**5. Agent 智能体**: 
  您可以基于 LLM 函数调用或 ReAct 定义 Agent，并为 Agent 添加预构建或自定义工具。本模型为 AI Agent 提供了50多种内置工具，如谷歌搜索、DALL·E、Stable Diffusion 和 WolframAlpha 等。

**6. LLMOps**: 
  随时间监视和分析应用程序日志和性能。您可以根据生产数据和标注持续改进提示、数据集和模型。

**7. 后端即服务**: 
  所有 Carbonis 的功能都带有相应的 API，因此您可以轻松地将 Carbonis 集成到自己的业务逻辑中。

### 验证依赖项

本模型依赖以下工具和库：

- [Node.js v18.x (LTS)](http://nodejs.org)
- [pnpm](https://pnpm.io/)
- [Python](https://www.python.org/) version 3.11.x or 3.12.x

### 后端

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

### 前端

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