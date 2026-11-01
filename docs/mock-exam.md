---
title: 期末模拟卷
description: 按期末闭卷考试的题型和分值，从各章课后练习中组成的两套模拟卷，可以直接作答并查看解析
---

# 期末模拟卷

本课程期末为闭卷考试，重点考查基本概念、云服务的用途和简单的应用分析。下面两套模拟卷按期末考试的题型和分值，从各章课后练习中抽题组成，覆盖全书 5 章，两套卷子的题目互不重复：

| 题型 | 题数 | 每题分值 | 合计 |
|---|---|---|---|
| 单项选择题 | 20 | 2 | 40 |
| 多项选择题 | 5 | 4 | 20 |
| 判断题 | 10 | 1 | 10 |
| 简答题 | 3 | 10 | 30 |

建议合上书本、限时 90 分钟，先独立做完一整套，再展开“答案与解析”核对。简答题按参考答案的要点自评。选择题和判断题可以直接点击作答；每道题解析下方的“回看”链接可以跳回对应章节复习。

## 模拟卷一

**一、单项选择题**（每题 2 分）

<div class="quiz" data-answer="A" markdown>

**1.** 按照 NIST 的定义，下面哪一项**不是**云计算的基本特点？（　　）

- A. 用户必须自己采购服务器硬件
- B. 按需自助服务
- C. 资源池化
- D. 服务可被测量

</div>

