---
title: 第 3 章 本章实验
description: 在云服务器上部署 Nginx 网站、调用阿里云百炼大模型 API、用 GitHub Actions 搭建持续集成流水线
---

# 第 3 章 本章实验

!!! abstract "实验总览"

    | 实验 | 难度 | 环境 | 时长 | 对应小节 |
    |---|---|---|---|---|
    | [实验 3-1 在云服务器上部署 Nginx 网站](#3-1) | ★ 基础 | 阿里云 ECS（或任意 Linux 云服务器） | 45 分钟 | [3.2.1](3-2.md#3211) |
    | [实验 3-2 调用大模型 API：体验模型即服务](#3-2) | ★ 基础 | 阿里云百炼（新用户有免费额度）+ Python | 30 分钟 | [3.4.2](3-4.md#342) |
    | [实验 3-3 用 GitHub Actions 搭建持续集成流水线](#3-3) | ☆ 拓展 | GitHub 账号 + 浏览器 | 40 分钟 | [3.5.2](3-5.md#352) |
    | [原书实训活动](#book-practice) | 课后 | 阿里云 ECS | 课后 | 全章 |

    本章实验学时为 2 学时。实验 3-1 就是纸质教材本章实训活动的网络版详细步骤，建议必做。

## 实验 3-1 ★ 在云服务器上部署 Nginx 网站 { #3-1 }

**实验目的**

1. 完成“创建云服务器 → 登录 → 装软件 → 放行端口 → 公网访问”的完整流程，对应 [3.2.1.1](3-2.md#3211) 的七个环节；
2. 学会在 Linux 上安装、启动 Nginx，并修改网页内容；
3. 理解安全组在网站发布中的作用（对应 [2.5 节](../02-core-technologies/2-5.md) 的安全组试验台动画）。

**实验环境**

- 运行环境：**云算力**。阿里云 ECS 2 vCPU 2 GiB，镜像 Ubuntu 22.04（也可以用 Alibaba Cloud Linux 3，命令差异见步骤 3）。可以继续使用实验 2-1 的实例。
- 编者实测：在 Ubuntu 22.04 环境中验证了步骤 3～5 的命令（Nginx 1.18.0）；阿里云控制台部分为待实测。
- 费用：沙箱或免费试用 0 元；按量付费约每小时几角钱，实验后释放。

**实验数据**：自己编写的一个网页。

**实验步骤与代码**

1. **准备实例**。按实验 2-1 的步骤创建实例，镜像选 Ubuntu 22.04，勾选“分配公网 IPv4 地址”。记下实例的**公网 IP**。
2. **登录**。在控制台点“远程连接”，或在自己电脑的终端执行：

    ```bash
    ssh root@公网IP
    ```

3. **安装 Nginx**：

    ```bash
    # Ubuntu
    apt update
    apt install -y nginx
    # Alibaba Cloud Linux 3 / CentOS 系列改用：dnf install -y nginx
    nginx -v
    ```

4. **启动并设为开机自启**：

    ```bash
    systemctl start nginx
    systemctl enable nginx
    systemctl status nginx --no-pager | head -3
    curl -s http://localhost | grep title
    ```

5. **换成自己的网页**。Ubuntu 的默认网页目录是 `/var/www/html`（Alibaba Cloud Linux 是 `/usr/share/nginx/html`）：

    ```bash
    echo "<meta charset='utf-8'><h1>你好，这是我的第一台云服务器</h1>" > /var/www/html/index.html
    curl -s http://localhost
    ```

6. **放行 80 端口**。回到控制台，进入实例的“安全组”→“配置规则”→“入方向”→“手动添加”：端口 80/80，授权对象 0.0.0.0/0，协议 TCP，策略允许。
7. **公网访问**。在自己电脑的浏览器里打开 `http://公网IP`，应当看到自己的网页。再查看访问日志：

    ```bash
    tail -3 /var/log/nginx/access.log
    ```

8. **管理实例**。在控制台依次体验“停止”“启动”“重启”实例，以及“监控”页面中的 CPU、网络曲线；停止后再启动，确认 Nginx 是否自动运行（第 4 步设置了开机自启）。实验结束后释放实例。

!!! warning "待实测"
    阿里云控制台的操作（步骤 1、2、6、7、8）在编者环境中无法访问，依据阿里云公开文档编写；任课教师上课前请实测并补充截图。步骤 3～5 的命令编者已在 Ubuntu 22.04 中实际运行验证。

**运行结果**

编者在 Ubuntu 22.04 中运行步骤 3～5 的输出（`systemctl` 一行在容器环境中以直接运行 `nginx` 代替）：

```text
$ nginx -v
nginx version: nginx/1.18.0 (Ubuntu)
$ nginx -t
nginx: the configuration file /etc/nginx/nginx.conf syntax is ok
nginx: configuration file /etc/nginx/nginx.conf test is successful
$ curl -s -o /dev/null -w "HTTP %{http_code}\n" http://localhost/
HTTP 200
$ curl -s http://localhost/ | grep -o "<title>.*</title>"
<title>Welcome to nginx!</title>
$ curl -s http://localhost/        # 换成自己的网页之后
<h1>你好，这是我的第一台云服务器</h1>
$ tail -1 /var/log/nginx/access.log
127.0.0.1 - - [01/Nov/2026:02:24:07 +0000] "GET / HTTP/1.1" 200 52 "-" "curl/7.81.0"
```

在云服务器上从浏览器访问时，访问日志中的第一列会是你自己电脑的公网 IP。

**实验记录表**

| 项目 | 记录 |
|---|---|
| 实例的公网 IP、镜像 |  |
| Nginx 版本 |  |
| 安全组中新增的规则（端口、授权对象） |  |
| 放行 80 端口之前，浏览器访问的结果 |  |
| 放行之后的访问截图 |  |
| 访问日志中记录的客户端 IP |  |
| 停止再启动实例后，网站是否自动恢复 |  |

**常见问题排查**

| 现象 | 原因与处理 |
|---|---|
| `apt install` 很慢 | 阿里云的 Ubuntu 镜像默认使用阿里云内网软件源，一般很快；若改过源，执行 `apt update` 后重试。 |
| 本机 `curl localhost` 正常，浏览器打不开 | 安全组没放行 80 端口；或访问时写成了 `https://`（本实验没有配置证书，要用 `http://`）。 |
| 浏览器显示 Nginx 默认页，不是自己的网页 | 网页写错了目录。Ubuntu 是 `/var/www/html`，Alibaba Cloud Linux 是 `/usr/share/nginx/html`。 |
| 网页中文乱码 | 在网页开头加 `<meta charset='utf-8'>`。 |
| `nginx: [emerg] bind() to 0.0.0.0:80 failed` | 80 端口被其他程序占用，执行 `ss -lntp` 查看哪个程序占用了 80 端口；或 Nginx 已经在运行了。 |

**思考与练习**

1. 实验 2-2 用 Docker 运行 Nginx，本实验直接安装 Nginx，两种方式各有什么优缺点？
2. 如果网站要面向全国用户，而你的服务器在“华南 1（深圳）”，北方用户访问会慢吗？可以用什么云服务改善？（提示：CDN）

**实验报告要求**

提交实验记录表和公网访问截图，并回答思考题第 1 题。

## 实验 3-2 ★ 调用大模型 API：体验模型即服务 { #3-2 }

**实验目的**

1. 体验 [3.4.2](3-4.md#342) 中的 MaaS：不训练、不部署，用十几行代码调用一个大模型；
2. 了解 API Key 的作用和安全使用方法；
3. 观察按 token 计费的方式，理解 MaaS 的“按需计费”。

**实验环境**

- 运行环境：**云算力**（大模型运行在阿里云百炼平台上）+ 本机 Python 3。
- 平台：阿里云百炼（大模型服务平台）。新用户开通后通常有一定的免费调用额度，以平台页面为准。
- 依赖：`pip install openai`（百炼提供与 OpenAI 接口兼容的调用方式，所以用 openai 这个通用库即可）。

**实验数据**：自己提的问题。

**实验步骤与代码**

1. **开通服务**。登录阿里云，在控制台搜索“百炼”，进入“大模型服务平台百炼”，按提示开通。
2. **创建 API Key**。在百炼控制台的“API-KEY”页面创建一个密钥，复制保存。API Key 相当于“调用密码”，**不要发到群里、不要写进代码提交到网上**，泄露后别人可以用你的额度。
3. **设置环境变量**：

    ```bash
    # Linux / macOS
    export DASHSCOPE_API_KEY="sk-你的密钥"
    # Windows 命令提示符
    set DASHSCOPE_API_KEY=sk-你的密钥
    ```

4. **运行程序**（完整代码见 `labs/ch03/lab3_2_bailian.py`）：

    ```python
    import os
    from openai import OpenAI

    client = OpenAI(
        api_key=os.getenv("DASHSCOPE_API_KEY"),
        base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
    )
    resp = client.chat.completions.create(
        model="qwen-plus",
        messages=[
            {"role": "system", "content": "你是一位耐心的云计算课程助教。"},
            {"role": "user", "content": "用三句话向零基础的同学解释什么是云计算的按需付费。"},
        ],
    )
    print(resp.choices[0].message.content)
    print("输入 token：", resp.usage.prompt_tokens, "输出 token：", resp.usage.completion_tokens)
    ```

5. **改一改**：换一个问题；把 `model` 换成百炼“模型广场”里的其他模型；比较不同模型的回答和 token 用量。
6. **查看用量**。回到百炼控制台查看调用次数和 token 消耗。

!!! warning "待实测"
    编者环境无法访问阿里云百炼，程序只做了语法检查，未实际调用。接口地址和模型名依据阿里云百炼公开文档（OpenAI 兼容模式），模型名称和免费额度可能调整，请以百炼控制台为准。任课教师实测后，请把一次真实的输出补进“运行结果”。

**运行结果**

程序会依次输出问题、模型的回答、用时和 token 用量。每次回答的内容都会略有不同，这是大模型的正常现象。请把你的输出粘贴到实验记录表中。

**实验记录表**

| 项目 | 记录 |
|---|---|
| 使用的模型名称 |  |
| 提出的问题 |  |
| 模型的回答（摘要） |  |
| 用时（秒） |  |
| 输入 token 和输出 token |  |
| 换一个模型后，回答有什么不同 |  |

**常见问题排查**

| 现象 | 原因与处理 |
|---|---|
| `401` 或 `Invalid API-key` | 环境变量没设置成功，或密钥复制不完整。用 `echo $DASHSCOPE_API_KEY`（Windows：`echo %DASHSCOPE_API_KEY%`）检查。 |
| `model not found` | 模型名写错，或该模型未开通。到“模型广场”复制准确的模型名。 |
| `ModuleNotFoundError: No module named 'openai'` | 没装依赖，执行 `pip install openai`。 |
| 提示额度用完 | 免费额度已用尽，停止实验，避免产生费用。 |

**思考与练习**

1. 本实验中，模型的训练、部署、GPU 服务器都是谁负责的？你负责什么？用 [3.4.2](3-4.md#342) 的 MaaS 框架解释。
2. 为什么程序用环境变量而不是直接把 API Key 写在代码里？

**实验报告要求**

提交实验记录表和程序运行截图（截图前遮住 API Key），回答两道思考题。

## 实验 3-3 ☆ 用 GitHub Actions 搭建持续集成流水线 { #3-3 }

**实验目的**

1. 亲手搭一条最简单的 CI 流水线：每次提交代码，自动安装依赖、运行测试；
2. 观察测试失败时流水线如何“拦住”有问题的代码，理解 [3.5.2.1](3-5.md#3521) 的关键阶段。

**实验环境**

- 运行环境：**云算力**。GitHub Actions 是 GitHub 提供的托管 CI/CD 服务，公开仓库免费使用，流水线运行在 GitHub 的云服务器上。
- 需要一个 GitHub 账号。国内访问 GitHub 不稳定时，可以改用阿里云云效流水线 Flow 或 Gitee Go，思路相同。
- 编者实测：示例程序和测试在本机 Python 3.13、pytest 9.2.0 下运行通过；GitHub 上的运行为待实测。

**实验数据**：示例项目 `labs/ch03/lab3_3_ci_demo/`，包含一个计算云服务器按量费用的小程序、3 个测试和一个工作流文件。

**实验步骤与代码**

1. **建仓库**。登录 GitHub，新建一个公开仓库，如 `ci-demo`。
2. **上传三个文件**。在仓库页面点“Add file → Create new file”，依次创建：

    `price.py`（被测试的程序）：

    ```python
    def monthly_cost(price_per_hour: float, hours_per_day: float, days: int = 30) -> float:
        """按量付费一个月的费用（元），保留两位小数。"""
        if price_per_hour < 0 or not 0 <= hours_per_day <= 24:
            raise ValueError("单价不能为负，每天使用时长应在 0～24 小时之间")
        return round(price_per_hour * hours_per_day * days, 2)
    ```

    （完整文件还有一个比较付费方式的函数 `cheaper_plan`，见示例项目。）

    `test_price.py`（测试）：

    ```python
    from price import cheaper_plan, monthly_cost

    def test_monthly_cost():
        assert monthly_cost(0.5, 24) == 360.0
        assert monthly_cost(0.5, 4) == 60.0
    ```

    `.github/workflows/ci.yml`（流水线定义，文件名中的目录要一起输入）：

    ```yaml
    name: CI
    on:
      push:
      pull_request:
    jobs:
      test:
        runs-on: ubuntu-latest
        steps:
          - name: 拉取代码
            uses: actions/checkout@v4
          - name: 安装 Python
            uses: actions/setup-python@v5
            with:
              python-version: "3.12"
          - name: 安装依赖
            run: pip install pytest
          - name: 运行测试
            run: pytest -v
    ```

3. **看流水线运行**。提交后点仓库上方的“Actions”标签，可以看到一次运行记录。点进去查看每一步的日志，全部通过时显示绿色对勾。
4. **故意改错**。在线编辑 `price.py`，把 `* days` 改成 `* 31`，提交。再看 Actions：流水线变成红色叉号，日志中能看到哪个测试失败、期望值和实际值。
5. **改回来**，再次提交，流水线恢复绿色。

!!! warning "待实测"
    编者环境无法访问 GitHub，GitHub 页面上的运行结果待实测；程序和测试已在本机实际运行。任课教师实测后请补充 Actions 页面截图。

**运行结果**

编者在本机运行 `pytest -v` 的输出（与流水线“运行测试”一步的日志相同）：

```text
test_price.py::test_monthly_cost PASSED                                  [ 33%]
test_price.py::test_cheaper_plan PASSED                                  [ 66%]
test_price.py::test_bad_input PASSED                                     [100%]

============================== 3 passed in 0.03s ===============================
```

按第 4 步改错后的输出：

```text
E        +  where 372.0 = monthly_cost(0.5, 24)

test_price.py:8: AssertionError
=========================== short test summary info ============================
FAILED test_price.py::test_monthly_cost - assert 372.0 == 360.0
1 failed, 2 passed in 0.01s
```

**实验记录表**

| 项目 | 记录 |
|---|---|
| 仓库地址 |  |
| 第一次运行用时、结果 |  |
| 改错后失败的测试名称和错误信息 |  |
| 改回后的运行结果 |  |
| 流水线有哪几个步骤 |  |

**常见问题排查**

| 现象 | 原因与处理 |
|---|---|
| Actions 页面没有运行记录 | 工作流文件路径必须是 `.github/workflows/` 下的 `.yml` 文件，检查是否少了点号或目录。 |
| 报 `ModuleNotFoundError: No module named 'price'` | `price.py` 和 `test_price.py` 必须放在仓库根目录。 |
| YAML 报错 | YAML 用空格缩进，不能用 Tab，层级要对齐。 |

**思考与练习**

1. 如果再加一个“部署到服务器”的步骤，它应该放在“运行测试”的前面还是后面？为什么？
2. 对照动画“CI/CD 流水线”，本实验实现的是持续集成、持续交付还是持续部署？

**实验报告要求**

提交实验记录表、成功和失败两次运行的 Actions 页面截图，回答两道思考题。

## 原书实训活动 { #book-practice }

下面是纸质教材本章的实训活动。实验 3-1 给出了它的详细操作步骤，完成实验 3-1 即可完成实训的主要内容，再按“实训总结”要求撰写报告。

题目：阿里云 ECS 服务器的创建与管理。

1. 实训目标

（1）熟悉阿里云 ECS 的基本操作流程。

（2）掌握云服务器的创建、配置及管理技巧。

（3）能够基于 ECS 搭建并运行基础 Web 服务。

2. 实训步骤

（1）账号注册与登录。

访问阿里云官网，完成账号注册及实名认证；登录阿里云控制台。

（2）创建 ECS 实例。

选择实例类型：根据需求选择合适的实例系列。

配置存储：选择系统盘类型与大小。

设置网络：配置 VPC、安全组规则。

选择操作系统：挑选合适的镜像。

配置访问方式：设置登录凭证。

（3）连接 ECS 实例。

Windows 实例：使用远程桌面连接。

Linux 实例：使用 SSH 工具连接。

（4）部署 Web 服务。

在 ECS 实例上安装 Web 服务器软件（如 Apache、Nginx）；配置 Web 服务，部署简单的网页内容；访问 Web 服务；通过公网 IP 或域名访问部署的 Web 服务。

（5）管理 ECS 实例。

监控实例运行状态；进行实例的停止、启动、重启操作；根据需求调整实例配置。

3. 实训总结

（1）记录实训过程中的关键步骤与操作细节。

（2）总结使用 ECS 创建和管理服务器的经验。

（3）对比传统物理服务器，阐述云服务器的优势与特点。

通过以上实训活动，学生可以掌握阿里云 ECS 的使用方法，了解云服务器的创建、配置与管理流程，并具备在云服务器上搭建和运行基础服务的能力。
