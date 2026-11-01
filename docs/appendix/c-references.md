---
title: 附录 C 参考文献
description: 全书各章参考文献汇总，包括教材与专著、在线文档和政策文件
---

# 附录 C 参考文献

本附录汇总了各章“本章小结与练习”页末尾的参考文献，按章排列，每条后面的灰色小字说明它与本书哪部分内容对应。在线资源的访问日期均为 2026 年 11 月 1 日，网址可能变动，打不开时可在对应网站内搜索标题。

纸质教材的编写参考了大量公开资料，本书正文与纸质教材一致，以下文献是网络版为延伸阅读精选的。

## 第 1 章 云计算基础

**教材与专著**

1. 埃尔. 云计算：概念、技术与架构[M]. 龚奕利，贺莲，胡创，译. 北京：机械工业出版社，2014.<br><span class="ref-note">本章云计算定义、NIST 五种角色、服务模式与部署模式的主要参考，对应 1.1 节。</span>
2. 汤兵勇，徐亭，章瑞. 云图·云途：云计算技术演进及应用[M]. 北京：机械工业出版社，2021.<br><span class="ref-note">云计算的演进历程与行业应用，对应 1.1.5 节和 1.2.1 节。</span>
3. 崔升广. 云计算技术应用基础：微课版[M]. 北京：人民邮电出版社，2023.<br><span class="ref-note">面向高职学生的云计算入门教材，可作为本章的平行读物。</span>

**标准与论文**

4. MELL P, GRANCE T. The NIST definition of cloud computing: NIST Special Publication 800-145[R]. Gaithersburg: National Institute of Standards and Technology, 2011.<br><span class="ref-note">NIST 的云计算定义原文，五个基本特点、三种服务模式、四种部署模式都出自这份文件，对应 1.1.1 节。</span>
5. ARMBRUST M, FOX A, GRIFFITH R, et al. A view of cloud computing[J]. Communications of the ACM, 2010, 53(4): 50-58.<br><span class="ref-note">伯克利大学对云计算经济性和挑战的经典分析，“按需付费”“弹性”的论证可延伸阅读。</span>

**在线资源与政策文件**

6. 国务院. “十四五”数字经济发展规划：国发〔2021〕29 号[EB/OL]. (2022-01-12)[2026-11-01]. https://www.gov.cn/zhengce/content/2022-01/12/content_5667817.htm.<br><span class="ref-note">本章导语中“上云用数赋智”的出处。</span>
7. 中国信息通信研究院. 云计算白皮书（2023 年）[R]. 北京：中国信息通信研究院，2023.<br><span class="ref-note">国内云计算市场规模与发展趋势，对应表 1-6 和 1.2.1.3 节。</span>
8. 阿里云. 云服务器 ECS 产品文档[EB/OL]. [2026-11-01]. https://help.aliyun.com/zh/ecs/.<br><span class="ref-note">实验 1-1 所用的 ECS 购买页、付费方式说明。</span>

## 第 2 章 云计算核心技术

**教材与专著**

1. 埃尔. 云计算：概念、技术与架构[M]. 龚奕利，贺莲，胡创，译. 北京：机械工业出版社，2014.<br><span class="ref-note">虚拟化、云存储、云安全威胁（拒绝服务、恶意中介、流量窃听、授权不足、虚拟化攻击）的主要参考，对应 2.1 节和 2.5.3 节。</span>
2. 陈驰. 云计算安全体系[M]. 北京：科学出版社，2014.<br><span class="ref-note">云安全体系架构与关键技术，对应 2.5.4 节、2.5.5 节。</span>
3. 张振峰. 云上合规：深信服云安全服务平台等级保护 2.0 合规能力技术指南[M]. 北京：电子工业出版社，2020.<br><span class="ref-note">等级保护 2.0 与云安全合规，对应 2.5.6 节。</span>

**经典论文**

4. BARHAM P, DRAGOVIC B, FRASER K, et al. Xen and the art of virtualization[C]//Proceedings of the 19th ACM Symposium on Operating Systems Principles. New York: ACM, 2003: 164-177.<br><span class="ref-note">半虚拟化的代表性论文，对应 2.1.1.2 节。</span>
5. GHEMAWAT S, GOBIOFF H, LEUNG S T. The Google file system[C]//Proceedings of the 19th ACM Symposium on Operating Systems Principles. New York: ACM, 2003: 29-43.<br><span class="ref-note">分布式文件系统的奠基论文，HDFS 的设计源头，对应 2.2 节。</span>
6. DEAN J, GHEMAWAT S. MapReduce: simplified data processing on large clusters[C]//Proceedings of the 6th Symposium on Operating Systems Design and Implementation. San Francisco: USENIX, 2004: 137-150.<br><span class="ref-note">MapReduce 原始论文，对应 2.3.3 节和实验 2-4。</span>
7. ZAHARIA M, CHOWDHURY M, DAS T, et al. Resilient distributed datasets: a fault-tolerant abstraction for in-memory cluster computing[C]//Proceedings of the 9th USENIX Symposium on Networked Systems Design and Implementation. San Jose: USENIX, 2012: 15-28.<br><span class="ref-note">Spark 的核心 RDD 论文，对应 2.3.4 节。</span>

**标准与在线资源**

