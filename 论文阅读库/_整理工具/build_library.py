from pathlib import Path
import json, re, html, urllib.request, time, hashlib, subprocess
from concurrent.futures import ThreadPoolExecutor, as_completed

ROOT = Path(__file__).resolve().parents[1]
DATE = '2026-10-27'
# id, short name, source, priority, topic, selection rationale, reading focus, question
E = [
('E01','InferenceSurvey','2407.12391','A','总体地图','先建立推理系统全貌，避免把效率等同于某个技巧。','分类图、请求生命周期、不同层次的瓶颈；旧综述不能替代2026查新。','用自己的话区分算法、内存、算子与调度优化。'),
('E02','Transformer','1706.03762','A','模型基础','理解QKV与注意力，后面的缓存和解码都依赖它。','注意力公式、因果mask、残差；原文是encoder-decoder结构。','画出decoder-only生成一次token时的主要张量。'),
('E03','FlashAttention','2205.14135','A','算子与IO','学习为何减少数据搬运比仅减少FLOPs更重要。','分块、online softmax、HBM/SRAM；先看机制图，再看证明。','为什么它不是删掉注意力连接，速度收益受什么限制？'),
('E04','PagedAttention','2309.06180','A','缓存与服务','理解vLLM背后的缓存管理与并发服务问题。','块表、内存浪费、共享与调度；注意吞吐实验的负载。','分页管理与语义KV淘汰的区别是什么？'),
('E05','SpeculativeDecoding','2211.17192','A','解码加速','大小模型协作和无损解码的重要起点。','草稿、批量验证、接受与校正条件、成本模型。','接受率很高为什么仍可能没有端到端加速？'),
('E06','AWQ','2306.00978','A','模型量化','用一篇代表论文理解低比特权重量化与硬件落地。','显著权重、激活统计、校准、实际内核和速度。','权重缩小四倍是否意味着生成快四倍？'),
('E07','STARS','2605.26733','A','循环与计算分配','与你已参与的研究直接衔接，应掌握到可独立解释。','稳定性与有效性、正则项、随机循环、质量随深度变化。','稳定但错误的样本是否存在，怎样量化？'),
('E08','TestTimeCompute','2408.03314','A','计算预算','学习在同一预算下比较搜索、验证与计算分配。','问题难度、compute-optimal策略、预算口径与oracle信息。','换成你能部署的难度估计后，最优策略还成立吗？'),
('E09','GQA','2305.13245','B','缓存与架构','解释KV头数怎样影响缓存规模与模型质量。','MHA/MQA/GQA关系、uptraining与质量效率权衡。','为什么不能直接改头数配置就保证模型无损？'),
('E10','GPTQ','2210.17323','B','模型量化','与AWQ形成方法对照，补齐PTQ核心思路。','逐层量化、误差补偿、校准数据和硬件假设。','GPTQ与AWQ优化的是同一件事吗？'),
('E11','H2O','2306.14048','B','KV压缩','理解基于重要token的KV淘汰经典思路。','heavy hitters、保留策略、长上下文任务与成本。','当前重要的token是否一定对未来查询重要？'),
('E12','SnapKV','2404.14469','B','KV压缩','与H2O比较观察窗口和输入侧选择假设。','prompt末端观察、按头选择、长输出和跨任务限制。','观察窗口变化时，哪些任务最易失效？'),
('E13','SGLang','2312.07104','B','服务与程序执行','把结构化多次调用与前缀复用联系起来。','RadixAttention、结构化程序、共享前缀与实际负载。','有大量共享前缀和随机请求时收益如何变化？'),
('E14','FlashInfer','2501.01005','B','算子工程','从单一注意力优化走向可组合的服务kernel。','统一表示、可定制内核、负载与调度；系统分支选读。','kernel微基准改善是否能转化为系统收益？'),
('E15','Ouro','2510.25741','B','循环与计算分配','STARS和动态退出的骨干背景，先理解模型再读改进。','共享层循环、退出目标、循环KV与真实运行。','参数效率、计算效率和内存效率有何不同？'),
('E16','LAVa','2509.09754','B','组内KV压缩','导师组内工作的直接衔接点。','层和头动态预算、信息损失度量、不同任务类型。','动态层预算与动态头预算分别在哪些任务有用？'),
('E17','SmallKV','2508.02751','B','组内KV压缩','理解小模型辅助大模型缓存压缩的另一种路径。','跨模型注意力匹配、边缘token补偿、额外模型成本。','省下的缓存与新增的小模型资源怎样一起核算？'),
('E18','TrigReason','2604.14847','B','组内计算分配','与Agent的选择性介入和预算决策也有关联。','三类触发、干预对象、强基线和真实延迟。','触发器是检测到困难，还是只是与困难相关？'),
('E19','TurboQuant','2504.19874','B','近期量化','2026正式会议方向样本，练习阅读理论与实际压缩的差别。','失真目标、随机变换、元数据与基线；同时检查相关工作。','理论向量失真保证能否直接推出所有任务无损？'),
('E20','Strata','https://www.usenix.org/conference/osdi26/presentation/xie-zhiqiang','C','近期服务系统','2026正式系统论文，补齐分层上下文缓存的新进展。','GPU/CPU/SSD层次、预取、调度、真实系统负载。','分层缓存何时受传输限制，何时受存储限制？'),
('E21','VeriCache','2605.17613','C','近期缓存与验证','把有损缓存用于草稿、完整缓存用于验证，连接两条效率路线。','精确性条件、swap重叠、验证成本和长生成。','相同输出的保证依赖哪些执行与采样条件？'),
('E22','ContinuousDepthBatching','2608.09444','C','近期循环服务','防止把少循环直接等同于服务加速。','循环间重组batch、KV布局、退出分布与吞吐。','你的退出策略在并发服务时会怎样改变收益？'),
('E23','RecurTrace','2609.03379','C','近期循环学习','自适应退出与循环轨迹利用的直接竞争工作。','循环记忆、halting监督、同预算基线、训练附录。','与STARS的稳定性目标相比，改进来源怎样区分？'),
('E24','TAPS','2609.36653','C','近期循环调节','提醒你动态控制不只有退出深度，还包括更新步长。','进展与波动分解、步长控制、理论假设、适用模型。','收益来自更少循环还是更好的单步更新？'),
('E25','DynamicComputation','2610.09013','C','近期循环实现','2026年10月的直接查新对象，关注实际跳过计算。','best-available KV、退出先验、训练推理一致性。','选出了退出深度后，哪些计算仍然不得不执行？'),
('E26','MonitoringLoopedLM','2610.18127','C','近期机制分析','2026年10月研究，避免重复已有内部行为分析。','carry/re-read结构、检查协议、模型家族和扰动。','哪些发现跨架构成立，哪些只对一种骨干成立？'),
]
A = [
('A01','ReAct','2210.03629','A','Agent基础','用经典论文建立观察—行动闭环。','交替推理行动、环境反馈、基线和失败例。','怎样区分模型决策错误与工具环境故障？'),
('A02','SelfRefine','2303.17651','A','反馈修复','理解任务内自反馈修复的基本结构。','生成、反馈、修订；任务差异与额外调用成本。','同预算独立重试是否也能得到同样收益？'),
('A03','Reflexion','2303.11366','A','经验与反思','区分当次修复与跨尝试保存文字经验。','反馈来源、反思存储、重试设置；不是权重RL。','经验如何影响下一次尝试，错误经验会怎样传播？'),
('A04','SelfCorrectionLimits','2310.01798','A','可靠性与反证','必须与积极修复论文对照阅读，学习条件边界。','intrinsic self-correction的定义、任务与提示控制。','论文否定的是哪类自纠错，不能泛化到哪些外部反馈？'),
('A05','Tau2Bench','2506.07982','A','执行评测','学会用环境状态而非自述判断任务成功。','双控制、用户模拟器、成功标准与重复运行。','模拟用户本身的误差会怎样影响结论？'),
('A06','Retrospex','https://aclanthology.org/2024.emnlp-main.268/','A','组内经验学习','与你的导师组和Agent学习直接相关。','离线critic、动作重评分、环境和轨迹数据。','直接检索经验与训练critic各自需要什么证据？'),
('A07','DPO','2305.18290','B','训练与偏好','理解示范、偏好与在线RL不是一回事。','目标函数直觉、reference、成对数据和训练假设。','偏好更高的轨迹是否真的执行更正确？'),
('A08','LongMemEval','2410.10813','A','记忆评测','用一个明确基准学习记忆任务、数据和评价协议。','五类能力、历史规模、检索与阅读、评价脚本。','记忆QA提高能否证明行动任务也提高？'),
('A09','PPO','1707.06347','B','RL基础','进入Agent RL前理解策略优化与优势的经典起点。','clipped objective、优势估计、采样与更新；不先背公式。','为什么限制更新，奖励尺度和采样怎样影响稳定性？'),
('A10','InstructGPT','2203.02155','B','后训练基础','理解SFT、偏好数据、奖励模型与RLHF完整链。','数据来源、三阶段训练、评价与对齐取舍。','人类偏好与可执行任务奖励有哪些差别？'),
('A11','DeepSeekR1','2501.12948','B','可验证奖励','理解reasoning中RL的代表性路线与训练阶段。','R1-Zero与R1区别、冷启动、奖励和蒸馏。','单轮可验证答案训练迁移到多轮Agent还缺什么？'),
('A12','SCoRe','2409.12917','B','训练自纠错','与不训练的Self-Refine、反证论文建立三方比较。','多轮训练目标、分布偏移、修好与改坏的对照。','训练怎样防止只会第一次答对而不学真正修复？'),
('A13','TauBench','2406.12045','B','执行评测','作为tau2前作，理解工具、规则与用户交互。','政策遵循、数据库结果、pass^k与多次稳定性。','一次成功率与重复全部成功的指标怎样不同？'),
('A14','SWEBench','2310.06770','B','执行评测','了解执行测试如何用于复杂代码任务评价。','真实issue、测试、环境复现、数据与泄漏限制。','测试通过是否足以代表真实需求全部满足？'),
('A15','LifeBench','2603.03781','B','组内长期记忆','组内直接相关；从显式事实走向多源流程和习惯。','事件生成、长时序、多源一致性、评测和人工审核。','合成数据的一致性与真实世界有效性如何区分？'),
('A16','AgentGymRL','2509.08755','B','近期Agent训练','2026正式会议工作，了解多轮RL训练框架和交互长度。','环境接口、训练稳定性、ScalingInter-RL与数据划分。','逐步增加交互时域为什么可能改变探索与坍塌？'),
('A17','RAGEN','2504.20073','B','Agent训练诊断','学习多轮RL为何失败、如何诊断而非只运行训练。','环境设计、训练坍塌、奖励与策略行为。','日志中哪些信号能区分真实学习与投机？'),
('A18','AgentLightning','2508.03680','B','Agent训练系统','理解运行Agent与训练接口解耦的工程问题。','轨迹结构、信用分配、执行与训练解耦。','已有Agent框架接入后，谁定义动作和奖励？'),
('A19','ACE','2510.04618','B','上下文与经验','2026正式会议方向样本；区分上下文更新和权重更新。','增量playbook、生成反思整理、消融与成本。','经验库增长后，冲突、冗余与错误如何管理？'),
('A20','LetsVerify','2305.20050','B','过程验证','学习结果监督和过程监督的差别。','步骤标签、奖励模型、评价独立性和成本。','数学步骤验证怎样迁移到工具Agent，哪些地方不成立？'),
('A21','MTBenchJudge','2306.05685','B','评估器可靠性','理解LLM-as-judge的偏差，避免生成器给自己证明。','位置、冗长、自偏好等评价偏差及人评对照。','更换judge或输出顺序后排名是否稳定？'),
('A22','LongMemEvalV2','2605.12493','C','近期记忆行动','把聊天回忆推进到定制环境中的经验能力。','任务设计、经验形成、底座与RAG基线、迁移。','记忆带来的收益是否来自更多上下文或更强底座？'),
('A23','MemCalib','2609.24259','C','近期记忆校准','2026年9月首发、10月修订，与你的可靠记忆问题直接相邻。','过度/不足使用、原子命题、反事实归因和训练评价。','忽略噪声与利用必要经验怎样同时优化？'),
('A24','ImageRSI','2610.32120','C','近期视觉修复','2026年10月23日首发，是RISA后续必须比较的近邻。','任务修复、经验准入、judge更新；不要把标题当成强RSI证明。','哪些修改持久保留，是否改善未见任务及后续改进？'),
('A25','DolphinBench','2609.24971','C','近期行动记忆评测','任务完成、费用与延迟共同评价记忆的近期入口。','任务依赖历史的验证、执行评分、完整成本。','高准确率是否以不现实的检索或调用成本换来？'),
('A26','AgentLightningV1','2608.17528','C','近期Agent训练系统','与2025原作形成版本对照，不把库升级当方法贡献。','harness、rollout、执行隔离与训练接口的新增内容。','对比旧版本，新增机制解决了什么可测失败？'),
('A27','CRITIC','2305.11738','A','外部反馈验证','与自反馈和自纠错局限对照，外部证据是可靠Agent的关键。','工具交互、验证再修订、外部反馈与额外预算。','控制工具与调用预算后，什么反馈最能带来修复收益？'),
]

