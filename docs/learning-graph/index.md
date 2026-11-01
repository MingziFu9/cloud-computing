---
title: 学习图谱
description: 全书核心概念及其先修关系，点一个概念就能看到学习路径
---

# 学习图谱

学习图谱把全书的核心概念和它们之间的“先修关系”画在一张图上：要理解一个概念，得先懂哪些更基础的概念；顺着箭头往回找，就是一条学习路径。

<iframe class="sim-frame" src="main.html" height="900" loading="lazy" title="学习图谱"></iframe>

[全屏打开](main.html){ target=_blank }

## 怎样使用

- **预习**：学新的一章前，点开本章的概念，看看橙色的先修概念自己是否都掌握了，没掌握的先回去复习；
- **复习**：期末复习时，从最后几章的概念出发，顺着学习路径往回梳理，就能把全书串起来；
- **查漏补缺**：做练习时遇到不懂的概念，在搜索框里输入它，看它依赖哪些更基础的概念。

<!-- graph:start -->

图谱共有 **65 个概念、72 条先修关系**，概念按章排列，颜色表示 6 个类别（基本概念、服务与部署模式、核心技术、云服务与工具、应用与架构、前沿趋势与职业）。概念的定义都来自[附录 D 术语表](../appendix/glossary.md)，先修关系由编者根据各章内容整理。

## 文字版

下面按章列出每个概念的直接先修概念，便于打印或用读屏软件阅读。

