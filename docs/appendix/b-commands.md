---
title: 附录 B 常用命令速查
description: 本书实验用到的 Linux、Docker、Docker Compose、Kubernetes、Git 和数据库常用命令
---

# 附录 B 常用命令速查

本附录汇总了本书实验中用到的命令，按工具分类，“实验”一列注明在哪个实验里第一次用到。命令中的 `<容器ID>`、`公网IP` 等要换成实际的值。

## B.1 Linux 基本命令 { #b1 }

| 命令 | 作用 | 实验 |
|---|---|---|
| `ssh root@公网IP` | 远程登录云服务器 | 2-1 |
| `apt update` / `apt install -y nginx` | 更新软件源 / 安装软件（Ubuntu） | 3-1 |
| `dnf install -y nginx` | 安装软件（Alibaba Cloud Linux、CentOS 系列） | 3-1 |
| `systemctl start nginx` / `stop` / `restart` | 启动 / 停止 / 重启服务 | 3-1 |
| `systemctl enable nginx` | 设置开机自启 | 3-1 |
| `systemctl status nginx` | 查看服务状态 | 3-1 |
| `curl -s http://localhost` | 在服务器本机访问网页 | 3-1 |
| `ss -lntp` | 查看哪些程序在监听哪些端口 | 3-1 |
| `tail -f /var/log/nginx/access.log` | 实时查看日志的最后几行 | 3-1 |
| `df -h` / `free -h` | 查看磁盘 / 内存使用情况 | — |
| `nano 文件名` | 用简单的文本编辑器修改文件（Ctrl+O 保存，Ctrl+X 退出） | 4-1 |

## B.2 Docker { #b2 }

| 命令 | 作用 | 实验 |
|---|---|---|
| `docker --version` / `docker version` | 查看 Docker 版本 | 2-2 |
| `docker pull nginx:1.27-alpine` | 拉取镜像 | 2-2 |
| `docker images` | 列出本地镜像 | 2-2 |
| `docker run -d -p 8080:80 --name web nginx:1.27-alpine` | 后台运行容器，宿主机 8080 端口映射到容器 80 端口 | 2-2 |
| `docker ps` / `docker ps -a` | 列出运行中的 / 全部容器 | 2-2 |
| `docker logs <容器ID>` | 查看容器日志 | 4-2 |
| `docker exec web2 nginx -v` | 在运行中的容器里执行一条命令 | 2-2 |
| `docker stats --no-stream` | 查看各容器的 CPU、内存占用 | 2-2 |
| `docker stop <容器ID>` / `docker rm <容器ID>` | 停止 / 删除容器 | 2-2 |
| `docker rm -f <容器ID>` | 强制删除运行中的容器 | 4-2 |
| `docker build -t my-python-app .` | 用当前目录的 Dockerfile 构建镜像 | 4-2 |
| `docker rmi my-python-app` | 删除镜像 | 4-2 |
| `docker image prune` | 删除不再使用的镜像 | 4-2 |
| `docker volume ls` | 列出数据卷 | 4-3 |

## B.3 Docker Compose { #b3 }

| 命令 | 作用 | 实验 |
|---|---|---|
| `docker compose up -d` | 按 docker-compose.yml 后台启动全部服务 | 4-2 |
| `docker compose up -d --build` | 先重新构建镜像再启动（改了代码后用） | 4-2 |
| `docker compose ps` | 查看各服务的状态 | 4-2 |
| `docker compose logs -f moodle` | 实时查看某个服务的日志 | 4-3 |
| `docker compose exec redis redis-cli get hits` | 在某个服务的容器里执行命令 | 4-2 |
| `docker compose stop redis` / `start redis` | 停止 / 启动某个服务 | 4-2 |
| `docker compose down` | 停止并删除容器和网络（保留数据卷） | 4-2 |
| `docker compose down -v` | 连数据卷一起删除 | 4-2 |

## B.4 Kubernetes（了解） { #b4 }

本书没有安排 Kubernetes 实验，下面的命令对应 4.1.3.4 节和动画“Kubernetes 自愈与扩缩容”，供拓展学习参考。

| 命令 | 作用 |
|---|---|
| `kubectl apply -f my-service-deployment.yaml` | 按 YAML 文件创建或更新资源 |
| `kubectl get pods` / `kubectl get nodes` | 列出 Pod / 节点 |
| `kubectl scale deployment web --replicas=5` | 把 Deployment 的副本数改为 5 |
| `kubectl set image deployment/web web=myapp:v2` | 滚动更新到新版本镜像 |
| `kubectl delete pod <Pod名>` | 删除一个 Pod（控制器会自动补一个新的） |
| `kubectl describe pod <Pod名>` | 查看 Pod 的详细信息和事件 |

## B.5 Git 与 GitHub { #b5 }

| 命令 | 作用 | 实验 |
|---|---|---|
| `git clone 仓库地址` | 把远程仓库下载到本机 | 3-3 |
| `git add .` | 把修改加入暂存区 | 3-3 |
| `git commit -m "说明"` | 提交修改 | 3-3 |
| `git push` | 推送到远程仓库（会触发 GitHub Actions） | 3-3 |
| `git log --oneline` | 查看提交历史 | 3-3 |

## B.6 数据库 { #b6 }

| 命令 | 作用 | 实验 |
|---|---|---|
| `mysql < init.sql` | 执行 SQL 脚本文件 | 4-1 |
| `mysql --default-character-set=utf8mb4 -e "SELECT * FROM guestbook.messages"` | 执行一条查询并正确显示中文 | 4-1 |
| `CREATE DATABASE …` / `CREATE TABLE …` | 建库 / 建表 | 4-1 |
| `CREATE USER …` / `GRANT … TO …` | 创建数据库账号 / 授权 | 4-1 |

## B.7 Python 与 pip { #b7 }

| 命令 | 作用 | 实验 |
|---|---|---|
| `python --version` | 查看 Python 版本 | 2-3 |
| `pip install -r requirements.txt` | 按文件安装依赖 | 2-3 |
| `pip install boto3 -i https://mirrors.aliyun.com/pypi/simple/` | 使用国内镜像安装 | 2-3 |
| `python 脚本名.py` | 运行脚本 | 2-3 |
| `pytest -q` | 运行单元测试 | 3-3 |