VERIFIED = {
'E02':('NeurIPS/NIPS 2017，正式论文集已核对','https://proceedings.neurips.cc/paper_files/paper/2017/hash/3f5ee243547dee91fbd053c1c4a845aa-Abstract.html'),
'E03':('NeurIPS 2022，正式论文集已核对','https://proceedings.neurips.cc/paper_files/paper/2022/hash/67d57c32e20fd0a7a302cb81d36e40d5-Abstract-Conference.html'),
'E06':('MLSys 2024，正式论文集已核对','https://proceedings.mlsys.org/paper_files/paper/2024/hash/42a452cbafa9dd64e9ba4aa95cc1ef21-Abstract-Conference.html'),
'E07':('ICML 2026，正式论文集已核对','https://proceedings.mlr.press/v306/yang26t.html'),
'E16':('Findings of EMNLP 2025，正式论文集已核对','https://aclanthology.org/2025.findings-emnlp.737/'),
'E17':('NeurIPS 2025，正式论文集已核对','https://papers.neurips.cc/paper_files/paper/2025/hash/45790132b9f91b5787232e1cbe0712fc-Abstract-Conference.html'),
'E18':('Findings of ACL 2026，正式论文集已核对','https://aclanthology.org/2026.findings-acl.333/'),
'E19':('ICLR 2026：Google Research官方页面标注；本次未独立核对论文集','https://research.google/blog/turboquant-redefining-ai-efficiency-with-extreme-compression/'),
'E20':('OSDI 2026，USENIX正式论文页已核对','https://www.usenix.org/conference/osdi26/presentation/xie-zhiqiang'),
'A05':('ICML 2026：作者报告页标注；可下载全文采用arXiv','https://victorbarres.github.io/assets/html/tau2-bench-icml2026-oral.html'),
'A02':('NeurIPS 2023，正式论文集已核对','https://proceedings.neurips.cc/paper_files/paper/2023/hash/91edff07232fb1b55a505a9e9f6c0ff3-Abstract-Conference.html'),
'A03':('NeurIPS 2023，正式论文集已核对；arXiv与会议版作者表有差异，以所读版本为准','https://proceedings.neurips.cc/paper_files/paper/2023/hash/1b44b878bb782e6954cd888628510e90-Abstract-Conference.html'),
'A04':('ICLR 2024，正式论文集已核对','https://proceedings.iclr.cc/paper_files/paper/2024/hash/8b4add8b0aa8749d80a34ca5d941c355-Abstract-Conference.html'),
'A06':('EMNLP 2024，正式论文集已核对','https://aclanthology.org/2024.emnlp-main.268/'),
'A07':('NeurIPS 2023，正式论文集已核对','https://proceedings.neurips.cc/paper_files/paper/2023/hash/a85b405ed65c6477a4fe8302b5e06ce7-Abstract.html'),
'A08':('ICLR 2025，正式论文集已核对','https://proceedings.iclr.cc/paper_files/paper/2025/file/d813d324dbf0598bbdc9c8e79740ed01-Paper-Conference.pdf'),
'A12':('ICLR 2025，正式论文集已核对','https://proceedings.iclr.cc/paper_files/paper/2025/hash/871ac99fdc5282d0301934d23945ebaa-Abstract-Conference.html'),
'A16':('ICLR 2026：正式论文检索页及作者仓库确认；Oral仅据作者仓库','https://github.com/woooodyy/AgentGym-RL'),
'A19':('ICLR 2026：正式下载目录及作者项目页确认','https://ace-agent.github.io/'),
}

