---
title: 网络版与纸质版对照
description: 网络版对纸质教材的勘误和编排调整清单
---

# 网络版与纸质版对照

网络版的正文以纸质教材《云计算及应用》（赵宇丹主编，国家开放大学出版社，2026 年 1 月第 1 版）为底本，章节结构、节号和文字保持一致。编写网络版时发现的少量笔误、前后不一致和已经过时的信息，已在网络版正文中直接改正，下表逐条列出，供教师备课和纸质教材重印时参考。

## 勘误（39 处）

| 位置 | 纸质版 | 网络版 | 说明 |
|---|---|---|---|
| [第 1 章案例导入](chapters/01-cloud-basics/index.md) | 员工通过 Shopify 后台 | 员工通过网店管家后台 | 前一句说采用“网店管家云端版”，后一句写成 Shopify 后台，两个产品前后不一致，统一为网店管家 |
| [表 1-6 云计算演进历程中的一些重大事件](chapters/01-cloud-basics/1-2.md) | 2009 年，Rackspace Hosting 和美国国家航空航天局联合推出 OpenStack | 2010 年，Rackspace Hosting 和美国国家航空航天局联合推出 OpenStack | OpenStack 由 Rackspace 与 NASA 于 2010 年 7 月联合发起，2009 年有误 |
| [表 1-6 云计算演进历程中的一些重大事件](chapters/01-cloud-basics/1-2.md) | 2024 年，华为云发布盘古大模型 3.0 | 2023 年，华为云发布盘古大模型 3.0 | 盘古大模型 3.0 于 2023 年 7 月华为开发者大会（Cloud）发布，2024 年发布的是 5.0 版 |
| [2.3.1.2 远程过程调用的调用过程](chapters/02-core-technologies/2-3.md) | 对外暴露的接口 AP，然后 | 对外暴露的接口 API，然后 | 漏字，应为 API（应用程序接口） |
| [2.3.2.2 分布式计算的模式](chapters/02-core-technologies/2-3.md) | 该模型比较适合大规模数据的选代批处理 | 该模型比较适合大规模数据的离线批处理 | “选代”为错字；且 MapReduce 每轮都要读写磁盘，并不擅长迭代计算（这正是 2.3.4 节 Spark 的优势），改为“离线批处理” |
| [2.3.3.2 MapReduce 工作流程](chapters/02-core-technologies/2-3.md) | 输入数据会被分制成多个分片 | 输入数据会被分割成多个分片 | 错字 |
| [第 2 章本章小结](chapters/02-core-technologies/summary.md) | 本节围绕云计算的核心 | 本章围绕云计算的核心 | 这是全章小结，“本节”应为“本章” |
| [第 2 章本章小结](chapters/02-core-technologies/summary.md) | 云安全按等级保护 2.0 标准为基础 | 云安全以等级保护 2.0 标准为基础 | 搭配不当，“按……为基础”改为“以……为基础” |
| [3.3.1.3 API 网关的使用（共 17 处）](chapters/03-platforms-tools/3-3.md) | 路由转发：API 能够将<br>实例时，API 会依据<br>……（同类共 17 处） | 路由转发：API 网关能够将<br>实例时，API 网关会依据<br>……（同类共 17 处） | 本小节讲的是 API 网关这一中间件，转发、负载均衡、限流、鉴权等都是网关的功能；API 本身是接口，不会“转发请求”，漏写“网关”二字会造成概念混淆 |
| [3.4.1.1 小节标题](chapters/03-platforms-tools/3-4.md) | 3.4.1.1 协助工具 | 3.4.1.1 协作工具 | 本小节讲在线文档、会议、即时通信等团队协作类 SaaS，“协助”为笔误 |
| [3.5.2.2 阿里云 CI/CD（共 5 处）](chapters/03-platforms-tools/3-5.md) | 阿里云提供多种 CI/CD 工具和服务，如阿里云 CodePipeline、阿里云容器服务等。<br>①源码管理：集成阿里云 Code 库、GitHub 等版本控制系统。<br>……（同类共 5 处） | 阿里云提供多种 CI/CD 工具和服务，如云效 DevOps 平台（代码管理 Codeup、流水线 Flow）、阿里云容器服务等。<br>①源码管理：集成云效 Codeup 代码库、GitHub 等版本控制系统。<br>……（同类共 5 处） | 阿里云早期的 CodePipeline 服务已由云效取代，现行的 CI/CD 产品是云效流水线 Flow 和代码管理 Codeup；“CodeBuild”是 AWS 的产品名，“阿里云 Code 库”也不是阿里云的产品名称 |
| [第 3 章本章小结](chapters/03-platforms-tools/summary.md) | 典型应用如协助工具 | 典型应用如协作工具 | 同上 |
| [第 3 章本章小结](chapters/03-platforms-tools/summary.md) | 典型服务包括阿里云和云数据库服务等 | 典型服务包括阿里云 ECS 和云数据库服务等 | “阿里云”是云平台名称，不是一种 IaaS 服务，此处指的是云服务器 ECS（见 3.2.1.1 节） |
| [4.1.1.2 配置云服务器](chapters/04-applications/4-1.md) | （1）创建 EC2 实例。 | （1）创建 ECS 实例。 | 本段以阿里云为例，阿里云的云服务器产品叫 ECS（弹性计算服务），EC2 是亚马逊 AWS 的产品名 |
| [4.1.3.3 构建容器镜像，Dockerfile 命令解释](chapters/04-applications/4-1.md) | 复制到容器内容的/app 目录下 | 复制到容器内的 /app 目录下 | “容器内容的”多了一个“容”字 |
| [4.1.1.2 配置云服务器，“说明”中的配置建议](chapters/04-applications/4-1.md) | （1）系统：Ubuntu 20.04 或 CentOS 7。 | （1）系统：Ubuntu 22.04 / 24.04 或 Alibaba Cloud Linux 3。 | CentOS 7 已于 2024 年 6 月停止维护，Ubuntu 20.04 的标准支持也已于 2025 年 5 月结束，云平台新建实例应选仍在维护的版本 |
| [4.2.3.2 教育云建设模式，末段](chapters/04-applications/4-2.md) | 随着技术的不断进步，云计算在教育行业的应用将会更加广泛和深入。如发布课程内容、布置作业、进行在线测验等。例如，某大学通过云计算平台实现了 LMS 的全面应用，教师可以实时跟踪学生的学习进度，及时给予反馈，促进学生的学习效果。 | 随着技术的不断进步，云计算在教育行业的应用将会更加广泛和深入。例如，某大学通过云计算平台实现了 LMS 的全面应用，教师可以在平台上发布课程内容、布置作业、进行在线测验，实时跟踪学生的学习进度，及时给予反馈，提升学生的学习效果。 | “如发布课程内容……”是缺了主语的残句，与后一句合并；“促进学生的学习效果”搭配不当 |
| [4.2.3.3 教育云建设历程](chapters/04-applications/4-2.md) | 在今年年初大模型应用爆发后，学习都在探索 AI+教育的应用 | 在 2023 年年初大模型应用爆发后，学校都在探索 AI+教育的应用 | “今年”在出版后会失去所指，按大模型应用爆发的时间写明 2023 年；“学习”为“学校”之误 |
| [4.2.5.3 工业云的建设架构，设备层和连接层](chapters/04-applications/4-2.md) | 再通过 MOTT、COAP、HTTPS 等协议 | 再通过 MQTT、CoAP、HTTPS 等协议 | 物联网消息协议是 MQTT（Message Queuing Telemetry Transport），受限应用协议写作 CoAP |
| [4.2.5.3 工业云的建设架构，应用层](chapters/04-applications/4-2.md) | 就可以使用云制造服务中心的云服务。生产需求模型，从而指导供应链的管理，协助供应商优化生产计划，实现减少库存，保障供应，提升供应链效率。智慧供应链管理云服务是对 ERP、物联网、人工智能、大数据等技术的综合应用。 | 就可以使用云制造服务中心的云服务。例如，智慧供应链管理云服务可以基于订单和市场数据建立生产需求模型，从而指导供应链的管理，协助供应商优化生产计划，实现减少库存，保障供应，提升供应链效率。智慧供应链管理云服务是对 ERP、物联网、人工智能、大数据等技术的综合应用。 | “生产需求模型，从而指导……”前面缺了主语和谓语，补全为完整的例子 |
| [4.3.1 第 6 点 降低大数据处理的成本](chapters/04-applications/4-3.md) | 计算采用按需付费的模式 | 云计算采用按需付费的模式 | 漏了“云”字 |
| [5.1.1.3 边缘计算的技术方案](chapters/05-trends-careers/5-1.md) | 基于 WinDriver 公司的高扩展 NFV 方案 | 基于 Wind River（风河）公司的高扩展 NFV 方案 | 公司名应为 Wind River（风河） |
| [5.1.3.1 无服务器计算发展历程](chapters/05-trends-careers/5-1.md) | FaaS（Function as a Service，功能即服务） | FaaS（Function as a Service，函数即服务） | FaaS 的通行译名是“函数即服务”，与阿里云“函数计算”、腾讯云“云函数”的叫法一致 |
| [5.1.3.1 无服务器计算发展历程](chapters/05-trends-careers/5-1.md) | 同年，谷歌也发布 Firebase，提供多端一体化开发的 Serverless 解决方案。 | 同年，谷歌也发布 Cloud Functions for Firebase，提供多端一体化开发的 Serverless 解决方案。 | Firebase 平台 2014 年已被谷歌收购，2017 年发布的是其函数服务 Cloud Functions for Firebase |
| [5.1.4.1 大模型的发展历程](chapters/05-trends-careers/5-1.md) | 2023 年，OpenAI 发布 GPT-4，它是首个多模态大模型，支持文本和图像处理 | 2023 年，OpenAI 发布 GPT-4，它是能同时理解文本和图像的多模态大模型 | 在 GPT-4 之前已有 Flamingo、PaLM-E 等多模态模型，“首个”不准确 |
| [5.1.4.1 大模型的发展历程](chapters/05-trends-careers/5-1.md) | DeepSeek 在 2024 年 1 月开源 670 亿参数 DeepSeek LLM | DeepSeek 在 2023 年 11 月开源 670 亿参数 DeepSeek LLM | DeepSeek LLM 67B 于 2023 年 11 月底开源，2024 年 1 月发布的是其技术报告 |
| [5.1.4.2 大模型对云计算的需求](chapters/05-trends-careers/5-1.md) | 依赖云计算的分布式计算集群（如 AWS 的 P3 实例、阿里云的 E-MapReduce） | 依赖云计算的分布式计算集群（如 AWS 的 P3 实例、阿里云的 GPU 云服务器） | E-MapReduce 是阿里云的大数据处理平台（Hadoop/Spark），不是训练大模型用的 GPU 计算集群 |
| [5.1.4.2 自动驾驶案例和 5.1.4.3 云边端协同](chapters/05-trends-careers/5-1.md) | 边缘推理与车云协同：特斯拉利用 AWS EC2 P4 实例训练自动驾驶模型，并通过 Inferentia 芯片在车载终端部署轻量化边缘推理服务，实现实时障碍物识别与决策。<br>典型场景：自动驾驶领域，特斯拉利用 AWS EC2 GPU 实例训练模型，通过 Inferentia 芯片在车载终端部署推理服务，实现实时障碍物识别； | 边缘推理与车云协同：车企利用云上 GPU 实例训练自动驾驶模型，再把压缩后的轻量化模型部署到车载芯片上进行边缘推理，实现实时障碍物识别与决策。<br>典型场景：自动驾驶领域，车企在云端用 GPU 集群训练模型，把推理服务部署到车载芯片上，实现实时障碍物识别； | AWS Inferentia 是部署在亚马逊数据中心的云端推理芯片，不能装在汽车上；特斯拉的车载推理使用自研 FSD 芯片，原文的组合与事实不符，改为一般性描述 |
| [5.1.4.2 自动驾驶案例](chapters/05-trends-careers/5-1.md) | AWS Trainium3 芯片与 Claude 模型训练：Amazon 与 Anthropic 合作的 Rainier 项目，使用数十万 Trainium2 芯片组成的 UltraServer 集群，提供超过当前 5 倍的算力（EP 级），用于训练下一代 Claude 模型，推动自动驾驶算法突破。 | AWS Trainium2 芯片与 Claude 模型训练：Amazon 与 Anthropic 合作的 Rainier 项目，使用数十万 Trainium2 芯片组成的 UltraServer 集群，提供超过当前 5 倍的算力（EP 级），用于训练下一代 Claude 模型。自动驾驶等超大规模训练任务同样依赖这类云上专用芯片集群。 | 标题写 Trainium3，正文写 Trainium2，Rainier 项目使用的是 Trainium2；该项目用于训练 Claude 大模型，与自动驾驶算法无直接关系 |
| [5.1.4.2 大模型与云计算技术应用挑战](chapters/05-trends-careers/5-1.md) | 模型蒸馏（如 LoRA 微调） | 模型蒸馏、参数高效微调（如 LoRA） | LoRA 是参数高效微调方法，不属于模型蒸馏 |
| [5.1.4.3 未来发展趋势](chapters/05-trends-careers/5-1.md) | NVIDIA V100 GPU 通过第三代 Tensor Core 与 NVLink 3.0 技术<br>NVIDIA V100 GPU 通过稀疏计算与混合精度技术 | NVIDIA A100 GPU 通过第三代 Tensor Core 与 NVLink 3.0 技术<br>NVIDIA A100 GPU 通过稀疏计算与混合精度技术 | 第三代 Tensor Core、NVLink 3.0 和结构化稀疏加速都是 A100 的特性，V100 是第一代 Tensor Core、NVLink 2.0 |
| [5.1.4.3 未来发展趋势](chapters/05-trends-careers/5-1.md) | 工业场景中，H800 芯片通过异构计算架构在边缘节点完成焊接图像缺陷检测<br>H800 芯片通过动态资源调度与硬件级安全隔离 | 工业场景中，边缘 AI 推理芯片通过异构计算架构在边缘节点完成焊接图像缺陷检测<br>边缘 AI 推理芯片通过动态资源调度与硬件级安全隔离 | H800 是功耗数百瓦的数据中心训练 GPU，不是部署在产线边缘节点的芯片 |
| [5.1.4.3 多云与混合云架构](chapters/05-trends-careers/5-1.md) | 华为 DaoCloud 解决方案 | DaoCloud（道客）的多云解决方案 | DaoCloud（上海道客网络科技）是独立的云原生企业，不属于华为 |
| [5.1.4.3 绿色计算](chapters/05-trends-careers/5-1.md) | 微软通过液冷技术与可再生能源降低数据中心 PUE 至 1.0 以下 | 微软通过液冷技术与可再生能源把数据中心 PUE 降到 1.1 左右 | PUE 是数据中心总能耗与 IT 设备能耗之比，最小只能接近 1.0，不可能低于 1.0 |
| [5.1.4.3 行业深度渗透](chapters/05-trends-careers/5-1.md) | 显著提升研究员信息处理效率———此信息源自招商银行 2023 年金融科技发布会及《中国银行业》期刊报道。 | 显著提升研究员信息处理效率（据招商银行 2023 年金融科技发布会及《中国银行业》期刊报道）。 | 来源说明改为括注，并去掉多余的破折号 |
| [5.2.2.2 云计算相关认证](chapters/05-trends-careers/5-2.md) | 阿里云 ACP（Alibaba Cloud Certified Professional）覆盖云计算、大数据、安全等领域，适合初、中级从业者，国内企业认可度高。 | 阿里云 ACP（Alibaba Cloud Certified Professional）覆盖云计算、大数据、安全等领域，是专业级认证，适合有一定基础的从业者，国内企业认可度高；零基础学习者可先考入门级的 ACA（Alibaba Cloud Certified Associate）。 | 阿里云认证分 ACA（助理/入门级）、ACP（专业级）、ACE（专家级），ACP 不是初级认证 |
| [5.2.1.1 云架构师 权威认证体系](chapters/05-trends-careers/5-2.md) | 基础认证包括 AWS Certified Solutions Architect-Associate、Microsoft Certified: Azure Solutions Architect Expert。<br>进阶认证包括 Google Cloud Professional Cloud Architect、信息系统安全专家认证。 | 基础认证包括 AWS Certified Solutions Architect-Associate、Microsoft Certified: Azure Administrator Associate。<br>进阶认证包括 Microsoft Certified: Azure Solutions Architect Expert、Google Cloud Professional Cloud Architect、信息系统安全专家认证（CISSP）。 | Azure Solutions Architect Expert 是微软的专家级认证，不宜列为基础认证；基础层改为助理级的 Azure Administrator Associate（即表 5-5 中的 AZ-104） |
| [5.2.2.2 AWS 认证](chapters/05-trends-careers/5-2.md) | 专家级：AWS Certified DevOps Engineer-Professional（自动化与运维）。 | 专业级：AWS Certified DevOps Engineer-Professional（自动化与运维）。 | AWS 认证分基础级、助理级、专业级（Professional）和专项级，Professional 中文译为“专业级” |
| [表 5-5 其他云计算认证推荐](chapters/05-trends-careers/5-2.md) | Google Cloud ACE，大数据/AI 领域 | Google Cloud ACE，谷歌云平台部署与运维岗 | ACE 是 Associate Cloud Engineer（助理云工程师），考查云上部署和运维，并非大数据/AI 方向的认证 |