8. 全国信息安全标准化技术委员会. 信息安全技术 网络安全等级保护基本要求：GB/T 22239—2019[S]. 北京：中国标准出版社，2019.<br><span class="ref-note">等级保护 2.0 基本要求，含云计算安全扩展要求，对应 2.5.6.3 节。</span>
9. Docker Inc. Docker documentation[EB/OL]. [2026-11-01]. https://docs.docker.com/.<br><span class="ref-note">Docker 命令与概念，对应 2.1.2.2 节和实验 2-2。</span>
10. RustFS. RustFS 文档[EB/OL]. [2026-11-01]. https://docs.rustfs.com/.<br><span class="ref-note">实验 2-3 所用对象存储的安装与使用说明。</span>

## 第 3 章 云计算平台与工具

**教材与专著**

1. 埃尔. 云计算：概念、技术与架构[M]. 龚奕利，贺莲，胡创，译. 北京：机械工业出版社，2014.<br><span class="ref-note">云服务的计费模型与成本度量，对应 3.1.3 节。</span>
2. 崔升广. 云计算技术应用基础：微课版[M]. 北京：人民邮电出版社，2023.<br><span class="ref-note">公有云平台操作的入门实例，可与实验 3-1 对照。</span>
3. 汤兵勇，徐亭，章瑞. 云图·云途：云计算技术演进及应用[M]. 北京：机械工业出版社，2021.<br><span class="ref-note">云平台与 DevOps 的发展，对应 3.5 节。</span>

**在线资源**

4. 阿里云. 云服务器 ECS 产品文档[EB/OL]. [2026-11-01]. https://help.aliyun.com/zh/ecs/.<br><span class="ref-note">实例创建、安全组、计费方式，对应 3.2.1 节和实验 3-1。</span>
5. 阿里云. 大模型服务平台百炼 文档[EB/OL]. [2026-11-01]. https://help.aliyun.com/zh/model-studio/.<br><span class="ref-note">API Key 创建与 OpenAI 兼容调用方式，对应实验 3-2。</span>
6. GitHub. GitHub Actions documentation[EB/OL]. [2026-11-01]. https://docs.github.com/actions.<br><span class="ref-note">工作流文件语法，对应实验 3-3。</span>
7. HashiCorp. Terraform documentation[EB/OL]. [2026-11-01]. https://developer.hashicorp.com/terraform/docs.<br><span class="ref-note">基础设施即代码的概念与用法，对应 3.5.1.1 节。</span>
8. Red Hat. Ansible documentation[EB/OL]. [2026-11-01]. https://docs.ansible.com/.<br><span class="ref-note">Playbook 与无代理架构，对应 3.5.1.2 节。</span>

## 第 4 章 云计算应用与实践

**教材与专著**

1. 崔升广. 云计算技术应用基础：微课版[M]. 北京：人民邮电出版社，2023.<br><span class="ref-note">云服务器上部署网站的入门实例，可与实验 4-1 对照。</span>
2. 汤兵勇，徐亭，章瑞. 云图·云途：云计算技术演进及应用[M]. 北京：机械工业出版社，2021.<br><span class="ref-note">云计算在政务、金融、制造等行业的应用，对应 4.2 节。</span>
3. 林子雨. 大数据技术原理与应用[M]. 3 版. 北京：人民邮电出版社，2021.<br><span class="ref-note">Hadoop、Spark 与云计算的关系，对应 4.3 节。</span>

**在线资源**

4. Docker Inc. Docker Compose 文档[EB/OL]. [2026-11-01]. https://docs.docker.com/compose/.<br><span class="ref-note">Compose 文件格式和常用命令，对应实验 4-2、4-3。</span>
5. The Kubernetes Authors. Kubernetes 文档：Deployments[EB/OL]. [2026-11-01]. https://kubernetes.io/zh-cn/docs/concepts/workloads/controllers/deployment/.<br><span class="ref-note">副本数、自愈和滚动更新，对应动画“Kubernetes 自愈与扩缩容”。</span>
6. Moodle HQ. Moodle 文档[EB/OL]. [2026-11-01]. https://docs.moodle.org/.<br><span class="ref-note">课程、用户和语言包管理，对应实验 4-3 和原书实训活动。</span>
7. 国务院. 国务院关于加强数字政府建设的指导意见[EB/OL]. (2022-06-23)[2026-11-01]. https://www.gov.cn/zhengce/content/2022-06/23/content_5697299.htm.<br><span class="ref-note">全国一体化政务云平台体系，对应 4.2.1.2 节。</span>

## 第 5 章 未来趋势与职业发展

**教材与专著**

1. 施巍松，刘芳，孙辉，等. 边缘计算[M]. 2 版. 北京：科学出版社，2021.<br><span class="ref-note">边缘计算的概念、架构与应用，对应 5.1.1 节。</span>

**在线资源**

2. 阿里云. 函数计算 FC 产品文档[EB/OL]. [2026-11-01]. https://help.aliyun.com/zh/functioncompute/.<br><span class="ref-note">创建函数、触发器与计费方式，对应实验 5-1。</span>
3. KubeEdge 项目. KubeEdge 文档[EB/OL]. [2026-11-01]. https://kubeedge.io/docs/.<br><span class="ref-note">云边协同的容器编排，对应 5.1.1.3 节。</span>
4. 阿里云. 阿里云认证[EB/OL]. [2026-11-01]. https://edu.aliyun.com/certification/.<br><span class="ref-note">ACA、ACP、ACE 认证的等级与考试大纲，对应 5.2.2.2 节。</span>
5. 华为. 华为认证[EB/OL]. [2026-11-01]. https://e.huawei.com/cn/talent/.<br><span class="ref-note">HCIA、HCIP、HCIE 云计算认证，对应 5.2.2.2 节。</span>