def seed():
    entries=[]
    for direction, rows in [('01-大模型高效推理',E),('02-可靠Agent与Agent学习',A)]:
        for row in rows:
            ident,short,src,level,topic,why,focus,question=row
            url=src if src.startswith('http') else 'https://arxiv.org/abs/'+src
            entries.append(dict(id=ident,short=short,source=url,arxiv_id=None if src.startswith('http') else src,
                priority=level,topic=topic,why=why,focus=focus,question=question,direction=direction,
                verification=VERIFIED.get(ident)))
    ROOT.mkdir(parents=True,exist_ok=True)
    (ROOT/'papers.json').write_text(json.dumps(entries,ensure_ascii=False,indent=2),encoding='utf-8')

def fetch(url,timeout=75):
    req=urllib.request.Request(url,headers={'User-Agent':'ResearchReadingLibrary/1.0 (personal academic literature reading)'})
    with urllib.request.urlopen(req,timeout=timeout) as r:
        return r.read(),r.geturl(),r.headers.get('Content-Type','')

def clean(s):
    return re.sub(r'\s+',' ',html.unescape(re.sub('<[^>]+>',' ',s))).strip()

def metadata(body,url):
    s=body.decode('utf-8',errors='replace')
    metas={}
    for tag in re.findall(r'<meta\b[^>]*>',s,re.I):
        attrs=dict((k.lower(),html.unescape(v)) for k,q,v in re.findall(r'([\w:-]+)\s*=\s*([\x22\x27])(.*?)\2',tag,re.S))
        k=attrs.get('name') or attrs.get('property')
        if k: metas.setdefault(k.lower(),[]).append(attrs.get('content',''))
    def get(k,default=''): return metas.get(k,[default])[0]
    title=get('citation_title') or get('dc.title') or get('og:title')
    if not title:
        m=re.search(r'<title>(.*?)</title>',s,re.S|re.I)
        title=clean(m.group(1)) if m else ''
    title=re.sub(r'^\[\d{4}\.\d+\]\s*','',title).replace(' | USENIX','')
    abstract=''
    m=re.search(r'<blockquote[^>]*class="abstract[^>]*>(.*?)</blockquote>',s,re.S)
    if m: abstract=re.sub(r'^Abstract:\s*','',clean(m.group(1)))
    comments=''; journal=''
    for label,key in [('Comments:','comments'),('Journal reference:','journal')]:
        m=re.search(re.escape(label)+r'.*?<td[^>]*>(.*?)</td>',s,re.S)
        if m:
            if key=='comments': comments=clean(m.group(1))
            else: journal=clean(m.group(1))
    authors=metas.get('citation_author',[]) or metas.get('dc.creator',[])
    date=get('citation_date') or get('citation_publication_date') or get('dc.date')
    pdf=get('citation_pdf_url')
    links=[]
    for href in re.findall(r'href=[\x22\x27]([^\x22\x27]+)',s):
        if 'github.com/' in href and not any(x in href for x in ['arXiv','arxiv','github.com/notifications']): links.append(html.unescape(href))
    return dict(title=clean(title),authors=authors,date=date,abstract=abstract,author_comments=comments,
                journal_reference=journal,pdf_url=pdf,code_links=list(dict.fromkeys(links))[:8],source_final=url)

