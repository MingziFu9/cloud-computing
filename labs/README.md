# 实验代码

按章存放，`chNN/` 对应第 NN 章。只需要浏览器和云控制台的实验（1-1、1-2、2-1、3-1）没有代码文件；实验 2-2 只用到 `docker run` 命令，写在教材正文里。

| 实验 | 文件 | 运行方式 |
|---|---|---|
| 2-3 搭建对象存储并用 Python 存取文件 | `ch02/lab2_3_object_storage.py` | 先按教材用 Docker 启动 RustFS，再 `python ch02/lab2_3_object_storage.py` |
| 2-4 用 Python 模拟 MapReduce 词频统计 | `ch02/lab2_4_mapreduce.py` | `python ch02/lab2_4_mapreduce.py` |
| 3-2 调用大模型 API | `ch03/lab3_2_bailian.py` | 设置环境变量 `DASHSCOPE_API_KEY` 后运行（待实测） |
| 3-3 GitHub Actions 持续集成 | `ch03/lab3_3_ci_demo/` | 本机 `cd ch03/lab3_3_ci_demo && pytest`；推到 GitHub 后由 Actions 自动运行 |
| 4-1 LAMP 留言板网站 | `ch04/lab4_1_lamp/` | 在 Ubuntu 22.04 上按教材安装 LAMP，`mysql < init.sql`，把 `guestbook.php` 复制到 `/var/www/html/` |
| 4-2 Docker Compose 部署“网站 + 缓存” | `ch04/lab4_2_compose/` | `cd ch04/lab4_2_compose && docker compose up -d --build`，访问 http://localhost:4000 |
| 4-3 部署 Moodle | `ch04/lab4_3_moodle/` | `cd ch04/lab4_3_moodle && docker compose up -d`，约 2 分钟后访问 http://localhost:8080 |
| 5-1 函数计算 | `ch05/lab5_1_fc/index.py` | 本机 `python ch05/lab5_1_fc/index.py` 模拟调用；部署到阿里云函数计算见教材（待实测） |

安装本机 Python 依赖：

```bash
pip install -r requirements.txt -i https://mirrors.aliyun.com/pypi/simple/
```

所有运行结果都与教材正文中的“运行结果”一致；标为“待实测”的部分需要阿里云控制台，编者环境无法访问。
