from pathlib import Path
import json,re,sys,importlib.util

ROOT=Path(__file__).resolve().parents[1]
spec=importlib.util.spec_from_file_location('library',Path(__file__).with_name('build_library.py'))
lib=importlib.util.module_from_spec(spec);spec.loader.exec_module(lib)

def status(e):
    if e.get('verification'):return e['verification'][0]
    c=e.get('author_comments','');j=e.get('journal_reference','')
    if j:return '原始页面给出期刊记录：'+j+'（本次未另核出版社）'
    venues=re.findall(r'(?:Accepted (?:at|by|to)\s*)?(?:ICLR|ICML|NeurIPS|NIPS|MLSys|SOSP|OSDI|ACL|EMNLP|COLM)\s*\'?\s*(?:20)?\d{2}',c,re.I)
    if venues:return '作者arXiv备注标注：'+'；'.join(venues)+'；未独立核对正式论文集'
    return '已核实可读全文；本次未独立确认正式发表状态，不据此断言未发表'

def load():
    items=json.loads((ROOT/'metadata.json').read_text(encoding='utf-8'))
    lib.seed()
    seeds={e['id']:e for e in json.loads((ROOT/'papers.json').read_text(encoding='utf-8'))}
    for e in items:
        old=e.get('local_pdf')
        for k in ['priority','topic','why','focus','question','verification']:e[k]=seeds[e['id']].get(k)
        if old:
            target=ROOT/e['direction']/lib.FOLDERS[e['priority']]/Path(old).name
            current=ROOT/old
            if target!=current:
                assert ROOT in target.resolve().parents and ROOT in current.resolve().parents
                target.parent.mkdir(exist_ok=True,parents=True)
                if target.exists():raise FileExistsError(target)
                current.rename(target)
                e['local_pdf']=target.relative_to(ROOT).as_posix()
        txt=ROOT/'_全文文本'/(e['id']+'.txt')
        if txt.exists():
            t=txt.read_text(encoding='utf-8',errors='replace')
            m=re.search(r'arXiv:\s*([\d.]+v\d+)',t[:12000])
            if m:
                e['downloaded_arxiv_version']=m.group(1)
                e['version_pdf_url']='https://arxiv.org/pdf/'+m.group(1)
        e['publication_status']=status(e)
    return sorted(items,key=lambda x:x['id'])

def bib(e):
    yr=re.search(r'\d{4}',e.get('date',''))
    authors=' and '.join(e.get('authors',[]))
    def esc(s):return s.replace('&',r'\&').replace('%',r'\%').replace('_',r'\_')
    fields=[('title','{'+esc(e.get('title',e['short']))+'}'),('author',esc(authors)),('year',yr.group() if yr else 'n.d.'),('url',e['source'])]
    if e.get('arxiv_id'):fields.extend([('eprint',e['arxiv_id']),('archivePrefix','arXiv')])
    fields.append(('note','Reading library checked 2026-10-27; metadata follows downloaded source version'))
    return '@misc{'+e['id']+'_'+e['short']+',\n'+',\n'.join('  '+k+' = {'+v+'}' for k,v in fields)+'\n}\n'