## 编排上的调整

以下调整只改变呈现方式，不改变内容：

1. **代码截图转为代码块**：纸质教材 4.1.3.3 节的 8 张命令和 Dockerfile 截图，网络版转录为可以复制的代码块，并给命令解释加上代码格式。
2. **排版断行修复**：PDF 排版中被图片隔断的句子（如 2.1.1、4.2.1.3）已接续完整，图片放回首次引用它的段落之后；文件名和网址中被拆开的“.”和空格（如 `requirements. txt`）已复原。
3. **标题层级**：4.2.4.3.1～4.2.4.3.5 和 4.3.1、4.3.3 下的小标题，按所属小节调整了层级，便于网页目录显示；节号和标题文字不变。
4. **产品名写法**：KubeEdge、OpenEdge、K3s、CodePipeline、GuardDuty、QuickSight、HAProxy、GitLab CI、Alertmanager 等产品名按官方写法去掉了多余空格。
5. **拓展阅读折叠**：2.4.1.3、2.5.4～2.5.7、2.6.3 等较深的内容在网页上默认折叠为“拓展阅读”，点击即可展开原文全文。
6. **练习题**：按任课教师意见，网络版不使用纸质教材的“思考与练习”，各节随堂小测和各章课后练习根据正文重新编写，并附答案与解析。
7. **二维码资源**：纸质教材中的微课二维码在网页上显示为“配套微课”占位，视频上线后补充链接。