FOLDERS={'A':'01-第一轮必读','B':'02-按分支选读','C':'03-近期前沿查新'}

def work(e):
    folder=ROOT/e['direction']/FOLDERS[e['priority']]
    folder.mkdir(parents=True,exist_ok=True)
    pdf=folder/f"{e['id']}_{e['short']}.pdf"
    ev=ROOT/'_来源快照';ev.mkdir(exist_ok=True)
    err=[]
    for attempt in range(3):
        try:
            data,final,ctype=fetch(e['source'],40)
            (ev/(e['id']+'.html')).write_bytes(data)
            m=metadata(data,final)
            if not m['title'] or 'Access Denied' in m['title']: raise ValueError('unusable metadata')
            e.update(m)
            break
        except Exception as ex:
            err.append('metadata: '+str(ex));time.sleep(3*(attempt+1))
    else:
        e['download_status']='metadata_failed';e['errors']=err;return e
    url=e.get('pdf_url')
    if e.get('arxiv_id'):
        # Fixed fetched version when arXiv exposes one; otherwise retain source URL and downloaded checksum.
        url=url or 'https://arxiv.org/pdf/'+e['arxiv_id']
    if not url:
        s=data.decode('utf-8',errors='replace')
        links=re.findall(r'href=[\x22\x27]([^\x22\x27]+\.pdf(?:\?[^\x22\x27]*)?)[\x22\x27]',s)
        links=[x for x in links if '/system/files/' in x or 'aclanthology.org/' in x]
        if links:
            from urllib.parse import urljoin
            url=urljoin(final,links[0])
    e['pdf_url']=url
    for attempt in range(3):
        try:
            if not url: raise ValueError('no public PDF link found')
            if pdf.exists() and pdf.read_bytes()[:5]==b'%PDF-':
                b=pdf.read_bytes();final_pdf=url
            else:
                b,final_pdf,ct=fetch(url,100)
                if not b.startswith(b'%PDF-') or len(b)<10000: raise ValueError('response is not valid-sized PDF')
                temp=pdf.with_suffix('.part');temp.write_bytes(b);temp.replace(pdf)
            e.update(download_status='downloaded',local_pdf=pdf.relative_to(ROOT).as_posix(),bytes=len(b),
                     sha256=hashlib.sha256(b).hexdigest(),pdf_final_url=final_pdf,fetched_on=DATE)
            break
        except Exception as ex:
            err.append('pdf: '+str(ex));time.sleep(3*(attempt+1))
    else: e['download_status']='pdf_failed'
    if err:e['errors']=err
    # Keep extracted text for title/page verification; no dependency installs.
    if e.get('download_status')=='downloaded':
        exe=Path(r'D:\MyDownload\Git\mingw64\bin\pdftotext.exe')
        if exe.exists():
            txt=ROOT/'_全文文本'/f"{e['id']}.txt";txt.parent.mkdir(exist_ok=True)
            r=subprocess.run([str(exe),'-layout','-enc','UTF-8',str(pdf),str(txt)],capture_output=True)
            if r.returncode==0:
                t=txt.read_text(encoding='utf-8',errors='replace')
                e['text_extraction_ok']=len(t)>500
                e['text_chars']=len(t)
                e['first_page_excerpt']=t.split('\f')[0][:2200]
            else:e['text_extraction_ok']=False
    return e

def download():
    src=json.loads((ROOT/'papers.json').read_text(encoding='utf-8'))
    results=[]
    with ThreadPoolExecutor(max_workers=2) as pool:
        jobs={pool.submit(work,e):e['id'] for e in src}
        for f in as_completed(jobs):
            e=f.result();results.append(e)
            print(e['id'],e.get('download_status'),e.get('title','')[:95],flush=True)
            (ROOT/'metadata.json').write_text(json.dumps(sorted(results,key=lambda x:x['id']),ensure_ascii=False,indent=2),encoding='utf-8')
    print('DONE',len(results),'PDF',sum(e.get('download_status')=='downloaded' for e in results),flush=True)

if __name__=='__main__':
    import sys
    if 'seed' in sys.argv: seed()
    if 'download' in sys.argv: download()