??? note "第 1 章 云计算基础（14 个概念）"

    | 概念 | 类别 | 直接先修 |
    |---|---|---|
    | [云计算](../appendix/glossary.md#g-云计算) | 基本概念 | — |
    | [虚拟化](../appendix/glossary.md#g-虚拟化) | 基本概念 | [云计算](../appendix/glossary.md#g-云计算) |
    | [分布式计算](../appendix/glossary.md#g-分布式计算) | 基本概念 | [云计算](../appendix/glossary.md#g-云计算) |
    | [资源调度](../appendix/glossary.md#g-资源调度) | 基本概念 | [虚拟化](../appendix/glossary.md#g-虚拟化) |
    | [多租户](../appendix/glossary.md#g-多租户) | 基本概念 | [云计算](../appendix/glossary.md#g-云计算) |
    | [弹性伸缩](../appendix/glossary.md#g-弹性伸缩) | 基本概念 | [资源调度](../appendix/glossary.md#g-资源调度) |
    | [按需付费](../appendix/glossary.md#g-按需付费) | 基本概念 | [云计算](../appendix/glossary.md#g-云计算) |
    | [基础设施即服务](../appendix/glossary.md#g-基础设施即服务) | 服务与部署模式 | [云计算](../appendix/glossary.md#g-云计算) |
    | [平台即服务](../appendix/glossary.md#g-平台即服务) | 服务与部署模式 | [基础设施即服务](../appendix/glossary.md#g-基础设施即服务) |
    | [软件即服务](../appendix/glossary.md#g-软件即服务) | 服务与部署模式 | [平台即服务](../appendix/glossary.md#g-平台即服务) |
    | [公有云](../appendix/glossary.md#g-公有云) | 服务与部署模式 | [多租户](../appendix/glossary.md#g-多租户) |
    | [私有云](../appendix/glossary.md#g-私有云) | 服务与部署模式 | [云计算](../appendix/glossary.md#g-云计算) |
    | [混合云](../appendix/glossary.md#g-混合云) | 服务与部署模式 | [公有云](../appendix/glossary.md#g-公有云)、[私有云](../appendix/glossary.md#g-私有云) |
    | [社区云](../appendix/glossary.md#g-社区云) | 服务与部署模式 | [私有云](../appendix/glossary.md#g-私有云) |

??? note "第 2 章 核心技术（16 个概念）"

    | 概念 | 类别 | 直接先修 |
    |---|---|---|
    | [虚拟机监视器](../appendix/glossary.md#g-虚拟机监视器) | 核心技术 | [虚拟化](../appendix/glossary.md#g-虚拟化) |
    | [容器](../appendix/glossary.md#g-容器) | 核心技术 | [虚拟化](../appendix/glossary.md#g-虚拟化) |
    | [快照](../appendix/glossary.md#g-快照) | 核心技术 | [虚拟机监视器](../appendix/glossary.md#g-虚拟机监视器) |
    | [虚拟机迁移](../appendix/glossary.md#g-虚拟机迁移) | 核心技术 | [虚拟机监视器](../appendix/glossary.md#g-虚拟机监视器) |
    | [对象存储](../appendix/glossary.md#g-对象存储) | 核心技术 | [分布式计算](../appendix/glossary.md#g-分布式计算) |
    | [文件存储](../appendix/glossary.md#g-文件存储) | 核心技术 | [分布式计算](../appendix/glossary.md#g-分布式计算) |
    | [块存储](../appendix/glossary.md#g-块存储) | 核心技术 | [分布式计算](../appendix/glossary.md#g-分布式计算) |
    | [纠删码](../appendix/glossary.md#g-纠删码) | 核心技术 | [对象存储](../appendix/glossary.md#g-对象存储) |
    | [MapReduce](../appendix/glossary.md#g-MapReduce) | 核心技术 | [分布式计算](../appendix/glossary.md#g-分布式计算) |
    | [Spark](../appendix/glossary.md#g-Spark) | 核心技术 | [MapReduce](../appendix/glossary.md#g-MapReduce) |
    | [软件定义网络](../appendix/glossary.md#g-软件定义网络) | 核心技术 | [虚拟化](../appendix/glossary.md#g-虚拟化) |
    | [私有网络](../appendix/glossary.md#g-私有网络) | 核心技术 | [软件定义网络](../appendix/glossary.md#g-软件定义网络) |
    | [弹性 IP](../appendix/glossary.md#g-弹性-IP) | 核心技术 | [私有网络](../appendix/glossary.md#g-私有网络) |
    | [安全组](../appendix/glossary.md#g-安全组) | 核心技术 | [私有网络](../appendix/glossary.md#g-私有网络) |
    | [等级保护制度](../appendix/glossary.md#g-等级保护制度) | 核心技术 | [安全组](../appendix/glossary.md#g-安全组) |
    | [桌面云](../appendix/glossary.md#g-桌面云) | 核心技术 | [虚拟化](../appendix/glossary.md#g-虚拟化) |

??? note "第 3 章 平台与工具（13 个概念）"

    | 概念 | 类别 | 直接先修 |
    |---|---|---|
    | [抢占式实例](../appendix/glossary.md#g-抢占式实例) | 云服务与工具 | [基础设施即服务](../appendix/glossary.md#g-基础设施即服务)、[按需付费](../appendix/glossary.md#g-按需付费) |
    | [云数据库](../appendix/glossary.md#g-云数据库) | 云服务与工具 | [平台即服务](../appendix/glossary.md#g-平台即服务) |
    | [消息队列](../appendix/glossary.md#g-消息队列) | 云服务与工具 | [平台即服务](../appendix/glossary.md#g-平台即服务) |
    | [API 网关](../appendix/glossary.md#g-API-网关) | 云服务与工具 | [平台即服务](../appendix/glossary.md#g-平台即服务) |
    | [函数计算](../appendix/glossary.md#g-函数计算) | 云服务与工具 | [容器](../appendix/glossary.md#g-容器)、[平台即服务](../appendix/glossary.md#g-平台即服务) |
    | [模型即服务](../appendix/glossary.md#g-模型即服务) | 云服务与工具 | [软件即服务](../appendix/glossary.md#g-软件即服务) |
    | [客户关系管理](../appendix/glossary.md#g-客户关系管理) | 云服务与工具 | [软件即服务](../appendix/glossary.md#g-软件即服务) |
    | [企业资源计划](../appendix/glossary.md#g-企业资源计划-ERP) | 云服务与工具 | [软件即服务](../appendix/glossary.md#g-软件即服务) |
    | [基础设施即代码](../appendix/glossary.md#g-基础设施即代码) | 云服务与工具 | [基础设施即服务](../appendix/glossary.md#g-基础设施即服务) |
    | [Terraform](../appendix/glossary.md#g-Terraform) | 云服务与工具 | [基础设施即代码](../appendix/glossary.md#g-基础设施即代码) |
    | [Ansible](../appendix/glossary.md#g-Ansible) | 云服务与工具 | [基础设施即代码](../appendix/glossary.md#g-基础设施即代码) |
    | [持续集成](../appendix/glossary.md#g-持续集成) | 云服务与工具 | — |
    | [持续交付](../appendix/glossary.md#g-持续交付) | 云服务与工具 | [持续集成](../appendix/glossary.md#g-持续集成) |

??? note "第 4 章 应用与实践（12 个概念）"

    | 概念 | 类别 | 直接先修 |
    |---|---|---|
    | [LAMP](../appendix/glossary.md#g-LAMP) | 应用与架构 | [块存储](../appendix/glossary.md#g-块存储)、[云数据库](../appendix/glossary.md#g-云数据库) |
    | [SSL 证书](../appendix/glossary.md#g-SSL-证书) | 应用与架构 | [安全组](../appendix/glossary.md#g-安全组) |
    | [数据湖](../appendix/glossary.md#g-数据湖) | 应用与架构 | [对象存储](../appendix/glossary.md#g-对象存储)、[Spark](../appendix/glossary.md#g-Spark) |
    | [微服务](../appendix/glossary.md#g-微服务) | 应用与架构 | [API 网关](../appendix/glossary.md#g-API-网关) |
    | [Dockerfile](../appendix/glossary.md#g-Dockerfile) | 应用与架构 | [容器](../appendix/glossary.md#g-容器) |
    | [Kubernetes](../appendix/glossary.md#g-Kubernetes) | 应用与架构 | [容器](../appendix/glossary.md#g-容器)、[微服务](../appendix/glossary.md#g-微服务)、[弹性伸缩](../appendix/glossary.md#g-弹性伸缩) |
    | [Docker Compose](../appendix/glossary.md#g-Docker-Compose) | 应用与架构 | [Dockerfile](../appendix/glossary.md#g-Dockerfile) |
    | [政务云](../appendix/glossary.md#g-政务云) | 应用与架构 | [混合云](../appendix/glossary.md#g-混合云) |
    | [信创](../appendix/glossary.md#g-信创) | 应用与架构 | [政务云](../appendix/glossary.md#g-政务云) |
    | [两地三中心](../appendix/glossary.md#g-两地三中心) | 应用与架构 | [快照](../appendix/glossary.md#g-快照) |
    | [工业云](../appendix/glossary.md#g-工业云) | 应用与架构 | [混合云](../appendix/glossary.md#g-混合云) |
    | [数据即服务](../appendix/glossary.md#g-数据即服务) | 应用与架构 | [数据湖](../appendix/glossary.md#g-数据湖) |

??? note "第 5 章 趋势与职业（10 个概念）"

    | 概念 | 类别 | 直接先修 |
    |---|---|---|
    | [边缘计算](../appendix/glossary.md#g-边缘计算) | 前沿趋势与职业 | [分布式计算](../appendix/glossary.md#g-分布式计算) |
    | [物联网](../appendix/glossary.md#g-物联网) | 前沿趋势与职业 | [边缘计算](../appendix/glossary.md#g-边缘计算)、[工业云](../appendix/glossary.md#g-工业云) |
    | [移动边缘计算](../appendix/glossary.md#g-移动边缘计算-MEC) | 前沿趋势与职业 | [边缘计算](../appendix/glossary.md#g-边缘计算) |
    | [无服务器计算](../appendix/glossary.md#g-无服务器计算) | 前沿趋势与职业 | [函数计算](../appendix/glossary.md#g-函数计算) |
    | [函数即服务](../appendix/glossary.md#g-函数即服务) | 前沿趋势与职业 | [无服务器计算](../appendix/glossary.md#g-无服务器计算) |
    | [冷启动](../appendix/glossary.md#g-冷启动) | 前沿趋势与职业 | [函数即服务](../appendix/glossary.md#g-函数即服务) |
    | [大模型](../appendix/glossary.md#g-大模型) | 前沿趋势与职业 | [模型即服务](../appendix/glossary.md#g-模型即服务)、[Transformer](../appendix/glossary.md#g-Transformer) |
    | [Transformer](../appendix/glossary.md#g-Transformer) | 前沿趋势与职业 | — |
    | [检索增强生成](../appendix/glossary.md#g-检索增强生成) | 前沿趋势与职业 | [大模型](../appendix/glossary.md#g-大模型) |
    | [DevOps](../appendix/glossary.md#g-DevOps) | 前沿趋势与职业 | [持续交付](../appendix/glossary.md#g-持续交付)、[Ansible](../appendix/glossary.md#g-Ansible) |

<!-- graph:end -->
