# Cam-Tu Nguyen 教授近年论文梳理（2024—2026）

> 核查日期：2026-10-12。这里将“近年”界定为 2024—2026 年；收录能够核实 **Cam-Tu Nguyen（亦写作 Cam Tu Nguyen、Nguyen Cam-Tu）本人署名**的 30 项研究。会议版、期刊版、预印本若属于同一研究，合并说明发表历程，不重复列为不同论文。链接优先指向会议论文集、期刊、arXiv 原页，少数条目指向作者或合作团队页面。本清单是截至核查日可核实的梳理，不能保证覆盖所有尚未被索引的稿件。

## 总览

| 年份 | 本文收录 | 已正式发表或有会议论文集记录 | 目前仅查到预印本 / 录用消息 |
| --- | ---: | ---: | ---: |
| 2026 | 13 | 10 | 3 |
| 2025 | 9 | 8 | 1 |
| 2024 | 8 | 6 | 2 |
| **合计** | **30** | **24** | **6** |

说明：2026 年的 MeteorIR 目前按“录用消息”统计；CVPR 2026、SIGCOMM 2026 Workshop 等有会议或项目的正式记录。上述计数是本文的核实结果，不等于研究者的完整学术履历。

## 2026 年

### 1. [LLM-based Embeddings: Attention Values Encode Sentence Semantics Better Than Hidden States](https://proceedings.mlr.press/v306/zhang26ga.html)

- **发表情况：** ICML 2026 正式论文，PMLR 306:158943–158959。
- **作者：** Yeqin Zhang、Yunfei Wang、Chen Jiaxuan、Ke Qin、Yizheng Zhao、Cam-Tu Nguyen。
- **方向与内容：** 文本表示 / 检索；研究发现 LLM 的注意力 value 向量可比常用隐藏状态更好地编码句子语义，并提出无需额外训练的聚合方法。

### 2. [Learning to Compress: Unlocking the Potential of Large Language Models for Text Representation](https://ojs.aaai.org/index.php/AAAI/article/view/40075)