def render(items):
    for direction in ['01-大模型高效推理','02-可靠Agent与Agent学习']:
        entries=[e for e in items if e['direction']==direction]
        d=ROOT/direction;d.mkdir(exist_ok=True,parents=True)
        name=direction[3:]
        lines=[f'# {name}：论文目录与阅读卡','',
               '核查日期：2026-10-27。A 是第一轮核心阅读，B 按子方向选择，C 用于近期查新；优先级针对你的当前阶段，不是论文质量排名。','',
               f'本方向收录 {len(entries)} 篇，已取得 {sum(e.get("download_status")=="downloaded" for e in entries)} 份PDF。先读同目录 README 中指定的顺序。','',
               '## 使用与证据说明','',
               '- “正式论文集已核对”“作者页面标注”“未独立确认状态”是不同证据等级；arXiv首发年份与会议年份可能不同。',
               '- PDF主要采用作者公开的arXiv版本，少数采用正式会议版。会议身份已确认不代表所下载文件必为最终会议版。',
               '- 标题、作者和首发日期取自原始页面；版本取自PDF可识别的arXiv标记。作者与标题有版本差异时，以实际阅读版本为准。',
               '- 选题建议依据摘要、关键机制与对照阅读关系；未逐篇完成全文精读或复现实验，不将作者报告的性能视为独立验证结论。',
               '- 近期论文C中含未完成正式发表核查的预印本；纳入依据是问题直接相关、方法可分析，不能将其一律称为顶会高质量论文。','',
               '## 总目录','',
               '| 编号 | 层级 | 短名 | 主题 | 原始页面首发日期 | 全文 |','| --- | --- | --- | --- | --- | --- |']
        for e in entries:
            link='[PDF]('+Path(e['local_pdf']).relative_to(direction).as_posix()+')' if e.get('local_pdf') else '[原页]('+e['source']+')'
            lines.append(f"| {e['id']} | {e['priority']} | {e['short']} | {e['topic']} | {e.get('date','待核')} | {link} |")
        for level in ['A','B','C']:
            lines+=['',f'## {level}：{lib.FOLDERS[level][3:]}','']
            for e in [x for x in entries if x['priority']==level]:
                authors=e.get('authors',[])
                shortauthors='；'.join(authors[:4])+(' 等' if len(authors)>4 else '')
                lines += [f"### {e['id']} · {e['title']}",'',
                          f"- **作者：** {shortauthors or '见原文'}。完整作者元数据见目录中的 metadata.json。",
                          f"- **首发日期：** {e.get('date','未提取')}；这是原始页面日期，不自动等同于正式发表日期。",
                          f"- **发表核查：** {e['publication_status']}。",
                          f"- **原始页面：** [{e['short']}]({e['source']})。"]
                if e.get('verification') and e['verification'][1]!=e['source']:lines.append(f"- **状态依据：** [会议／作者原始来源]({e['verification'][1]})。")
                if e.get('local_pdf'):
                    relative=Path(e['local_pdf']).relative_to(direction).as_posix()
                    lines.append(f"- **本地全文：** [{Path(relative).name}]({relative})。")
                else:lines.append('- **本地全文：** 未成功取得，保留原始入口；详见下载核验报告。')
                if e.get('downloaded_arxiv_version'):lines.append(f"- **下载版本：** [{e['downloaded_arxiv_version']}]({e['version_pdf_url']})。")
                if e.get('code_links'):lines.append('- **原页关联仓库：** '+'；'.join('[仓库'+str(i+1)+']('+u+')' for i,u in enumerate(e['code_links'][:2]))+'。仅作入口，未验证代码可运行。')
                lines += [f"- **为什么读：** {e['why']}",f"- **重点看：** {e['focus']}",
                          f"- **读完要回答：** {e['question']}",
                          '- **阅读方式：** 第一遍看问题、方法图和实验设置；第二遍围绕上面的问题读方法与消融。先不逐行复现全部代码。','']
        (d/'论文目录与阅读卡.md').write_text('\n'.join(lines),encoding='utf-8')
        (d/'references.bib').write_text('\n'.join(bib(e) for e in entries),encoding='utf-8')
        (d/'metadata.json').write_text(json.dumps(entries,ensure_ascii=False,indent=2),encoding='utf-8')
    (ROOT/'metadata.json').write_text(json.dumps(items,ensure_ascii=False,indent=2),encoding='utf-8')
    downloaded=[e for e in items if e.get('download_status')=='downloaded']
    lines=['# 下载与全文核验报告','', '日期：2026-10-27。核验的是文件完整性和标题关联，不是论文结论的复现。','',
           f'- 书目数：{len(items)}。',f'- PDF成功数：{len(downloaded)}。',
           f'- PDF总大小：{sum(e.get("bytes",0) for e in downloaded)/1024**2:.1f} MiB。',
           f'- 可提取正文的PDF：{sum(bool(e.get("text_extraction_ok")) for e in downloaded)}。','',
           '逐项记录原始来源、下载URL、字节数、SHA-256和可识别的arXiv版本；详情见 metadata.json。下载失败不计入成功数。','',
           '| 编号 | 下载 | 正文提取 | 字节数 | 版本 |','| --- | --- | --- | --- | --- |']
    for e in items:lines.append(f"| {e['id']} | {e.get('download_status')} | {e.get('text_extraction_ok',False)} | {e.get('bytes',0)} | {e.get('downloaded_arxiv_version','非arXiv或未识别')} |")
    lines+=['','## 范围与限制','',
            'PDF只从公开作者稿或会议入口获取，未修改原论文。通过PDF文件头、最小大小、文本提取和标题对应检查排除下载到网页或明显损坏的情况；这不等同于逐页视觉检查。',
            '来源快照位于 _来源快照，全文提取文本位于 _全文文本。它们是核验辅助文件，阅读时从两个方向的README进入即可。',
            '本库以2026-10-27为查新截止日；不声称穷尽所有论文。近期预印本的正式发表、代码可用性和独立复现情况需要持续更新。']
    (ROOT/'下载与核验报告.md').write_text('\n'.join(lines),encoding='utf-8')

if __name__=='__main__':render(load())
