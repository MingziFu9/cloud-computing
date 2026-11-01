---
title: 附录 A 实验环境准备
description: 阿里云账号与免费资源、Docker 安装与镜像加速、Python 环境、实验费用与安全注意事项
---

# 附录 A 实验环境准备

本书 13 个实验用到三类环境：**浏览器 + 阿里云账号**（实验 1-1、2-1、3-1、3-2、4-1、5-1）、**装有 Docker 的电脑或云服务器**（实验 2-2、2-3、4-2、4-3）、**只需浏览器**（实验 1-2、2-4 可在任意装有 Python 的电脑上做、3-3 用 GitHub 网页）。下表列出各实验的环境：

| 实验 | 环境 | 费用 |
|---|---|---|
| 1-1 注册云平台、逛控制台、算一算价格 | 浏览器 + 阿里云账号 | 0 元 |
| 1-2 服务模式与部署模式对号入座 | 浏览器 | 0 元 |
| 2-1 创建云服务器并打快照 | 阿里云 ECS | 沙箱或试用 0 元 |
| 2-2 用 Docker 运行一个网站 | Docker | 0 元 |
| 2-3 搭建对象存储并用 Python 存取文件 | Docker + Python | 0 元 |
| 2-4 用 Python 模拟 MapReduce 词频统计 | Python | 0 元 |
| 3-1 在云服务器上部署 Nginx 网站 | 阿里云 ECS | 沙箱或试用 0 元 |
| 3-2 调用大模型 API | 阿里云百炼 + Python | 免费额度内 0 元 |
| 3-3 用 GitHub Actions 搭建持续集成流水线 | GitHub 账号 + 浏览器 | 0 元 |
| 4-1 LAMP 留言板网站 | 阿里云 ECS | 沙箱或试用 0 元 |
| 4-2 Docker Compose 部署“网站 + 缓存” | Docker | 0 元 |
| 4-3 部署 Moodle 在线教学平台 | 云服务器 + Docker | 按量付费每小时几角钱 |
| 5-1 在函数计算上部署第一个函数 | 阿里云函数计算 | 免费额度内 0 元 |

## A.1 阿里云账号与免费资源 { #a1 }

1. **注册与实名认证**。打开阿里云官网注册账号，按提示完成个人实名认证（需要身份证和手机号），未实名的账号不能购买云服务器。
2. **云起实验室**。在阿里云官网搜索“云起实验室”，里面有大量免费的动手实验场景，每个场景会临时分配一套云资源，实验结束自动回收，**不会产生费用**，非常适合做实验 2-1、3-1、4-1。
3. **免费试用**。新用户在“免费试用”页面可以领取一定时长的云服务器、对象存储、函数计算等资源，具体产品和时长以页面为准。
4. **学生优惠**。在校学生可以关注阿里云的高校计划，通过学生认证后可享受优惠。

!!! warning "防止意外扣费"
    - 实验结束后在控制台**释放**云服务器（“停止”的实例仍会对云盘、公网 IP 计费）；
    - 删除不用的快照、存储桶中的文件、函数和触发器；
    - 在“费用中心”设置**余额预警**，余额低于设定值时短信提醒；
    - API Key、AccessKey 等密钥不要截图发到群里，也不要写进代码上传到网上。

## A.2 安装 Docker 与配置镜像加速 { #a2 }

**Windows 10/11 和 macOS**：在 Docker 官网下载安装 Docker Desktop，安装后启动，等待左下角显示 Engine running。Windows 需要开启 WSL 2（安装程序会提示）。

**Ubuntu 22.04（云服务器或虚拟机）**：

```bash
sudo apt update
sudo apt install -y docker.io docker-compose-v2
sudo systemctl enable --now docker
sudo usermod -aG docker $USER     # 让当前用户不加 sudo 也能用 docker，重新登录后生效
docker version
docker compose version
```

**配置镜像加速器**。国内访问 Docker Hub 不稳定，可以使用阿里云容器镜像服务 ACR 提供的专属加速地址：登录阿里云控制台 → 搜索“容器镜像服务” → “镜像工具” → “镜像加速器”，复制形如 `https://xxxx.mirror.aliyuncs.com` 的地址，然后：

```bash
sudo mkdir -p /etc/docker
sudo tee /etc/docker/daemon.json <<'JSON'
{ "registry-mirrors": ["https://你的加速地址.mirror.aliyuncs.com"] }
JSON
sudo systemctl restart docker
docker info | grep -A1 "Registry Mirrors"
```

Docker Desktop 用户在 Settings → Docker Engine 的 JSON 中加入同样的 `registry-mirrors` 一行，点 Apply & restart。

**验证**：

```bash
docker run --rm hello-world
```

看到 `Hello from Docker!` 说明安装成功。

!!! note "编者环境"
    本书 Docker 实验在 Docker 29.9.2、Docker Compose v5.6.1 中实测；用到的镜像有 `nginx:1.27-alpine`、`rustfs/rustfs:1.0.4`、`python:3.12-slim`、`redis:7-alpine`、`ubuntu:22.04`、`bitnamilegacy/moodle:4.5`、`bitnamilegacy/mariadb:11.4`。

## A.3 Python 环境 { #a3 }

实验 2-3、2-4、3-2、3-3 需要 Python 3.9 及以上版本。Windows 用户在 Python 官网下载安装包，安装时勾选 Add Python to PATH；Ubuntu 自带 Python 3。

安装本书实验用到的全部依赖（在仓库根目录执行）：

```bash
pip install -r labs/requirements.txt -i https://mirrors.aliyun.com/pypi/simple/
```

`-i` 参数指定阿里云的 PyPI 镜像，下载更快。

## A.4 GitHub 账号 { #a4 }

实验 3-3 需要一个 GitHub 账号：在 GitHub 官网用邮箱注册即可，免费账号可以使用 GitHub Actions。国内访问 GitHub 有时较慢，可以换个时间再试；也可以改用阿里云云效流水线 Flow 或 Gitee Go，思路相同。

## A.5 实验报告的一般要求 { #a5 }

每个实验后面都有“实验记录表”和“实验报告要求”。一般要提交：

1. 填好的实验记录表；
2. 关键步骤的截图（截图中要能看出是你自己的账号或主机名，遮住密码和密钥）；
3. 思考题的回答；
4. 遇到的问题和解决办法（选写，写得好可加分）。