- **发表情况：** AAAI 2026 正式论文，40(34):28456–28464；2025 年曾发布[预印本](https://arxiv.org/abs/2511.17129)。
- **作者：** Yeqin Zhang、Yizheng Zhao、Chen Hu、Binxing Jiao、Daxin Jiang、Ruihang Miao、Cam-Tu Nguyen。
- **方向与内容：** 文本表示 / 模型适配；以“压缩上下文并保留预测所需信息”为预训练任务，提升 LLM 生成文本向量的能力。

### 3. [LLMs Meet Isolation Kernel: Lightweight, Learning-free Binary Embeddings for Fast Retrieval](https://aclanthology.org/2026.findings-acl.666/)

- **发表情况：** Findings of ACL 2026 正式论文，13601–13623；另有[arXiv 预印本](https://arxiv.org/abs/2601.09159)。
- **作者：** Zhibo Zhang、Yang Xu、Kai Ming Ting、Cam-Tu Nguyen。
- **方向与内容：** 高效文本检索；用无需训练的 Isolation Kernel 将高维 LLM 向量转换为二值表示，以降低存储与检索开销。

### 4. [Bidirectional Semantic Enhancement for Schema Routing Across Large-Scale Databases](https://aclanthology.org/2026.findings-acl.369/)

- **发表情况：** Findings of ACL 2026 正式论文，7495–7509。
- **作者：** Yuyang Wu、Xiaoliang Wang、Cam-Tu Nguyen。
- **方向与内容：** Text-to-SQL / 数据库检索；同时扩充含糊的表结构描述和用户查询语义，帮助系统在大规模数据库中找到相关表。

### 5. [TrigReason: Trigger-Based Collaboration between Small and Large Reasoning Models](https://aclanthology.org/2026.findings-acl.333/)

- **发表情况：** Findings of ACL 2026 正式论文；另有[arXiv 预印本](https://arxiv.org/abs/2604.14847)。
- **作者：** Yi Zhao、Yajuan Peng、Cam-Tu Nguyen、Zuchao Li、Xiaoliang Wang、Xiaoming Fu、Hai Zhao。
- **方向与内容：** 推理效率 / 小大模型协作；让小模型执行大部分推理，仅在规划、过载或陷入循环等触发条件下调用大模型。

### 6. [MiMIC: Mitigating Visual Modality Collapse in Universal Multimodal Retrieval While Avoiding Semantic Misalignment](https://aclanthology.org/2026.findings-acl.158/)

- **发表情况：** Findings of ACL 2026 正式论文；另有[arXiv 预印本](https://arxiv.org/abs/2604.21326)。
- **作者：** Juan Li、Chuanghao Ding、Xujie Zhang、Cam-Tu Nguyen。
- **方向与内容：** 多模态检索；用解码器融合和训练策略缓解图像信息被忽略及图文语义错位的问题。

### 7. [Thermometer of Thoughts: Enhancing LLM’s Exploration via Attention Temperature Modulation](https://aclanthology.org/2026.acl-long.200/)

- **发表情况：** ACL 2026 主会长论文，4355–4368。
- **作者：** Zhiyuan Yu、Shijian Xiao、Cam-Tu Nguyen、Zhangyue Yin、Lekai Xing、Wenzhong Li、Sanglu Lu。
- **方向与内容：** LLM 推理；通过调节注意力温度改变模型内部探索程度，再按问题难度汇总候选推理路径。

### 8. [Beyond the Global Scores: Fine-Grained Token Grounding as a Robust Detector of LVLM Hallucinations](https://arxiv.org/abs/2604.04863)

- **发表情况：** CVPR 2026 主会论文；[论文项目页](https://token-grounding-detection-cvpr26.github.io/)也列出会议版。
- **作者：** Tuan Dung Nguyen、Minh Khoi Ho、Qi Chen、Yutong Xie、Cam-Tu Nguyen、Minh Khoi Nguyen、Dang Huy Pham Nguyen、Anton van den Hengel、Johan W. Verjans、Phi Le Nguyen、Vu Minh Hieu Phan。
- **方向与内容：** 视觉语言模型可靠性；用图像局部区域与生成 token 的细粒度对应关系检测“看图编造”的内容。

### 9. [Fine-Grained Scheduling of In-Network Aggregation Resources for Efficient Machine Learning Service](https://doi.org/10.1109/TON.2025.3617081)

- **发表情况：** *IEEE Transactions on Networking* 34:1160–1174（2026）；与下文 INFOCOM 2025 的 MINA 工作密切相关，但期刊标题和作者阵容不同，故单列。
- **作者：** Shichen Dong、Zhixiong Niu、Mingchao Zhang、Zhiying Xu、Chuntao Hu、Pengzhi Zhu、Qingchun Song、Lei Qu、Peng Cheng、Cam-Tu Nguyen、Shaoling Sun、Xiaohu Xu、Yongqiang Xiong、Wei Wang、Xiaoliang Wang、Guihai Chen。
- **方向与内容：** AI 系统 / 计算机网络；细粒度调度交换机内的聚合资源，提升多项机器学习训练任务共享网络加速能力时的效率。

### 10. [GPU-Centric Stateless LLM Serving With GIGANETS](https://dblp.org/rec/conf/sigcomm/WangPZN26.html)

- **发表情况：** ACM SIGCOMM 2026 的 [Networks for AI Computing Workshop](https://conferences.sigcomm.org/sigcomm/2026/naic/) 论文，1988–1993；**是 SIGCOMM 附属研讨会论文，不是 SIGCOMM 主会长论文**。
- **作者：** Xiaoliang Wang、Zhenwei Pi、Rui Zhang、Cam-Tu Nguyen。
- **方向与内容：** LLM 服务系统；根据公开标题和会议议程，这项工作探索以 GPU 为中心的无状态模型服务架构；未查到可核对的公开摘要，因此不进一步推断实现细节。

### 11. [MeteorIR: Why Multimodal LLMs Hallucinate the Weather?](https://njuhml.github.io/en/publish/publish.html)

- **发表情况：** [导师主页](https://ai.nju.edu.cn/CamTuNguyen/)称获 ACM MM 2026 录用；合作的南京大学水文气象实验室目录也标“Accepted”，但将刊名写为 *ACM Multimedia Systems Conference 2026*。两处刊名不一致，截至核查日未据可访问的正式论文页面消除分歧，因此暂记为**已报告录用，准确会议名称待核**。
- **作者：** C. Ding、Z. Li、Y. Liu、J. Li、H. Yuan、X. Wang、C.-T. Nguyen。合作团队公开目录仅给出缩写，这里不擅自补写全名。
- **方向与内容：** 多模态模型 / 气象图理解；围绕模型识读气象图和视觉推理时的幻觉或能力局限进行研究（依据标题和[会议报告题名](https://mm.cms1924.org/cn/web/program/29509?date_id=14189&hall_id=32230&session_id=886040)概括）。

### 12. [LifeBench: A Benchmark for Long-Horizon Multi-Source Memory](https://arxiv.org/abs/2603.03781)

- **发表情况：** 2026 年 arXiv 预印本；本次未核实到正式会议或期刊版本。
- **作者：** Zihao Cheng、Weixin Wang、Yu Zhao、Ziyang Ren、Jiaxuan Chen、Ruiyang Xu、Shuai Huang、Yang Chen、Guowei Li、Mengshi Wang、Yi Xie、Ren Zhu、Zeren Jiang、Keda Lu、Yihong Li、Xiaoliang Wang、Liwei Liu、Cam-Tu Nguyen。
- **方向与内容：** Agent 长期记忆评测；构建跨时间、跨来源的事件基准，检验系统是否能综合显式事实与习惯、流程等隐性记忆。

### 13. [Structures Facilitate Retrieve, Rerank, and Generate](https://arxiv.org/abs/2606.03247)

- **发表情况：** 2026 年 arXiv 预印本；本次未核实到正式会议或期刊版本。
- **作者：** Yeqin Zhang、Haomin Fu、Xujie Zhang、Cam-Tu Nguyen。
- **方向与内容：** 文档对话 / RAG；把文档的章节和邻接结构用于段落检索、重排序和答案生成。

## 2025 年

### 14. [MLAlgo-Bench: Can Machines Implement Machine Learning Algorithms?](https://aclanthology.org/2025.findings-emnlp.772/)

- **发表情况：** Findings of EMNLP 2025 正式论文，14298–14329。
- **作者：** Yunfei Wang、Yeqin Zhang、Yuyang Wu、Liang Lu、Phi Le Nguyen、Xiaoliang Wang、Cam-Tu Nguyen。
- **方向与内容：** AI for AI / 代码生成评测；建立从机器学习算法描述及 Kaggle 解题草案生成可运行代码的基准。

### 15. [SmallKV: Small Model Assisted Compensation of KV Cache Compression for Efficient LLM Inference](https://papers.neurips.cc/paper_files/paper/2025/hash/45790132b9f91b5787232e1cbe0712fc-Abstract-Conference.html)

- **发表情况：** NeurIPS 2025 主会正式论文；[导师主页](https://ai.nju.edu.cn/CamTuNguyen/)和[合作者主页](https://cs.nju.edu.cn/wangxiaoliang/index_files/index.psp)注明 Spotlight。
- **作者：** Yi Zhao、Yajuan Peng、Cam-Tu Nguyen、Zuchao Li、Xiaoliang Wang、Hai Zhao、Xiaoming Fu。
- **方向与内容：** LLM 推理效率；利用小模型的注意力信息补偿大模型 KV cache 压缩时丢失的重要或边缘 token 信息。

### 16. [Consultant Decoding: Yet Another Synergistic Mechanism](https://aclanthology.org/2025.findings-acl.797/)

- **发表情况：** Findings of ACL 2025 正式论文，15438–15452。
- **作者：** Chuanghao Ding、Jiaping Wang、Ziqing Yang、Xiaoliang Wang、Dahua Lin、Cam-Tu Nguyen、Fei Tan。
- **方向与内容：** LLM 推理加速；提出 Consultant Decoding，让小模型与大模型协作生成以减少大模型验证调用。

### 17. [daDPO: Distribution-Aware DPO for Distilling Conversational Abilities](https://aclanthology.org/2025.findings-acl.796/)

- **发表情况：** Findings of ACL 2025 正式论文，15421–15437。
- **作者：** Zhengze Zhang、Shiqi Wang、Yiqun Shen、Simin Guo、Dahua Lin、Xiaoliang Wang、Cam Tu Nguyen、Fei Tan。
- **方向与内容：** 小模型能力蒸馏 / 偏好优化；将教师模型的概率分布信息加入 DPO，使小模型更好地继承对话能力。

### 18. [Momentum Posterior Regularization for Multi-hop Dense Retrieval](https://aclanthology.org/2025.coling-main.550/)

- **发表情况：** COLING 2025 正式论文，8255–8271。
- **作者：** Zehua Xia、Yuyang Wu、Yiyun Xia、Cam Tu Nguyen。
- **方向与内容：** 多跳检索 / 问答；用动量更新的后验检索器向推理时可用的前验检索器传递跨跳信息。

### 19. [LAVa: Layer-wise KV Cache Eviction with Dynamic Budget Allocation](https://aclanthology.org/2025.findings-emnlp.737/)

- **发表情况：** Findings of EMNLP 2025 正式论文，13672–13692。
- **作者：** Yiqun Shen、Song Yuan、Zhengze Zhang、Xiaoliang Wang、Daxin Jiang、Cam-Tu Nguyen。
- **方向与内容：** LLM 长上下文推理；依据层和注意力头的信息损失动态分配 KV cache，决定哪些缓存项应被淘汰。

### 20. [Mina: Fine-Grained In-network Aggregation Resource Scheduling for Machine Learning Service](https://www.microsoft.com/en-us/research/publication/mina-fine-grained-in-network-aggregation-resource-scheduling-for-machine-learning-service/)

- **发表情况：** IEEE INFOCOM 2025 正式论文，1–10；相关期刊论文见第 9 项。
- **作者：** Shichen Dong、Zhixiong Niu、Mingchao Zhang、Zhiying Xu、Chuntao Hu、Pengzhi Zhu、Qingchun Song、Lei Qu、Peng Cheng、Cam-Tu Nguyen、Shaoling Sun、Xiaohu Xu、Yongqiang Xiong、Wei Wang、Xiaoliang Wang。
- **方向与内容：** 分布式机器学习 / 网络内计算；为多个训练任务在时间和空间维度上调度交换机的梯度聚合资源。

### 21. [Accelerating Network Features Deployment With Heterogeneous Platforms](https://doi.org/10.1109/TNET.2024.3491840)

- **发表情况：** *IEEE Transactions on Networking* 33(1):430–445（2025）。
- **作者：** Tingting Xu、Xiaoliang Wang、Chen Tian、Yun Xiong、Baoliu Ye、Sanglu Lu、Cam-Tu Nguyen。
- **方向与内容：** 云网络系统；研究借助异构平台加快网络功能的部署；由于本次未取得可核对的公开摘要，此句仅概括题名。

### 22. [Corporate Fraud Detection in Rich-yet-Noisy Financial Graph](https://arxiv.org/abs/2502.19305)

- **发表情况：** 2025 年 arXiv 预印本；本次未核实到正式会议或期刊版本。
- **作者：** Shiqi Wang、Zhibo Zhang、Libing Fang、Cam-Tu Nguyen、Wenzhong Li。
- **方向与内容：** 金融图学习；针对企业关系图中的噪声节点和漏标欺诈，结合知识图谱表示与鲁棒两阶段图卷积进行识别。

## 2024 年

### 23. [Mitigating the Impact of False Negative in Dense Retrieval with Contrastive Confidence Regularization](https://ojs.aaai.org/index.php/AAAI/article/view/29885)

- **发表情况：** AAAI 2024 正式论文，38(17):19171–19179。
- **作者：** Shiqi Wang、Yeqin Zhang、Cam-Tu Nguyen。
- **方向与内容：** 稠密检索；通过对比置信正则化和噪声负例过滤，缓解相关文档被误当负样本的问题。

### 24. [Reward Difference Optimization For Sample Reweighting In Offline RLHF](https://aclanthology.org/2024.findings-emnlp.115/)

- **发表情况：** Findings of EMNLP 2024 正式论文，2109–2123；[arXiv 版本](https://arxiv.org/abs/2408.09385)属于同一研究。
- **作者：** Shiqi Wang、Zhengze Zhang、Rui Zhao、Fei Tan、Cam Tu Nguyen。
- **方向与内容：** LLM 对齐 / 离线 RLHF；预测两条回答之间的奖励差距，并据此为偏好训练样本赋权。

### 25. [Retrospex: Language Agent Meets Offline Reinforcement Learning Critic](https://aclanthology.org/2024.emnlp-main.268/)

- **发表情况：** EMNLP 2024 主会正式论文，4650–4666。
- **作者：** Yufei Xiang、Yiqun Shen、Yeqin Zhang、Cam-Tu Nguyen。
- **方向与内容：** LLM Agent / 强化学习；训练离线 RL Critic 从既往交互中评估动作价值，并用于重新排序 Agent 决策。

### 26. [Sample Efficiency Matters: Training Multimodal Conversational Recommendation Systems in a Small Data Setting](https://doi.org/10.1145/3664647.3681217)

- **发表情况：** ACM Multimedia 2024 正式论文，2223–2232。
- **作者：** Haoyang Su、Wenzhe Du、Xiaoliang Wang、Cam-Tu Nguyen。
- **方向与内容：** 多模态对话推荐；通过对话状态编码、半监督学习和图文对齐，在少量标注对话数据下训练推荐系统。

### 27. [CyberStar: Simple, Elastic and Cost-Effective Network Functions Management in Cloud Network at Scale](https://www.usenix.org/conference/atc24/presentation/xu-tingting)

- **发表情况：** USENIX ATC 2024 正式论文，227–246。
- **作者：** Tingting Xu、Bengbeng Xue、Yang Song、Xiaomin Wu、Xiaoxin Peng、Yilong Lyu、Xiaoliang Wang、Chen Tian、Baoliu Ye、Camtu Nguyen、Biao Lyu、Rong Wen、Zhigang Zong、Shunmin Zhu。
- **方向与内容：** 云网络功能管理；通过三级架构、资源池和按需分配，支持弹性且低成本的大规模网络功能服务。

### 28. [EdgeCross: Cloud Scale Traffic Management at Peering Edges](https://cs.nju.edu.cn/tianchen/lunwen/2024/conext24-xiaoliang.pdf)

- **发表情况：** *Proceedings of the ACM on Networking* 2(CoNEXT4), Article 24（2024）；与 CoNEXT 2024 相关。
- **作者：** Xiaoliang Wang、Penghui Mi、Yong Zhu、Baoyi An、Yinhua Wang、Lixiang Wang、Xuezhi Yu、Qiong Xie、Xiang Huang、Mingliang Yin、Chaoyang Ji、Wei Sun、Yihang Lv、Yuhang Chen、Cam-Tu Nguyen、Chen Tian、Xiaoming Fu。
- **方向与内容：** 云网络流量调度；在满足不同应用时延需求的同时，降低云平台对等互联边缘的带宽成本。

### 29. [Mixed Preference Optimization: Reinforcement Learning with Data Selection and Better Reference Model](https://arxiv.org/abs/2403.19443)

- **发表情况：** 2024 年 arXiv 首发、2025 年修订；本次未核实到正式会议或期刊版本。
- **作者：** Qi Gou、Cam-Tu Nguyen。
- **方向与内容：** LLM 对齐；先在易区分的偏好样本上进行 DPO，再以所得模型为参照对困难样本进行在线 RLHF。

### 30. [SynthDoc: Bilingual Documents Synthesis for Visual Document Understanding](https://arxiv.org/abs/2408.14764)

- **发表情况：** 2024 年 arXiv 预印本；本次未核实到正式会议或期刊版本。
- **作者：** Chuanghao Ding、Xuejing Liu、Wei Tang、Juan Li、Xiaoliang Wang、Rui Zhao、Cam-Tu Nguyen、Fei Tan。
- **方向与内容：** 视觉文档理解 / 数据合成；生成含文本、图片、表格和图表的双语文档数据，缓解文档模型训练数据不足。

## 研究方向与脉络

| 方向 | 具体研究内容 | 对应论文 |
| --- | --- | --- |
| **信息检索、RAG 与文本表示** | 稠密检索的假负例、多跳检索、数据库 schema routing、文档结构辅助检索与生成，以及 LLM 向量的语义质量和压缩效率。 | 1、2、3、4、13、18、23 |
| **大模型推理与部署效率** | KV cache 淘汰与补偿、小大模型协作、解码加速、注意力温度调节，以及模型服务架构。 | 5、7、10、15、16、19 |
| **Agent、长期记忆与 AI for AI** | 从离线经验改进 Agent 行动、评测长期多源记忆，以及评测模型编写机器学习算法的能力。 | 12、14、25 |
| **多模态理解与可靠性** | 图文统一检索、视觉语言模型幻觉检测、气象图理解、双语视觉文档数据合成和少样本对话推荐。 | 6、8、11、26、30 |
| **模型对齐与蒸馏** | DPO、RLHF 的偏好样本选择与赋权，以及将大模型的对话能力蒸馏给小模型。 | 17、24、29 |
| **AI 系统与计算机网络** | 网络内梯度聚合资源调度、云网络功能弹性部署、云边缘流量管理。 | 9、20、21、27、28 |
| **领域图学习** | 在有噪声的金融关系图中识别企业欺诈。 | 22 |

**整体观察：** 从 2024 年的检索鲁棒性、对话推荐和对齐研究，到 2025—2026 年的 LLM 文本表示、推理效率、Agent 记忆与多模态检索，可以看到“让大模型更会检索、更省资源、更可靠”这一主线；云网络和网络内计算是并行的系统合作方向。她的[招生研究方向说明](https://ai.nju.edu.cn/CamTuNguyen/)还明确列出信息检索 / RAG、训练与推理效率、AI for Scientific Discovery；其中 AI for Scientific Discovery 目前可由 MLAlgo-Bench 等工作体现，但不能把所有系统合作论文直接归为该方向。

## 资料核查说明

- 作者与发表记录主要交叉核对了 [ACL Anthology 作者页](https://aclanthology.org/people/cam-tu-nguyen/)、[DBLP 作者页](https://dblp.org/pid/14/5079.html)、[导师主页](https://ai.nju.edu.cn/CamTuNguyen/)及各论文链接。ACL Anthology 和 DBLP 的收录会滞后，因此另查了 PMLR、AAAI、NeurIPS、USENIX、CVPR 项目页和合作者页面。
- **“arXiv 预印本”不等于正式发表；“已录用”也不等于已经有可核对的正式论文集版本。** 所有一行主题概括依据论文摘要；第 10、11、21 项因缺少可核对的公开摘要或完整会议页，明确限定了概括依据。
- 作者姓名按所链接原始来源保留英文拼写和顺序；同一人的 Cam-Tu、Cam Tu、Camtu 与 Nguyen Cam-Tu 写法在不同出版社页面上确有差异。