??? tip "答案与解析"
    **答案：A**

    解析：云计算的意义正是让用户不必自己采购硬件，而是通过网络从资源池中按需取用。B、C、D 都是 NIST 定义的基本特点。

    考查：云计算的特点 · 认知层次：记忆 · [回看 1.1.1](chapters/01-cloud-basics/1-1.md#111)
    { .quiz-meta }

<div class="quiz" data-answer="B" markdown>

**2.** 分布式计算中，负责把一个大任务拆分、分配给各个计算节点，并跟踪执行进度的是（　　）。

- A. 数据存储体系
- B. 任务调度引擎
- C. 监控体系
- D. 安全控制体系

</div>

??? tip "答案与解析"
    **答案：B**

    解析：任务调度引擎决定“哪个任务交给哪个节点做”。数据存储体系管数据放在哪里；监控体系负责观察运行状态；安全控制体系负责身份认证和访问控制。

    考查：分布式计算的组成 · 认知层次：理解 · [回看 1.1.2](chapters/01-cloud-basics/1-1.md#1122)
    { .quiz-meta }

<div class="quiz" data-answer="A" markdown>

**3.** 使用 SaaS 时，下列哪一项仍然主要由**用户自己**负责？（　　）

- A. 账号权限和自己录入的业务数据
- B. 服务器硬件维护
- C. 操作系统打补丁
- D. 应用软件版本升级

</div>

??? tip "答案与解析"
    **答案：A**

    解析：SaaS 中硬件、操作系统、应用软件都由云服务商管理，但谁能登录、数据录得对不对、密码有没有泄露，仍然是用户的责任。这就是“安全责任共担”。

    考查：SaaS 服务安全责任 · 认知层次：理解 · [回看 1.1.3](chapters/01-cloud-basics/1-1.md#1133)
    { .quiz-meta }

<div class="quiz" data-answer="C" markdown>

**4.** 云服务提供商把云平台部署到用户自己的机房里，由提供商负责运维，让用户在本地享受类似公有云的弹性服务。这种模式叫（　　）。

- A. 托管云
- B. 互联云
- C. 驻地云
- D. 社区云

</div>

??? tip "答案与解析"
    **答案：C**

    解析：驻地云的关键词是“部署在用户机房、本地化”。托管云是在提供商那里为一个用户单独划出的环境；互联云是把多个独立的云环境连起来。

    考查：其他部署模式 · 认知层次：理解 · [回看 1.1.4](chapters/01-cloud-basics/1-1.md#1145)
    { .quiz-meta }

<div class="quiz" data-answer="B" markdown>

**5.** 在个人电脑的 Windows 上安装 VMware Workstation，再在里面运行 Linux 虚拟机，VMware Workstation 属于（　　）。

- A. 原生型 Hypervisor
- B. 宿主型 Hypervisor
- C. 容器引擎
- D. 分布式文件系统

</div>

??? tip "答案与解析"
    **答案：B**

    解析：宿主型 Hypervisor 运行在已有的操作系统（这里是 Windows）之上；原生型直接装在硬件上，如 ESXi。

    考查：Hypervisor 的类型 · 认知层次：应用 · [回看 2.1.1](chapters/02-core-technologies/2-1.md#2111)
    { .quiz-meta }

<div class="quiz" data-answer="D" markdown>

**6.** 在 Docker 中，用来“打包好的、只读的应用模板”，可以据此创建多个容器的是（　　）。

- A. 仓库
- B. 数据卷
- C. 端口映射
- D. 镜像

</div>

??? tip "答案与解析"
    **答案：D**

    解析：镜像是只读模板，容器是镜像运行起来的实例，仓库是存放镜像的地方（如 Docker Hub）。实验 2-2 中用同一个 nginx 镜像创建了两个容器。

    考查：Docker 主要部件 · 认知层次：理解 · [回看 2.1.2](chapters/02-core-technologies/2-1.md#2122)
    { .quiz-meta }

<div class="quiz" data-answer="B" markdown>

**7.** 为云服务器挂载一块“云硬盘”，在操作系统里分区、格式化后安装数据库。云硬盘属于（　　）。

- A. 对象存储
- B. 块存储
- C. 文件存储
- D. 键值存储

</div>

??? tip "答案与解析"
    **答案：B**

    解析：块存储提供的裸块设备对操作系统来说就像本地硬盘，可以直接分区、格式化，时延低，适合数据库和虚拟机磁盘。

    考查：块存储 · 认知层次：应用 · [回看 2.2.2](chapters/02-core-technologies/2-2.md#2223)
    { .quiz-meta }

<div class="quiz" data-answer="D" markdown>

**8.** 下列 IPC 机制中，速度最快、允许多个进程直接访问同一块内存的是（　　）。

- A. 管道
- B. 消息队列
- C. 套接字
- D. 共享内存

</div>

??? tip "答案与解析"
    **答案：D**

    解析：共享内存把同一块物理内存映射到多个进程的地址空间，数据不用来回复制，是所有 IPC 机制中最快的，但需要配合信号量等做同步。

    考查：进程间通信 · 认知层次：记忆 · [回看 2.3.1](chapters/02-core-technologies/2-3.md#2312)
    { .quiz-meta }

<div class="quiz" data-answer="C" markdown>

**9.** 新华三的私有云产品中，负责云资源管理和分配、提供自服务门户的是（　　）。

- A. CVK
- B. CVM
- C. CIC
- D. CMP

</div>

??? tip "答案与解析"
    **答案：C**

    解析：H3C 云的技术架构中，CVK 是虚拟化内核平台，CVM 是虚拟化管理系统，CIC（云业务管理中心）负责云资源的管理和分配，提供自服务门户和运营管理功能。

    考查：私有云平台 · 认知层次：记忆 · [回看 3.1.1](chapters/03-platforms-tools/3-1.md#3112)
    { .quiz-meta }

<div class="quiz" data-answer="B" markdown>

**10.** 登录 Linux 云服务器最常用的方式是（　　）。

- A. 远程桌面（RDP）
- B. SSH
- C. FTP
- D. 电子邮件

</div>

??? tip "答案与解析"
    **答案：B**

    解析：Linux 实例通常用 SSH 工具（如 PuTTY、终端）通过公网 IP 和密码或密钥登录；Windows 实例用远程桌面。

    考查：登录云服务器 · 认知层次：记忆 · [回看 3.2.1](chapters/03-platforms-tools/3-2.md#3211)
    { .quiz-meta }

<div class="quiz" data-answer="C" markdown>

**11.** 消息队列在“生产者产生消息太快、消费者来不及处理”时，起到的主要作用是（　　）。

- A. 加密
- B. 负载均衡
- C. 缓冲
- D. 存储备份

</div>

??? tip "答案与解析"
    **答案：C**

    解析：即使暂时没有读取操作，新消息仍可放入队列，消息队列发挥了缓冲区的作用，让生产和消费解耦。

    考查：消息队列使用 · 认知层次：理解 · [回看 3.3.1](chapters/03-platforms-tools/3-3.md#3312)
    { .quiz-meta }

<div class="quiz" data-answer="B" markdown>

**12.** 字节跳动推出的、具备即时通信、智能日历、云文档等功能的一站式协作平台是（　　）。

- A. 钉钉
- B. 飞书
- C. 企业微信
- D. Jira

</div>

??? tip "答案与解析"
    **答案：B**

    解析：钉钉属于阿里巴巴，企业微信属于腾讯，Jira 是项目管理工具。

    考查：常见的 SaaS 应用 · 认知层次：记忆 · [回看 3.4.1](chapters/03-platforms-tools/3-4.md#3411)
    { .quiz-meta }

<div class="quiz" data-answer="B" markdown>

**13.** 搭建网站时，用来存放图片、视频等静态文件，并可以设置为“公共读”的云服务是（　　）。

- A. 云服务器 ECS
- B. 对象存储 OSS
- C. 云数据库 RDS
- D. 安全组

</div>

??? tip "答案与解析"
    **答案：B**

    解析：对象存储的基本容器是存储桶（Bucket），适合存放网站的静态文件；设为公共读后浏览器可以直接访问。

    考查：搭建网站：配置云存储 · 认知层次：记忆 · [回看 4.1.1.3](chapters/04-applications/4-1.md#4113)
    { .quiz-meta }

<div class="quiz" data-answer="C" markdown>

**14.** 为网站配置 SSL 证书的主要目的是（　　）。

- A. 让网站访问速度更快
- B. 让网站可以通过域名访问
- C. 加密浏览器与服务器之间传输的数据，提高安全性
- D. 自动备份网站数据

</div>

??? tip "答案与解析"
    **答案：C**

    解析：SSL 证书用于 HTTPS 加密传输，防止数据被窃听和篡改；通过域名访问靠的是域名解析。

    考查：域名绑定和 SSL 证书配置 · 认知层次：理解 · [回看 4.1.1.7](chapters/04-applications/4-1.md#4117)
    { .quiz-meta }

<div class="quiz" data-answer="B" markdown>

**15.** 大型企业需要高可用、可扩展、自动故障恢复的容器编排平台，教材首推的是（　　）。

- A. 只用单机 Docker
- B. Kubernetes
- C. Docker Swarm
- D. 虚拟机

</div>

??? tip "答案与解析"
    **答案：B**

    解析：Kubernetes 支持自动化部署、扩展和故障恢复，适合大规模生产环境；Docker Swarm 适合中小规模、对编排要求不高的场景。

    考查：选择合适的容器化平台 · 认知层次：理解 · [回看 4.1.3.1](chapters/04-applications/4-1.md#4131)
    { .quiz-meta }

<div class="quiz" data-answer="A" markdown>

**16.** “核心数据部署在私有云，公共服务使用公有云弹性扩展”，这是政务云的（　　）。

- A. 混合云模式
- B. 集中统建型
- C. 购买服务型
- D. 社区云模式

</div>

??? tip "答案与解析"
    **答案：A**

    解析：教材的小贴士以国家政务服务平台为例：核心数据在私有云，健康码等公共服务在公有云快速扩容。

    考查：政务云建设模式 · 认知层次：理解 · [回看 4.2.1.2](chapters/04-applications/4-2.md#4212)
    { .quiz-meta }

<div class="quiz" data-answer="A" markdown>

**17.** 在靠近物或数据源头的一侧，就近提供计算、存储等服务的计算模式是（　　）。

- A. 边缘计算
- B. 网格计算
- C. 集中式计算
- D. 批处理计算

</div>

??? tip "答案与解析"
    **答案：A**

    解析：教材在 5G 车联网部分给出了边缘计算的定义：在靠近物或数据源头的一侧，采用集网络、计算、存储、应用核心能力于一体的开放平台，就近提供最近端服务。

    考查：边缘计算的概念 · 认知层次：记忆 · [回看 5.1.1.2](chapters/05-trends-careers/5-1.md#5112)
    { .quiz-meta }

<div class="quiz" data-answer="D" markdown>

**18.** 华为开源、支持把容器化业务逻辑下发到边缘部署的边缘计算项目是（　　）。

- A. Link Edge
- B. OpenEdge
- C. Lambda
- D. KubeEdge

</div>

??? tip "答案与解析"
    **答案：D**

    解析：KubeEdge 由华为开源，基于 Kubernetes，把容器化应用下发到边缘；OpenEdge 是百度开源的，提供本地函数式引擎；Link Edge 是阿里云的产品，未开源。

    考查：云服务商边缘计算产品 · 认知层次：记忆 · [回看 5.1.1.3](chapters/05-trends-careers/5-1.md#5113)
    { .quiz-meta }

<div class="quiz" data-answer="A" markdown>

**19.** 函数一段时间没有被调用，再次调用时需要重新创建运行环境，响应变慢，这种现象称为（　　）。

- A. 冷启动
- B. 热迁移
- C. 负载均衡
- D. 弹性伸缩

</div>

??? tip "答案与解析"
    **答案：A**

    解析：冷启动是 Serverless 的主要挑战之一，实验 5-1 的第 5 步就是观察冷启动。

    考查：Serverless 的挑战 · 认知层次：理解 · [回看 5.1.3.3](chapters/05-trends-careers/5-1.md#5133)
    { .quiz-meta }

<div class="quiz" data-answer="B" markdown>

**20.** 通过 Prometheus、Grafana 构建监控体系，确保满足服务等级协议要求，这主要是（　　）的工作。

- A. 售后工程师
- B. 云运维工程师
- C. 前端设计师
- D. 财务人员

</div>

??? tip "答案与解析"
    **答案：B**

    解析：云环境运维监控是云运维工程师的第一项核心职责。

    考查：云运维工程师 · 认知层次：理解 · [回看 5.2.1.2](chapters/05-trends-careers/5-2.md#5212)
    { .quiz-meta }

**二、多项选择题**（每题 4 分）

<div class="quiz quiz-multi" data-answer="ABC" markdown>

**1.** 下列属于云计算服务模式的有（　　）。

- A. IaaS
- B. PaaS
- C. SaaS
- D. 混合云

</div>

??? tip "答案与解析"
    **答案：ABC**

    解析：IaaS、PaaS、SaaS 是三种基本服务模式。混合云是部署模式，回答的是“云在哪里、归谁”，不是“提供什么服务”。

    考查：服务模式与部署模式的区别 · 认知层次：记忆 · [回看 1.1.3](chapters/01-cloud-basics/1-1.md#113)
    { .quiz-meta }

<div class="quiz quiz-multi" data-answer="ABD" markdown>

**2.** 与虚拟机相比，容器的特点有（　　）。

- A. 启动速度快，通常是秒级或更快
- B. 占用资源少
- C. 每个容器都运行一个完整的独立操作系统内核
- D. 镜像体积小，便于分发和部署

</div>

??? tip "答案与解析"
    **答案：ABD**

    解析：容器共享宿主机内核，不运行独立的内核，所以 C 错。实验 2-2 中 nginx 镜像压缩后仅约 22 MB，容器启动不到 0.5 秒。

    考查：虚拟机与容器的对比 · 认知层次：理解 · [回看 2.1.2](chapters/02-core-technologies/2-1.md#212)
    { .quiz-meta }

<div class="quiz quiz-multi" data-answer="ABCD" markdown>

**3.** 降低云服务成本的有效做法有（　　）。

- A. 定期清理闲置的云服务器和云硬盘
- B. 对稳定业务购买预留实例
- C. 利用自动扩展，低谷期减少实例
- D. 把很少访问的数据转到归档存储

</div>

??? tip "答案与解析"
    **答案：ABCD**

    解析：四项都是 3.1.3.2 节介绍的成本优化方法：资源管理与调整、合理利用折扣、提高资源利用率、优化存储策略。

    考查：云服务的成本优化 · 认知层次：应用 · [回看 3.1.3](chapters/03-platforms-tools/3-1.md#3132)
    { .quiz-meta }

<div class="quiz quiz-multi" data-answer="ABD" markdown>

**4.** 下列属于 4.1.1 节“搭建一个简单的网站”步骤的有（　　）。

- A. 选择云服务提供商
- B. 配置云服务器
- C. 训练大模型
- D. 域名绑定和 SSL 证书配置

</div>

??? tip "答案与解析"
    **答案：ABD**

    解析：网站搭建的关键步骤是：选择云服务提供商、配置云服务器、配置云存储、设置云数据库、开发网站代码、部署网站到云服务器、域名绑定和 SSL 证书配置。

    考查：搭建网站的步骤 · 认知层次：记忆 · [回看 4.1.1](chapters/04-applications/4-1.md#411)
    { .quiz-meta }

<div class="quiz quiz-multi" data-answer="ABD" markdown>

**5.** Serverless 的技术优势包括（　　）。

- A. 无须管理服务器
- B. 弹性伸缩
- C. 函数可以永久保持运行状态，不会冷启动
- D. 按需计费

</div>

??? tip "答案与解析"
    **答案：ABD**

    解析：教材列出的四项优势是：无须管理服务器、弹性伸缩、按需计费、快速开发与部署。冷启动恰恰是 Serverless 面临的挑战。

    考查：Serverless 技术优势 · 认知层次：记忆 · [回看 5.1.3.2](chapters/05-trends-careers/5-1.md#5132)
    { .quiz-meta }

**三、判断题**（每题 1 分）

<div class="quiz quiz-judge" data-answer="×" markdown>

**1.** 使用了云计算，用户就完全不用操心安全问题，一切由云服务商负责。（　　）

- √
- ×

</div>

??? tip "答案与解析"
    **答案：×**

    解析：云计算实行安全责任共担。服务商负责它管理的那几层，用户仍要负责自己的账号、数据，以及 IaaS 中的操作系统和应用。

    考查：服务安全责任 · 认知层次：理解 · [回看 1.1.3](chapters/01-cloud-basics/1-1.md#1131)
    { .quiz-meta }

<div class="quiz quiz-judge" data-answer="×" markdown>

**2.** 云计算的资源在哪个城市、哪个机房，用户在使用时必须精确知道。（　　）

- √
- ×

</div>

??? tip "答案与解析"
    **答案：×**

    解析：资源池具有位置无关性，用户一般不需要知道资源具体在哪台机器上，最多选择“地域”和“可用区”这样的大致范围。

    考查：云计算的特点 · 认知层次：理解 · [回看 1.1.1](chapters/01-cloud-basics/1-1.md#1112)
    { .quiz-meta }

<div class="quiz quiz-judge" data-answer="√" markdown>

**3.** KVM 是 Linux 内核中的虚拟化模块，借助 CPU 的硬件虚拟化功能运行虚拟机。（　　）

- √
- ×

</div>

??? tip "答案与解析"
    **答案：√**

    解析：KVM（基于内核的虚拟机）集成在 Linux 内核中，需要 CPU 支持 Intel VT 或 AMD-V 等硬件虚拟化技术，常与 QEMU 配合使用。

    考查：KVM · 认知层次：记忆 · [回看 2.1.2](chapters/02-core-technologies/2-1.md#2123)
    { .quiz-meta }

<div class="quiz quiz-judge" data-answer="√" markdown>

**4.** 在 MapReduce 中，同一个键的所有中间结果一定会被交给同一个 Reduce 任务处理。（　　）

- √
- ×

</div>

??? tip "答案与解析"
    **答案：√**

    解析：这是 Shuffle 阶段的保证，否则同一个词的计数会被分散在不同 Reduce 中，结果就不对了。

    考查：MapReduce 工作流程 · 认知层次：理解 · [回看 2.3.3](chapters/02-core-technologies/2-3.md#2332)
    { .quiz-meta }

<div class="quiz quiz-judge" data-answer="√" markdown>

**5.** 云平台的主账号权限很大，日常工作应为团队成员创建子账号，并按需授予最小权限。（　　）

- √
- ×

</div>

??? tip "答案与解析"
    **答案：√**

    解析：阿里云的 RAM 访问控制、华为云的 IAM、AWS 的 IAM 都支持创建子用户并授权，避免多人共用主账号带来的风险。

    考查：云服务的账户管理 · 认知层次：理解 · [回看 3.1.2](chapters/03-platforms-tools/3-1.md#3122)
    { .quiz-meta }

<div class="quiz quiz-judge" data-answer="√" markdown>

**6.** 用弹性负载均衡实现同步解耦一般不需要修改代码，而用消息队列实现异步解耦需要调整代码。（　　）

- √
- ×

</div>

??? tip "答案与解析"
    **答案：√**

    解析：这是 3.3.1.2 节的原话。异步解耦要求程序改为“发消息、取消息”的方式工作。

    考查：消息队列使用 · 认知层次：记忆 · [回看 3.3.1](chapters/03-platforms-tools/3-3.md#3312)
    { .quiz-meta }

<div class="quiz quiz-judge" data-answer="√" markdown>

**7.** 执行 `docker run -d -p 4000:80 my-python-app` 时，`-d` 表示让容器在后台运行。（　　）

- √
- ×

</div>

??? tip "答案与解析"
    **答案：√**

    解析：-d 即 detached 模式，容器在后台运行，终端可以继续输入其他命令。

    考查：运行 Docker 容器 · 认知层次：记忆 · [回看 4.1.3.3](chapters/04-applications/4-1.md#4133)
    { .quiz-meta }

<div class="quiz quiz-judge" data-answer="√" markdown>

**8.** Docker Compose 适合用一个 YAML 文件管理一个应用的多个容器，如“网站 + MySQL + Redis”。（　　）

- √
- ×

</div>

??? tip "答案与解析"
    **答案：√**

    解析：教材 4.1.3.5 指出，简单的微服务应用可以用 Docker Compose 编排，执行 docker compose up -d 所有服务自动拉起；实验 4-2 就是这样做的。

    考查：容器编排 · 认知层次：理解 · [回看 4.1.3.5](chapters/04-applications/4-1.md#4135)
    { .quiz-meta }

<div class="quiz quiz-judge" data-answer="√" markdown>

**9.** 边缘计算与云计算是互补关系，常见的架构是“云边协同”。（　　）

- √
- ×

</div>

??? tip "答案与解析"
    **答案：√**

    解析：边缘负责实时处理和本地决策，云端负责全局分析、模型训练和长期存储，两者协同工作。

    考查：边缘计算与云计算 · 认知层次：理解 · [回看 5.1.1](chapters/05-trends-careers/5-1.md#511)
    { .quiz-meta }

<div class="quiz quiz-judge" data-answer="√" markdown>

**10.** DevOps 工程师关注部署频率和故障恢复速度，传统运维工程师更关注系统可用性和故障预防。（　　）

- √
- ×

</div>

??? tip "答案与解析"
    **答案：√**

    解析：见表 5-4“DevOps 工程师与传统运维工程师的差异”的“目标指标”一行。

    考查：DevOps 与传统运维 · 认知层次：理解 · [回看 5.2.1.3](chapters/05-trends-careers/5-2.md#5213)
    { .quiz-meta }

**四、简答题**（每题 10 分）

**1.** 用“公寓”和“酒店房间”的比喻说明虚拟机和容器的区别，并各说一个适合的使用场景。

??? tip "参考答案"
    虚拟机像独立的公寓，每套都有自己完整的水电系统（独立的操作系统内核），隔离彻底，但装修入住慢、占地大；容器像酒店房间，共用大楼的水电系统（宿主机内核），拎包入住、退房快、占用少，但隔离程度不如公寓。需要运行不同操作系统（如在 Linux 服务器上跑 Windows）或对隔离要求高时用虚拟机；需要快速部署、频繁更新的 Web 应用和微服务用容器。

    评分要点：说清共享内核与独立内核的区别（2 分）；启动速度和资源占用（1 分）；场景各 1 分。

**2.** 某初创公司准备上线一个网站，预计白天访问多、夜里很少，促销时访问量是平时的 5 倍。请为它设计云服务器的计费和扩缩容方案。

??? tip "参考答案"
    保底部分：用 1～2 台包年包月的云服务器承担全天的基本访问，单价较低；弹性部分：配置弹性伸缩，CPU 利用率超过阈值（如 70%）时自动增加按量付费实例，低于阈值（如 30%）时自动释放；促销前可以提前设置定时扩容。这样既保证高峰可用，又避免全天按高峰配置造成浪费。

    评分要点：包年包月承担基本负载（2 分）；按量付费 + 弹性伸缩应对波动（2 分）；提到阈值或定时扩容（1 分）。

**3.** 网站部署到云服务器后，用户访问时浏览器提示“无法访问此网站”。请按请求经过的顺序，列出至少四个需要检查的环节。

??? tip "参考答案"
    按顺序检查：① 域名解析是否指向了正确的公网 IP；② 安全组是否放行了 80/443 端口（表现为连接超时）；③ Web 服务器（Nginx/Apache）是否已启动（表现为拒绝连接）；④ 网站代码是否放在了网站根目录；⑤ 网站程序能否连上数据库（表现为数据库连接错误）。

    评分要点：每个环节 1 分，答出四个及以上且顺序合理得满分（5 分）。

## 模拟卷二

**一、单项选择题**（每题 2 分）

<div class="quiz" data-answer="D" markdown>

**1.** 把一台物理服务器抽象成多台虚拟服务器，每台都能运行自己的操作系统，这是（　　）。

- A. 网络虚拟化
- B. 存储虚拟化
- C. 安全虚拟化
- D. 服务器虚拟化

</div>

??? tip "答案与解析"
    **答案：D**

    解析：服务器虚拟化（也叫计算虚拟化）把一台物理服务器“切”成多台虚拟机。存储虚拟化针对磁盘，网络虚拟化针对网络，安全虚拟化把防火墙等安全设备做成虚拟机。

    考查：虚拟化的类型 · 认知层次：理解 · [回看 1.1.2](chapters/01-cloud-basics/1-1.md#1121)
    { .quiz-meta }

<div class="quiz" data-answer="C" markdown>

**2.** 某公司在阿里云上租用虚拟机，自己安装操作系统补丁、部署 Java 运行环境和网站程序。它使用的是（　　）。

- A. SaaS
- B. PaaS
- C. IaaS
- D. 私有云

</div>

??? tip "答案与解析"
    **答案：C**

    解析：用户要自己管操作系统和运行环境，说明云服务商只提供了计算、存储、网络等基础设施，属于 IaaS。D 是部署模式，不是服务模式。

    考查：IaaS · 认知层次：应用 · [回看 1.1.3](chapters/01-cloud-basics/1-1.md#1131)
    { .quiz-meta }

<div class="quiz" data-answer="B" markdown>

**3.** 一家医院希望病历数据只放在自己可控的机房里，同时又能像公有云一样自助申请资源。最合适的部署模式是（　　）。

- A. 公有云
- B. 私有云
- C. 社区云
- D. 互联云

</div>

??? tip "答案与解析"
    **答案：B**

    解析：私有云由单一组织拥有和使用，数据留在自己掌控的环境里，安全性和独占性高，适合敏感数据。公有云面向公众；社区云面向多个组织；互联云是把多个云连起来。

    考查：私有云 · 认知层次：应用 · [回看 1.1.4](chapters/01-cloud-basics/1-1.md#1142)
    { .quiz-meta }

<div class="quiz" data-answer="D" markdown>

**4.** 下面哪个事件与“云原生”关系最密切？（　　）

- A. 1972 年 IBM 推广虚拟化技术
- B. 1999 年 Salesforce 推出在线客户关系管理系统
- C. 2006 年亚马逊推出 EC2
- D. 2014 年 Kubernetes 开源

</div>

??? tip "答案与解析"
    **答案：D**

    解析：云原生以容器、容器编排和微服务为代表，Kubernetes 是容器编排的事实标准。A 属于虚拟化，B 是 SaaS 的落地，C 是公有云商业化的起点。

    考查：云计算的演进历程 · 认知层次：理解 · [回看 1.2.1](chapters/01-cloud-basics/1-2.md#1212)
    { .quiz-meta }

<div class="quiz" data-answer="C" markdown>

**5.** 需要修改客户操作系统、让它“知道”自己运行在虚拟机里，以减少虚拟化开销的技术是（　　）。

- A. 全虚拟化
- B. 基于硬件的虚拟化
- C. 半虚拟化
- D. 桌面虚拟化

</div>

??? tip "答案与解析"
    **答案：C**

    解析：半虚拟化要修改虚拟机中的操作系统，集成一些虚拟化代码，性能较好但兼容性较差；全虚拟化不修改客户操作系统，客户系统察觉不到自己在虚拟机里。

    考查：虚拟化技术分类 · 认知层次：理解 · [回看 2.1.1](chapters/02-core-technologies/2-1.md#2112)
    { .quiz-meta }

<div class="quiz" data-answer="A" markdown>

**6.** 运行中的虚拟机从一台物理主机搬到另一台，期间业务几乎不中断，这叫（　　）。

- A. 热迁移
- B. 冷迁移
- C. 快照回滚
- D. 镜像派生

</div>

??? tip "答案与解析"
    **答案：A**

    解析：热迁移在虚拟机持续运行的状态下，通过预拷贝内存和反复复制“脏页”完成，只在最后切换时有极短的停顿；冷迁移要先关机。

    考查：虚拟机迁移 · 认知层次：记忆 · [回看 2.1.3](chapters/02-core-technologies/2-1.md#2133)
    { .quiz-meta }

<div class="quiz" data-answer="C" markdown>

**7.** 在“三副本”方式下，存 1 TB 的数据实际要占用多少存储空间？（　　）

- A. 1 TB
- B. 1.5 TB
- C. 3 TB
- D. 6 TB

</div>

??? tip "答案与解析"
    **答案：C**

    解析：三副本就是同一份数据存 3 份，空间利用率只有 1/3。纠删码（如 4+2）只需 1.5 倍空间就能容忍 2 块盘损坏，这也是对象存储常用纠删码的原因。可以在“多副本与纠删码”动画里验证。

    考查：数据冗余 · 认知层次：应用 · [回看 2.2.1](chapters/02-core-technologies/2-2.md#221)
    { .quiz-meta }

<div class="quiz" data-answer="A" markdown>

**8.** 用户在云上创建的、与其他用户逻辑隔离、可以自定义 IP 地址范围和子网的网络是（　　）。

- A. 私有网络（VPC）
- B. 弹性 IP
- C. 互联网
- D. 内容分发网络

</div>

??? tip "答案与解析"
    **答案：A**

    解析：VPC 让用户完全控制网络配置，包括 IP 地址范围、子网、路由表和网关，并通过安全组和访问控制列表控制流量。

    考查：私有网络 · 认知层次：理解 · [回看 2.4.2](chapters/02-core-technologies/2-4.md#2422)
    { .quiz-meta }

<div class="quiz" data-answer="A" markdown>

**9.** 企业有一套全年 7×24 小时运行、负载稳定的核心业务系统，从成本角度最合适的计费方式是（　　）。

- A. 包年包月或预留实例
- B. 按量付费
- C. 抢占式实例
- D. 免费试用

</div>

??? tip "答案与解析"
    **答案：A**

    解析：长期稳定运行的业务，预付费方式单价更低；按量付费适合波动大的业务；抢占式实例可能被回收，不适合核心业务。

    考查：选择合适的计费模式 · 认知层次：应用 · [回看 3.1.3](chapters/03-platforms-tools/3-1.md#3131)
    { .quiz-meta }

<div class="quiz" data-answer="D" markdown>

**10.** 关于云服务器的安全管理，下列做法**错误**的是（　　）。

- A. 定期检查安全组规则，只允许必要的流量
- B. 使用强密码或 SSH 密钥
- C. 定期更新操作系统和软件包
- D. 为了方便同事登录，把 root 密码设为 123456 并对全网开放 22 端口

</div>

??? tip "答案与解析"
    **答案：D**

    解析：弱密码加上对全网开放 22 端口，极易被暴力破解。A、B、C 都是 3.2.1.1 节推荐的做法。

    考查：云服务器的安全管理 · 认知层次：评价 · [回看 3.2.1](chapters/03-platforms-tools/3-2.md#3211)
    { .quiz-meta }

<div class="quiz" data-answer="A" markdown>

**11.** 阿里云容器服务 Kubernetes 版的简称是（　　）。

- A. ACK
- B. ECS
- C. OSS
- D. RDS

</div>

??? tip "答案与解析"
    **答案：A**

    解析：ACK 是阿里云容器服务 Kubernetes 版；ECS 是云服务器，OSS 是对象存储，RDS 是云数据库。

    考查：容器服务 · 认知层次：记忆 · [回看 3.3.2](chapters/03-platforms-tools/3-3.md#3321)
    { .quiz-meta }

<div class="quiz" data-answer="D" markdown>

**12.** CI/CD 流水线中，“开发者提交代码后，CI 工具自动编译代码、运行单元测试”属于（　　）阶段。

- A. 源码管理
- B. 监控与反馈
- C. 部署到生产环境
- D. 持续集成

</div>

??? tip "答案与解析"
    **答案：D**

    解析：持续集成包括代码提交、自动化构建（编译、单元测试）和代码质量检查。

    考查：CI/CD 关键阶段 · 认知层次：理解 · [回看 3.5.2](chapters/03-platforms-tools/3-5.md#3521)
    { .quiz-meta }

<div class="quiz" data-answer="D" markdown>

**13.** LAMP 环境中的“M”指的是（　　）。

- A. Memcache
- B. MongoDB
- C. MaxCompute
- D. MySQL

</div>

??? tip "答案与解析"
    **答案：D**

    解析：LAMP 即 Linux、Apache、MySQL、PHP。实验 4-1 使用的 MariaDB 是 MySQL 的开源分支。

    考查：搭建网站：设置云数据库 · 认知层次：记忆 · [回看 4.1.1.4](chapters/04-applications/4-1.md#4114)
    { .quiz-meta }

<div class="quiz" data-answer="A" markdown>

**14.** 在数据分析平台中，需要实时地从多种数据源采集数据，可以选用（　　）。

- A. Apache Kafka、Apache Flume
- B. Tableau、Power BI
- C. MySQL、PostgreSQL
- D. Nginx、Apache

</div>

??? tip "答案与解析"
    **答案：A**

    解析：Kafka、Flume 是分布式数据采集工具；Tableau、Power BI 是 BI 可视化工具；MySQL、PostgreSQL 是关系数据库；Nginx、Apache 是 Web 服务器。

    考查：构建数据分析平台：数据上传 · 认知层次：理解 · [回看 4.1.2.1](chapters/04-applications/4-1.md#4121)
    { .quiz-meta }

<div class="quiz" data-answer="C" markdown>

**15.** Dockerfile 中的 `EXPOSE 80` 表示（　　）。

- A. 把宿主机的 80 端口映射到容器
- B. 容器启动时运行 80 号程序
- C. 声明容器内的应用使用 80 端口，以便外部访问
- D. 删除 80 端口

</div>

??? tip "答案与解析"
    **答案：C**

    解析：EXPOSE 只是声明容器使用的端口；真正把宿主机端口映射到容器端口，要在 docker run 时用 -p 参数，如 -p 4000:80。

    考查：编写 Dockerfile · 认知层次：理解 · [回看 4.1.3.3](chapters/04-applications/4-1.md#4133)
    { .quiz-meta }

<div class="quiz" data-answer="D" markdown>

**16.** 医院同城灾备要求 RPO≤10 min，这里的 RPO 指的是（　　）。

- A. 恢复业务所需的最长时间
- B. 每秒处理的请求数
- C. 服务器的 CPU 利用率
- D. 灾难发生时最多可能丢失多长时间的数据

</div>

??? tip "答案与解析"
    **答案：D**

    解析：RPO（恢复点目标）衡量最多丢失多少数据；RTO（恢复时间目标）衡量多久能恢复业务。

    考查：医疗云灾备 · 认知层次：理解 · [回看 4.2.4.3](chapters/04-applications/4-2.md#42435)
    { .quiz-meta }

<div class="quiz" data-answer="C" markdown>

**17.** 欧洲电信标准化协会在 2014 年提出的、在离用户最近的无线接入网中部署 IT 基础设施的方案是（　　）。

- A. CDN
- B. NFV
- C. MEC（移动边缘计算）
- D. SaaS

</div>

??? tip "答案与解析"
    **答案：C**

    解析：MEC 即 mobile edge computing，由网络运营商主导，在无线接入网中部署计算、存储、网络能力。

    考查：网络运营商移动边缘计算方案 · 认知层次：记忆 · [回看 5.1.1.3](chapters/05-trends-careers/5-1.md#5113)
    { .quiz-meta }

<div class="quiz" data-answer="B" markdown>

**18.** 下列关于 Serverless 的说法，正确的是（　　）。

- A. Serverless 意味着程序运行时根本不需要服务器
- B. 开发者不用管理服务器，平台按实际调用计费并自动伸缩
- C. Serverless 只能运行 Java 程序
- D. Serverless 没有任何缺点

</div>

??? tip "答案与解析"
    **答案：B**

    解析：Serverless 不是没有服务器，而是服务器由云平台管理，开发者只关注业务逻辑；它也面临冷启动、可移植性、可观测性等挑战。

    考查：Serverless 技术优势与挑战 · 认知层次：理解 · [回看 5.1.3.2](chapters/05-trends-careers/5-1.md#5132)
    { .quiz-meta }

<div class="quiz" data-answer="C" markdown>

**19.** 大模型训练需要数千块 GPU，企业一般通过（　　）获取这些算力，而不必自建数据中心。

- A. 购买个人电脑
- B. 只用 CPU 服务器
- C. 云计算平台的 GPU 集群
- D. 手机终端

</div>

??? tip "答案与解析"
    **答案：C**

    解析：云计算凭借弹性扩展、资源池化和按需付费，成为支撑大模型落地的核心基础设施。

    考查：大模型对云计算的需求 · 认知层次：理解 · [回看 5.1.4.2](chapters/05-trends-careers/5-1.md#5142)
    { .quiz-meta }

<div class="quiz" data-answer="D" markdown>

**20.** 深信服云计算认证分为 A、P、E、M 四个等级，其中适合应届毕业生的是（　　）。

- A. 认证大师（SCCM-C）
- B. 认证专家（SCCE-C）
- C. 认证资深工程师（SCCP-C）
- D. 认证工程师（SCCA-C）

</div>

??? tip "答案与解析"
    **答案：D**

    解析：SCCA-C 适合应届毕业生或具备 1~3 年工作经验的初级从业人员。

    考查：深信服云计算认证 · 认知层次：记忆 · [回看 5.2.2.2](chapters/05-trends-careers/5-2.md#5222)
    { .quiz-meta }

**二、多项选择题**（每题 4 分）

<div class="quiz quiz-multi" data-answer="ABD" markdown>

**1.** 资源调度在云计算中的作用包括（　　）。

- A. 提高资源利用率
- B. 保证服务质量
- C. 让用户不再需要网络
- D. 实现弹性扩展

</div>

??? tip "答案与解析"
    **答案：ABD**

    解析：本书把资源调度的作用归纳为提高资源利用率、保证服务质量、实现弹性扩展三点。云计算离不开网络，C 错误。

    考查：资源调度 · 认知层次：记忆 · [回看 1.1.2](chapters/01-cloud-basics/1-1.md#1123)
    { .quiz-meta }

<div class="quiz quiz-multi" data-answer="ABCD" markdown>

**2.** 分布式存储技术的基本特征包括（　　）。

- A. 数据分片
- B. 数据冗余
- C. 故障检测和恢复
- D. 动态扩展

</div>

??? tip "答案与解析"
    **答案：ABCD**

    解析：2.2.1 节列出的特征有数据分片、数据冗余、一致性、故障检测和恢复、动态扩展、提供数据访问接口。

    考查：分布式存储的基本特征 · 认知层次：记忆 · [回看 2.2.1](chapters/02-core-technologies/2-2.md#221)
    { .quiz-meta }

<div class="quiz quiz-multi" data-answer="ABC" markdown>

**3.** 阿里云云数据库 RDS 提供的数据库引擎包括（　　）。

- A. MySQL
- B. SQL Server
- C. PostgreSQL
- D. Excel

</div>

??? tip "答案与解析"
    **答案：ABC**

    解析：3.2.2.1 节介绍了云数据库 MySQL 版、SQL Server 版、PostgreSQL 版。Excel 是电子表格软件，不是数据库引擎。

    考查：云数据库的使用 · 认知层次：记忆 · [回看 3.2.2](chapters/03-platforms-tools/3-2.md#3221)
    { .quiz-meta }

<div class="quiz quiz-multi" data-answer="ABC" markdown>

**4.** 设计微服务架构时，属于“服务编排与管理”的措施有（　　）。

- A. 使用 API 网关管理入口流量
- B. 使用服务发现工具动态注册服务实例
- C. 引入熔断器与重试机制
- D. 所有服务共用一个数据库

</div>

??? tip "答案与解析"
    **答案：ABC**

    解析：微服务主张每个服务拥有独立的数据库，避免数据耦合，D 错误。

    考查：设计微服务架构 · 认知层次：理解 · [回看 4.1.3.2](chapters/04-applications/4-1.md#4132)
    { .quiz-meta }

<div class="quiz quiz-multi" data-answer="ABC" markdown>

**5.** 云计算与人工智能互补协同，体现在（　　）。

- A. 云计算提供海量数据存储，人工智能从数据中提取价值
- B. 云计算提供 GPU 等高性能计算资源，支持模型训练
- C. 云计算提供应用部署平台，人工智能部署智能服务
- D. 人工智能可以完全取代云计算

</div>

??? tip "答案与解析"
    **答案：ABC**

    解析：这是 5.1.2.2 节“互补性协同工作制”的三个方面。

    考查：人工智能与云计算的结合 · 认知层次：理解 · [回看 5.1.2.2](chapters/05-trends-careers/5-1.md#5122)
    { .quiz-meta }

**三、判断题**（每题 1 分）

<div class="quiz quiz-judge" data-answer="√" markdown>

**1.** 社区云在国内也称为团体云或行业云，政务云是它的典型应用。（　　）

- √
- ×

</div>

??? tip "答案与解析"
    **答案：√**

    解析：社区云面向有共同目标和利益的用户群体，各级政府部门共用的政务云就是典型例子。

    考查：社区云 · 认知层次：记忆 · [回看 1.1.4](chapters/01-cloud-basics/1-1.md#1144)
    { .quiz-meta }

<div class="quiz quiz-judge" data-answer="√" markdown>

**2.** 云计算 2.0 阶段的主要标志是资源可以自助申请、自动分配，减少了管理员的人工干预。（　　）

- √
- ×

</div>

??? tip "答案与解析"
    **答案：√**

    解析：2.0 阶段借助软件定义存储、软件定义网络和资源调度自动化软件，实现了基础设施的资源服务化与管理自动化。

    考查：云计算的演进历程 · 认知层次：记忆 · [回看 1.2.1](chapters/01-cloud-basics/1-2.md#1212)
    { .quiz-meta }

<div class="quiz quiz-judge" data-answer="×" markdown>

**3.** 对象存储中的 `photos/2026/cat.jpg` 说明对象存储和文件存储一样，有真正的多层目录结构。（　　）

- √
- ×

</div>

??? tip "答案与解析"
    **答案：×**

    解析：对象存储采用扁平命名空间，斜杠只是对象名的一部分，控制台把它显示成“文件夹”只是为了方便浏览。实验 2-3 中可以观察到这一点。

    考查：对象存储 · 认知层次：理解 · [回看 2.2.2](chapters/02-core-technologies/2-2.md#2221)
    { .quiz-meta }

<div class="quiz quiz-judge" data-answer="×" markdown>

**4.** 弹性 IP 一旦绑定到某台云服务器，就不能再更换绑定对象。（　　）

- √
- ×

</div>

??? tip "答案与解析"
    **答案：×**

    解析：弹性 IP 的特点正是可以动态分配，故障或维护时可以快速解绑并重新绑定到其他实例，保持对外地址不变。

    考查：弹性 IP · 认知层次：记忆 · [回看 2.4.2](chapters/02-core-technologies/2-4.md#2423)
    { .quiz-meta }

<div class="quiz quiz-judge" data-answer="×" markdown>

**5.** 抢占式（竞价）实例价格低，适合运行银行核心交易系统。（　　）

- √
- ×

</div>

??? tip "答案与解析"
    **答案：×**

    解析：竞价实例可能被云服务商回收，只适合对时效性要求不高、可以中断的任务。

    考查：合理利用折扣与优惠 · 认知层次：评价 · [回看 3.1.3](chapters/03-platforms-tools/3-1.md#3132)
    { .quiz-meta }

<div class="quiz quiz-judge" data-answer="×" markdown>

**6.** 使用 MaaS 调用大模型，用户需要先自己下载模型、购买 GPU 服务器并完成部署。（　　）

- √
- ×

</div>

??? tip "答案与解析"
    **答案：×**

    解析：MaaS 的意义就是“即开即用”，模型的训练、部署、运行都由服务商负责，用户通过 API 调用、按量付费。实验 3-2 只需要十几行代码。

    考查：MaaS · 认知层次：理解 · [回看 3.4.2](chapters/03-platforms-tools/3-4.md#342)
    { .quiz-meta }

<div class="quiz quiz-judge" data-answer="×" markdown>

**7.** `docker rmi` 命令用于删除容器。（　　）

- √
- ×

</div>

??? tip "答案与解析"
    **答案：×**

    解析：删除容器用 docker rm，删除镜像用 docker rmi（i 即 image）。

    考查：停止和删除容器、删除镜像 · 认知层次：记忆 · [回看 4.1.3.3](chapters/04-applications/4-1.md#4133)
    { .quiz-meta }

<div class="quiz quiz-judge" data-answer="×" markdown>

**8.** 政务外网承载各级党委和政府的涉密信息系统。（　　）

- √
- ×

</div>

??? tip "答案与解析"
    **答案：×**

    解析：涉密信息系统接入政务内网；政务外网承载非涉密信息系统，如政府门户网站和教育、卫生等公共服务系统。

    考查：通用政务云建设 · 认知层次：理解 · [回看 4.2.1.3](chapters/04-applications/4-2.md#4213)
    { .quiz-meta }

<div class="quiz quiz-judge" data-answer="×" markdown>

**9.** 2014 年阿里云推出了函数计算，这是首个商业化的 FaaS 产品。（　　）

- √
- ×

</div>

??? tip "答案与解析"
    **答案：×**

    解析：首个商业化 FaaS 是 2014 年 AWS 推出的 Lambda；阿里云函数计算 2017 年推出。

    考查：Serverless 发展历程 · 认知层次：记忆 · [回看 5.1.3.1](chapters/05-trends-careers/5-1.md#5131)
    { .quiz-meta }

<div class="quiz quiz-judge" data-answer="×" markdown>

**10.** 云计算认证一旦获得就终身有效，不需要更新。（　　）

- √
- ×

</div>

??? tip "答案与解析"
    **答案：×**

    解析：以深信服认证为例，有效期为 3 年，超过有效期需重新认证或升级；AWS 等认证也有有效期。云计算技术迭代快，需要持续学习。

    考查：认证的重认证机制 · 认知层次：理解 · [回看 5.2.2.2](chapters/05-trends-careers/5-2.md#5222)
    { .quiz-meta }

**四、简答题**（每题 10 分）

**1.** 用自己的话说明 IaaS、PaaS、SaaS 的区别，并各举一个例子。

??? tip "参考答案"
    三者的区别在于云服务商替用户管到哪一层。IaaS 只提供计算、存储、网络等基础设施，用户自己装操作系统和软件，例如租一台阿里云 ECS；PaaS 再加上操作系统、运行环境和中间件，用户只管写代码和放数据，例如云数据库 RDS、应用托管平台；SaaS 连软件都是现成的，用户注册即用，例如钉钉、在线文档。

    评分要点：说清“管到哪一层”（2 分），三个例子各 1 分。

**2.** 对象存储、文件存储、块存储各适合什么场景？各举一个例子。

??? tip "参考答案"
    对象存储适合海量非结构化数据，通过 HTTP 按对象名访问，例如网站图片、短视频、数据备份归档；文件存储有目录树，可被多台机器同时挂载，适合共享文件，例如企业共享盘、AI 训练数据集共享；块存储像本地硬盘，时延低，适合数据库和虚拟机磁盘，例如为 MySQL 服务器挂载的云硬盘。

**3.** 以智慧交通的智能信号灯为例，说明为什么要用边缘计算，而不是把所有视频都传到云端处理。

??? tip "参考答案"
    ① 延迟：边缘节点就在路口，识别结果几十毫秒内就能控制信号灯，云端处理要经过接入网、骨干网往返，延迟更高；② 带宽：几十路高清视频全部上传需要很大的上行带宽，边缘节点只上传异常片段，流量可减少九成以上；③ 可靠性：网络中断时边缘节点仍能离线工作。云端仍负责跨路口的全局优化和模型训练。

    评分要点：延迟、带宽、离线运行各 1～2 分，提到云边协同加分（共 5 分）。
