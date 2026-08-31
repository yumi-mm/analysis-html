# -*- coding: utf-8 -*-
"""Export chart data from WebApp累计数据看板.html into an editable Excel workbook."""
from openpyxl import Workbook
from openpyxl.styles import Font, Alignment, Border, Side, PatternFill
from openpyxl.chart import LineChart, Reference, BarChart
from openpyxl.utils import get_column_letter

wb = Workbook()

header_fill = PatternFill("solid", fgColor="2B6CB0")
header_font = Font(bold=True, color="FFFFFF", size=11)
section_font = Font(bold=True, size=12, color="1A365D")
thin = Border(
    left=Side(style="thin", color="D0D5DD"),
    right=Side(style="thin", color="D0D5DD"),
    top=Side(style="thin", color="D0D5DD"),
    bottom=Side(style="thin", color="D0D5DD"),
)
center = Alignment(horizontal="center", vertical="center", wrap_text=True)
left = Alignment(horizontal="left", vertical="center", wrap_text=True)
note_font = Font(size=10, color="667085", italic=True)


def style_header(ws, row, cols):
    for c in range(1, cols + 1):
        cell = ws.cell(row=row, column=c)
        cell.fill = header_fill
        cell.font = header_font
        cell.alignment = center
        cell.border = thin


def style_body(ws, start_row, end_row, cols):
    for r in range(start_row, end_row + 1):
        for c in range(1, cols + 1):
            cell = ws.cell(row=r, column=c)
            cell.border = thin
            cell.alignment = center


def autosize(ws, widths):
    for i, w in enumerate(widths, 1):
        ws.column_dimensions[get_column_letter(i)].width = w


def add_smooth_line(ws, title, min_col, max_col, header_row, data_start, data_end, cat_col, anchor, height=9, width=15):
    chart = LineChart()
    chart.title = title
    chart.style = 10
    chart.height = height
    chart.width = width
    chart.legend.position = "b"
    data = Reference(ws, min_col=min_col, max_col=max_col, min_row=header_row, max_row=data_end)
    cats = Reference(ws, min_col=cat_col, min_row=data_start, max_row=data_end)
    chart.add_data(data, titles_from_data=True)
    chart.set_categories(cats)
    for s in chart.series:
        s.smooth = True
        s.marker.symbol = "circle"
        s.marker.size = 7
    ws.add_chart(chart, anchor)
    return chart


# ========== 目录 ==========
ws0 = wb.active
ws0.title = "目录说明"
ws0["A1"] = "测试组累计数据报表 · 作图数据（Excel可编辑版）"
ws0["A1"].font = Font(bold=True, size=16, color="1A365D")
ws0["A2"] = "来源：WebApp累计数据看板.html  |  统计周期：2026.05 – 2026.07  |  改表中数字后，嵌入的折线图会随之更新"
ws0["A2"].font = note_font
ws0.merge_cells("A1:D1")
ws0.merge_cells("A2:D2")

catalog = [
    ("Sheet名称", "对应HTML模块", "图表内容", "说明"),
    ("WebApp-用例Bug", "用例与Bug累计 · WebApp", "新增用例/通过率；当期Bug/修复率", "含完整版本明细表 + 两张折线图"),
    ("WebApp-Sentry", "Sentry", "发现问题/解决/待解决；崩溃率与LCP", "含版本明细 + 两张折线图"),
    ("WebApp-高优优化", "Sentry高优问题优化效果", "按版本优化前后影响量；问题明细", "含明细表 + 折线图/柱状图"),
    ("WebApp-线上事故", "线上事故 · WebApp", "新增事故/累计事故数", "含事故详情 + 折线图"),
    ("WebApp-UI自动化", "自动化 · WebApp UI", "人工回归/节省/累计效率提升%", "含明细表 + 折线图"),
    ("App-用例Bug", "用例与Bug累计 · App", "新增用例/通过率；当期Bug/修复率", "含完整版本明细 + 两张折线图"),
    ("App-线上事故", "线上事故 · App", "服务器/版本事故/累计", "含趋势表、详情 + 折线图"),
    ("App-埋点自动化", "自动化 · App埋点", "节省时长/累计效率提升%", "含明细表 + 折线图"),
]
for i, row in enumerate(catalog, 4):
    for j, v in enumerate(row, 1):
        ws0.cell(row=i, column=j, value=v)
    if i == 4:
        style_header(ws0, 4, 4)
    else:
        for j in range(1, 5):
            ws0.cell(row=i, column=j).border = thin
            ws0.cell(row=i, column=j).alignment = left if j > 1 else center
autosize(ws0, [18, 28, 42, 36])
ws0["A14"] = "使用提示：每个 sheet 上方是「作图用数据」；右侧/下方已嵌入 Excel 图，直接改数字即可编辑图表。"
ws0["A14"].font = note_font
ws0.merge_cells("A14:D14")

# ========== WebApp 用例 Bug ==========
ws = wb.create_sheet("WebApp-用例Bug")
ws["A1"] = "一、作图数据 · 用例趋势（对应 chart-case）"
ws["A1"].font = section_font
ws.merge_cells("A1:E1")

headers = ["版本", "迭代类型", "新增用例", "通过率(%)", "累计用例"]
for j, h in enumerate(headers, 1):
    ws.cell(row=2, column=j, value=h)
style_header(ws, 2, 5)

versions = [
    "20260508", "20260514", "20260520", "20260528", "20260611", "20260617",
    "20260625", "20260702", "20260708", "20260715", "20260722", "20260729",
]
caseMap = {
    "20260508": ("敏捷", None, None, 0),
    "20260514": ("敏捷", None, None, 0),
    "20260520": ("敏捷", None, None, 0),
    "20260528": ("标准", 1028, 86, 1028),
    "20260611": ("敏捷", None, None, 1028),
    "20260617": ("敏捷", None, None, 1028),
    "20260625": ("敏捷", None, None, 1028),
    "20260702": ("敏捷", None, None, 1028),
    "20260708": ("敏捷", None, None, 1028),
    "20260715": ("敏捷", None, None, 1028),
    "20260722": ("标准", 65, 87.6, 1093),
    "20260729": ("敏捷", None, None, 1093),
}
for i, v in enumerate(versions):
    t, newC, rate, cum = caseMap[v]
    r = 3 + i
    ws.cell(row=r, column=1, value=v)
    ws.cell(row=r, column=2, value=t)
    ws.cell(row=r, column=3, value=newC if newC is not None else 0)
    ws.cell(row=r, column=4, value=rate if rate is not None else 0)
    ws.cell(row=r, column=5, value=cum)
style_body(ws, 3, 14, 5)
add_smooth_line(ws, "WebApp · 用例趋势（新增用例 / 通过率）", 3, 4, 2, 3, 14, 1, "G2", width=16)

ws["A17"] = "二、作图数据 · Bug趋势（对应 chart-bug）"
ws["A17"].font = section_font
ws.merge_cells("A17:F17")
bug_headers = ["版本", "当期Bug", "已修复", "修复率(%)", "遗留", "累计Bug", "累计修复率(%)"]
for j, h in enumerate(bug_headers, 1):
    ws.cell(row=18, column=j, value=h)
style_header(ws, 18, 7)

bugMap = {
    "20260508": (0, 0, 100, 0, 0, 100),
    "20260514": (9, 9, 100, 0, 9, 100),
    "20260520": (134, 131, 97.7, 3, 143, 97.9),
    "20260528": (37, 40, 100, 0, 180, 100),
    "20260611": (0, 0, 100, 0, 180, 100),
    "20260617": (0, 0, 100, 0, 180, 100),
    "20260625": (5, 5, 100, 0, 185, 100),
    "20260702": (0, 0, 100, 0, 185, 100),
    "20260708": (2, 2, 100, 0, 187, 100),
    "20260715": (5, 5, 100, 0, 192, 100),
    "20260722": (28, 28, 100, 0, 220, 100),
    "20260729": (6, 6, 100, 0, 226, 100),
}
for i, v in enumerate(versions):
    cur, fixed, fixRate, remain, cum, cumFix = bugMap[v]
    r = 19 + i
    ws.cell(row=r, column=1, value=v)
    ws.cell(row=r, column=2, value=cur)
    ws.cell(row=r, column=3, value=fixed)
    ws.cell(row=r, column=4, value=fixRate)
    ws.cell(row=r, column=5, value=remain)
    ws.cell(row=r, column=6, value=cum)
    ws.cell(row=r, column=7, value=cumFix)
style_body(ws, 19, 30, 7)

# Bug chart: 当期Bug + 修复率 (cols 2 and 4) — add separately then merge visually via two series
c2 = LineChart()
c2.title = "WebApp · Bug趋势（当期Bug / 修复率）"
c2.style = 10
c2.height = 9
c2.width = 16
c2.legend.position = "b"
c2.add_data(Reference(ws, min_col=2, max_col=2, min_row=18, max_row=30), titles_from_data=True)
c2.add_data(Reference(ws, min_col=4, max_col=4, min_row=18, max_row=30), titles_from_data=True)
c2.set_categories(Reference(ws, min_col=1, min_row=19, max_row=30))
for s in c2.series:
    s.smooth = True
    s.marker.symbol = "circle"
ws.add_chart(c2, "G17")

ws["A33"] = "三、版本完整明细（用例侧，便于核对）"
ws["A33"].font = section_font
detail_h = [
    "版本", "迭代类型", "新增用例", "执行用例", "通过用例", "阻塞用例",
    "通过率(%)", "累计用例", "累计执行", "累计通过率(%)",
]
for j, h in enumerate(detail_h, 1):
    ws.cell(row=34, column=j, value=h)
style_header(ws, 34, 10)

caseDetail = {
    "20260508": ("敏捷", None, None, None, None, None, 0, 0, None),
    "20260514": ("敏捷", None, None, None, None, None, 0, 0, None),
    "20260520": ("敏捷", None, None, None, None, None, 0, 0, None),
    "20260528": ("标准", 1028, 1028, 885, 10, 86, 1028, 1028, 86.08),
    "20260611": ("敏捷", None, None, None, None, None, 1028, 1028, 86.08),
    "20260617": ("敏捷", None, None, None, None, None, 1028, 1028, 86.08),
    "20260625": ("敏捷", None, None, None, None, None, 1028, 1028, 86.08),
    "20260702": ("敏捷", None, None, None, None, None, 1028, 1028, 86.08),
    "20260708": ("敏捷", None, None, None, None, None, 1028, 1028, 86.08),
    "20260715": ("敏捷", None, None, None, None, None, 1028, 1028, 86.08),
    "20260722": ("标准", 65, 65, 57, 2, 87.6, 1093, 1093, 86.18),
    "20260729": ("敏捷", None, None, None, None, None, 1093, 1093, 86.18),
}
for i, v in enumerate(versions):
    vals = caseDetail[v]
    r = 35 + i
    ws.cell(row=r, column=1, value=v)
    for j, val in enumerate(vals, 2):
        ws.cell(row=r, column=j, value="—" if val is None else val)
style_body(ws, 35, 46, 10)
ws["A48"] = "口径说明：敏捷迭代无新增用例时，作图「新增用例/通过率」按 0 处理；累计修复率=(累计Bug−累计遗留)/累计Bug。"
ws["A48"].font = note_font
autosize(ws, [12, 12, 10, 10, 10, 10, 12, 10, 10, 14])

# ========== WebApp Sentry ==========
ws = wb.create_sheet("WebApp-Sentry")
ws["A1"] = "一、作图数据 · 问题数量趋势（对应 chart-sentry-cnt）"
ws["A1"].font = section_font
h = ["版本", "事项", "排查数", "发现问题", "解决(P0)", "待解决问题", "会话崩溃率(%)", "用户崩溃率(%)", "整体LCP(s)"]
for j, x in enumerate(h, 1):
    ws.cell(row=2, column=j, value=x)
style_header(ws, 2, 9)

sentryRows = [
    ("20260708", "Sentry上线", None, None, None, None, 15.43, 88.18, 5.17),
    ("20260715", "收集、排查问题", 50, 11, 0, 11, 15.7, 87.42, 5.83),
    ("20260722", "一期高优问题优化", 50, 5, 7, 9, 6.72, 41.05, 6.30),
    ("20260729", "二期高优问题优化", 60, 16, 7, 18, 1.01, 10, 6.21),
]
for i, row in enumerate(sentryRows):
    r = 3 + i
    for j, val in enumerate(row, 1):
        if j in (3, 4, 5, 6) and val is None:
            ws.cell(row=r, column=j, value=0)
        else:
            ws.cell(row=r, column=j, value="—" if val is None else val)
style_body(ws, 3, 6, 9)
add_smooth_line(ws, "WebApp · Sentry问题数量（发现问题 / 解决P0 / 待解决）", 4, 6, 2, 3, 6, 1, "A9")

ws["A26"] = "二、作图数据 · 崩溃率与LCP（对应 chart-sentry-perf）"
ws["A26"].font = section_font
h2 = ["版本", "会话崩溃率(%)", "用户崩溃率(%)", "整体LCP(s)"]
for j, x in enumerate(h2, 1):
    ws.cell(row=27, column=j, value=x)
style_header(ws, 27, 4)
for i, row in enumerate(sentryRows):
    r = 28 + i
    ws.cell(row=r, column=1, value=row[0])
    ws.cell(row=r, column=2, value=row[6])
    ws.cell(row=r, column=3, value=row[7])
    ws.cell(row=r, column=4, value=row[8])
style_body(ws, 28, 31, 4)
add_smooth_line(ws, "WebApp · 崩溃率与LCP", 2, 4, 27, 28, 31, 1, "A34")
ws["A51"] = "说明：Sentry上线版本排查/发现/解决/待解决在HTML中为「—」，作图按 0 处理。"
ws["A51"].font = note_font
autosize(ws, [12, 22, 10, 10, 10, 12, 14, 14, 12])

# ========== WebApp 高优优化 ==========
ws = wb.create_sheet("WebApp-高优优化")
ws["A1"] = "一、作图数据 · 按版本优化前后影响量（对应 chart-sentry-impact）"
ws["A1"].font = section_font
h = ["版本", "标签", "问题数", "优化前合计", "优化后合计"]
for j, x in enumerate(h, 1):
    ws.cell(row=2, column=j, value=x)
style_header(ws, 2, 5)
impact_ver = [
    ("20260722", "20260722 一期高优", 4, 69736 + 22760 + 10464 + 4702, 0 + 10 + 10 + 10),
    ("20260729", "20260729 二期高优", 5, 20280 + 873 + 711 + 177 + 176, 0 + 0 + 5 + 0 + 0),
]
for i, row in enumerate(impact_ver):
    r = 3 + i
    for j, val in enumerate(row, 1):
        ws.cell(row=r, column=j, value=val)
style_body(ws, 3, 4, 5)
add_smooth_line(ws, "WebApp · 高优问题优化前后影响量（按版本）", 4, 5, 2, 3, 4, 2, "G2", width=14)

ws["A7"] = "二、问题明细（优化效果描述）"
ws["A7"].font = section_font
h = ["版本", "优化批次", "问题", "数据效果"]
for j, x in enumerate(h, 1):
    ws.cell(row=8, column=j, value=x)
style_header(ws, 8, 4)
issues = [
    ("20260722", "一期高优问题", "1、视频聊场景偶现提示 accesstoken error", "影响用户由 69,736 人降为 0 人/日"),
    ("20260722", "一期高优问题", "2、视频聊场景偶现卡住、按钮无法点击", "影响用户由 22,760 人降至 <10 人/日；死点击由 2,526 次降为 1,071 次"),
    ("20260722", "一期高优问题", "3、用户退出登录后仍能进入登录态页面", "影响用户由 10,464 人降至 <10 人/日"),
    ("20260722", "一期高优问题", "4、发现页加载特别慢", "影响用户由 4,702 人降至 <10 人/日"),
    ("20260729", "二期高优问题", "1、谷歌登录浏览器权限拒绝导致无法调起 PWA 引导安装弹窗", "影响用户由 20,280 人降为 0 人/日"),
    ("20260729", "二期高优问题", "2、手机号登录环节，偶现点击下一步按钮没有反应", "触发事件由 873 次降为 0 次/日"),
    ("20260729", "二期高优问题", "3、个人主页点击视频聊按钮偶现没有反应", "触发事件由 711 次降至 <5 次/日"),
    ("20260729", "二期高优问题", "4、全屏充值页点击返回按钮没有反应", "触发事件由 177 次降为 0 次/日"),
    ("20260729", "二期高优问题", "5、首页点击速配按钮偶现没有反应", "触发事件由 176 次降为 0 次/日"),
]
for i, row in enumerate(issues):
    r = 9 + i
    for j, val in enumerate(row, 1):
        ws.cell(row=r, column=j, value=val)
        ws.cell(row=r, column=j).border = thin
        ws.cell(row=r, column=j).alignment = left

ws["A20"] = "三、按单问题量化（作图备用）"
ws["A20"].font = section_font
h = ["问题简称", "优化前", "优化后"]
for j, x in enumerate(h, 1):
    ws.cell(row=21, column=j, value=x)
style_header(ws, 21, 3)
impact_items = [
    ("accesstoken error", 69736, 0),
    ("视频聊卡住/按钮不可点", 22760, 10),
    ("退出后仍进登录态", 10464, 10),
    ("发现页加载慢", 4702, 10),
    ("PWA引导弹窗失败", 20280, 0),
    ("手机号登录下一步无响应", 873, 0),
    ("主页视频聊无响应", 711, 5),
    ("充值页返回无响应", 177, 0),
    ("首页速配无响应", 176, 0),
]
for i, row in enumerate(impact_items):
    r = 22 + i
    for j, val in enumerate(row, 1):
        ws.cell(row=r, column=j, value=val)
style_body(ws, 22, 30, 3)

bar = BarChart()
bar.type = "col"
bar.title = "单问题优化前后对比（备用）"
bar.style = 10
bar.height = 10
bar.width = 16
bar.legend.position = "b"
bar.y_axis.title = "影响量"
bar.add_data(Reference(ws, min_col=2, max_col=3, min_row=21, max_row=30), titles_from_data=True)
bar.set_categories(Reference(ws, min_col=1, min_row=22, max_row=30))
ws.add_chart(bar, "E20")
autosize(ws, [14, 18, 55, 55])

# ========== WebApp 线上事故 ==========
ws = wb.create_sheet("WebApp-线上事故")
ws["A1"] = "一、作图数据 · 事故趋势（对应 chart-accident）"
ws["A1"].font = section_font
h = ["时间点", "新增事故", "累计事故数"]
for j, x in enumerate(h, 1):
    ws.cell(row=2, column=j, value=x)
style_header(ws, 2, 3)
accidentTimeline = [
    ("20260508", 0), ("20260514", 0), ("20260520", 0), ("20260527", 1),
    ("20260528", 0), ("20260611", 0), ("20260617", 0), ("20260625", 0),
    ("20260702", 0), ("20260708", 0), ("20260715", 0), ("20260721", 1),
    ("20260722", 0), ("20260729", 0),
]
cum = 0
for i, (t, n) in enumerate(accidentTimeline):
    cum += n
    r = 3 + i
    ws.cell(row=r, column=1, value=t)
    ws.cell(row=r, column=2, value=n)
    ws.cell(row=r, column=3, value=cum)
style_body(ws, 3, 16, 3)
add_smooth_line(ws, "WebApp · 线上事故（新增 / 累计）", 2, 3, 2, 3, 16, 1, "E2")

ws["A19"] = "二、事故详情"
ws["A19"].font = section_font
h = ["时间", "根因", "关键节点", "影响"]
for j, x in enumerate(h, 1):
    ws.cell(row=20, column=j, value=x)
style_header(ws, 20, 4)
accidents = [
    (
        "20260527",
        "线上发布问题：审批修改速配弹窗配置（应改为显示速配入口、不显示速配弹窗；服务端误改为不显示速配入口和弹窗）",
        "5.27 19:00 审批修改配置 → 5.27 24:00 发现线上数据异常并回退 → 5.28 10:00 确认正确配置，测试后重新发布上线",
        "速配人数同比下降约 7000 人",
    ),
    (
        "20260721",
        "为解决部分用户 HTTP 从 2.0 降级到 1.1，将相关 API 域名 TLS 从 1.0 升级到 1.3",
        "7.21 17:35 调整配置完毕 → 17:55 业务监控报警【速配在聊女异常】→ 18:49 确认 Web 注册量下降 → 18:54 定位配置相关并回滚，线上恢复",
        "大量用户访问 WebApp 接口异常，预计影响新增注册约 5k；同步影响正常功能，预计影响充值约 2W",
    ),
]
for i, row in enumerate(accidents):
    r = 21 + i
    for j, val in enumerate(row, 1):
        ws.cell(row=r, column=j, value=val)
        ws.cell(row=r, column=j).border = thin
        ws.cell(row=r, column=j).alignment = left
autosize(ws, [12, 50, 55, 40])

# ========== WebApp UI自动化 ==========
ws = wb.create_sheet("WebApp-UI自动化")
ws["A1"] = "一、作图数据 · 模块效率（对应 chart-auto）"
ws["A1"].font = section_font
h = ["模块", "状态", "人工回归时长(min/版本)", "节省时长(min/版本)", "累计回归效率提升(%)"]
for j, x in enumerate(h, 1):
    ws.cell(row=2, column=j, value=x)
style_header(ws, 2, 5)
auto_chart = [
    ("注册登录", "已完成", 15, 10, 66.7),
    ("直播间", "已完成", 35, 30, 80.0),
    ("交友房", "计划", 40, 30, 77.8),
    ("我的栏目", "计划", 20, 20, 81.8),
    ("消息", "计划", 20, 15, 80.8),
    ("个人主页", "计划", 10, 10, 82.1),
]
for i, row in enumerate(auto_chart):
    r = 3 + i
    for j, val in enumerate(row, 1):
        ws.cell(row=r, column=j, value=val)
style_body(ws, 3, 8, 5)
add_smooth_line(ws, "WebApp · UI自动化（人工/节省/累计效率提升%）", 3, 5, 2, 3, 8, 1, "G2")

ws["A11"] = "二、自动化明细表（含框架搭建等）"
ws["A11"].font = section_font
h = ["状态", "时间", "模块", "用例数", "人工回归", "节省时长", "累计回归效率提升"]
for j, x in enumerate(h, 1):
    ws.cell(row=12, column=j, value=x)
style_header(ws, 12, 7)
autoRows_raw = [
    ("已完成", "6/1 ~ 6/5", "搭建自动化框架", "—", "—", "—", 0, 0),
    ("已完成", "6/1 ~ 6/5", "完成注册、登录模块自动化", "10 条", "15min / 版本", "10min / 版本", 15, 10),
    ("已完成", "6/8 ~ 6/12", "完成直播间模块用例编写", "41 条", "35min / 版本", "30min / 版本", 35, 30),
    ("已完成", "6/22 ~ 6/26", "完成直播间模块自动化", "（同上累计）", "35min / 版本", "30min / 版本", 0, 0),
    ("计划", "8/1 ~ 8/31", "交友房模块自动化", "—", "40min / 版本", "30min / 版本", 40, 30),
    ("计划", "9/1 ~ 9/15", "我的栏目自动化", "—", "20min / 版本", "20min / 版本", 20, 20),
    ("计划", "9/15 ~ 9/30", "消息模块自动化", "—", "20min / 版本", "15min / 版本", 20, 15),
    ("计划", "10/8 ~ 10/20", "个人主页自动化", "—", "10min / 版本", "10min / 版本", 10, 10),
]
cm = cs = 0
detail_rows = []
for status, time, module, cases, manual, saved, am, as_ in autoRows_raw:
    if manual == "—":
        lift = "—"
    else:
        cm += am
        cs += as_
        pct = cs / cm * 100
        lift = f"{round(pct, 1):.1f}".rstrip("0").rstrip(".") + "%"
    detail_rows.append((status, time, module, cases, manual, saved, lift))
lift_total = f"{round(cs / cm * 100, 2):.2f}%"
detail_rows.append(("合计", "—", "计划合计（人工/节省）", "—", "140min / 版本", "115min / 版本", lift_total))

for i, row in enumerate(detail_rows):
    r = 13 + i
    for j, val in enumerate(row, 1):
        ws.cell(row=r, column=j, value=val)
        ws.cell(row=r, column=j).border = thin
        ws.cell(row=r, column=j).alignment = left if j == 3 else center
ws["A24"] = "口径：累计回归效率提升% = 累计节省时长 ÷ 累计人工回归时长；直播间用例编写与自动化同属一个模块，时长只累加一次。"
ws["A24"].font = note_font
autosize(ws, [10, 14, 28, 14, 16, 16, 16])

# ========== App 用例 Bug ==========
ws = wb.create_sheet("App-用例Bug")
ws["A1"] = "一、作图数据 · App用例趋势（对应 chart-app-case）"
ws["A1"].font = section_font
appVersions = [
    "20260514", "20260521", "20260528", "20260604", "20260610", "20260617", "20260625",
    "20260702", "20260708", "20260715", "20260722", "20260724", "20260729",
]
appCase = {
    "20260514": ("敏捷", None, None, None),
    "20260521": ("敏捷", 40, 57.5, 40),
    "20260528": ("敏捷", 12, 100, 52),
    "20260604": ("敏捷", None, None, 52),
    "20260610": ("敏捷", None, None, 52),
    "20260617": ("敏捷", None, None, 52),
    "20260625": ("敏捷", None, None, 52),
    "20260702": ("标准", 314, 82.48, 366),
    "20260708": ("敏捷", None, None, 366),
    "20260715": ("敏捷", None, None, 366),
    "20260722": ("敏捷", None, None, 366),
    "20260724": ("标准", None, None, 366),
    "20260729": ("敏捷", None, None, 366),
}
h = ["版本", "迭代类型", "新增用例", "通过率(%)", "累计用例"]
for j, x in enumerate(h, 1):
    ws.cell(row=2, column=j, value=x)
style_header(ws, 2, 5)
for i, v in enumerate(appVersions):
    t, newC, rate, cum = appCase[v]
    r = 3 + i
    ws.cell(row=r, column=1, value=v)
    ws.cell(row=r, column=2, value=t)
    ws.cell(row=r, column=3, value=newC if newC is not None else 0)
    ws.cell(row=r, column=4, value=rate if rate is not None else 0)
    ws.cell(row=r, column=5, value=cum if cum is not None else "—")
style_body(ws, 3, 15, 5)
add_smooth_line(ws, "App · 用例趋势（新增用例 / 通过率）", 3, 4, 2, 3, 15, 1, "G2", width=16)

ws["A18"] = "二、作图数据 · App Bug趋势（对应 chart-app-bug）"
ws["A18"].font = section_font
h = ["版本", "当期Bug", "已修复", "修复率(%)", "遗留", "累计Bug", "累计遗留", "累计修复率(%)"]
for j, x in enumerate(h, 1):
    ws.cell(row=19, column=j, value=x)
style_header(ws, 19, 8)
appBug = {
    "20260514": (7, 7, 100, 0, 7, 0, 100),
    "20260521": (29, 29, 100, 0, 36, 0, 100),
    "20260528": (3, 3, 100, 0, 39, 0, 100),
    "20260604": (35, 35, 100, 0, 74, 0, 100),
    "20260610": (3, 3, 100, 0, 77, 0, 100),
    "20260617": (1, 1, 100, 0, 78, 0, 100),
    "20260625": (0, 0, 100, 0, 78, 0, 100),
    "20260702": (55, 55, 100, 0, 133, 0, 100),
    "20260708": (28, 28, 100, 0, 161, 0, 100),
    "20260715": (27, 27, 100, 0, 188, 0, 100),
    "20260722": (16, 16, 100, 0, 204, 0, 100),
    "20260724": (0, 0, 100, 0, 204, 0, 100),
    "20260729": (12, 11, 99.99, 1, 216, 1, 99.54),
}
for i, v in enumerate(appVersions):
    vals = appBug[v]
    r = 20 + i
    ws.cell(row=r, column=1, value=v)
    for j, val in enumerate(vals, 2):
        ws.cell(row=r, column=j, value=val)
style_body(ws, 20, 32, 8)

c = LineChart()
c.title = "App · Bug趋势（当期Bug / 修复率）"
c.style = 10
c.height = 9
c.width = 16
c.legend.position = "b"
c.add_data(Reference(ws, min_col=2, max_col=2, min_row=19, max_row=32), titles_from_data=True)
c.add_data(Reference(ws, min_col=4, max_col=4, min_row=19, max_row=32), titles_from_data=True)
c.set_categories(Reference(ws, min_col=1, min_row=20, max_row=32))
for s in c.series:
    s.smooth = True
    s.marker.symbol = "circle"
ws.add_chart(c, "J18")

ws["A35"] = "三、用例完整明细"
ws["A35"].font = section_font
h = ["版本", "迭代类型", "新增用例", "执行用例", "通过用例", "阻塞", "通过率(%)", "累计用例", "累计执行", "累计通过率(%)"]
for j, x in enumerate(h, 1):
    ws.cell(row=36, column=j, value=x)
style_header(ws, 36, 10)
appCaseDetail = {
    "20260514": ("敏捷", None, None, None, None, None, None, None, None),
    "20260521": ("敏捷", 40, 40, 23, None, 57.5, 40, 40, 57.5),
    "20260528": ("敏捷", 12, 12, 12, None, 100, 52, 52, 67.31),
    "20260604": ("敏捷", None, None, None, None, None, 52, 52, 67.31),
    "20260610": ("敏捷", None, None, None, None, None, 52, 52, 67.31),
    "20260617": ("敏捷", None, None, None, None, None, 52, 52, 67.31),
    "20260625": ("敏捷", None, None, None, None, None, 52, 52, 67.31),
    "20260702": ("标准", 314, 314, 259, None, 82.48, 366, 366, 80.33),
    "20260708": ("敏捷", None, None, None, None, None, 366, 366, 80.33),
    "20260715": ("敏捷", None, None, None, None, None, 366, 366, 80.33),
    "20260722": ("敏捷", None, None, None, None, None, 366, 366, 80.33),
    "20260724": ("标准", None, None, None, None, None, 366, 366, 80.33),
    "20260729": ("敏捷", None, None, None, None, None, 366, 366, 80.33),
}
for i, v in enumerate(appVersions):
    vals = appCaseDetail[v]
    r = 37 + i
    ws.cell(row=r, column=1, value=v)
    for j, val in enumerate(vals, 2):
        ws.cell(row=r, column=j, value="—" if val is None else val)
style_body(ws, 37, 49, 10)
autosize(ws, [12, 10, 10, 10, 10, 8, 12, 10, 10, 14])

# ========== App 线上事故 ==========
ws = wb.create_sheet("App-线上事故")
ws["A1"] = "一、作图数据 · 事故趋势（对应 chart-app-accident）"
ws["A1"].font = section_font
h = ["版本", "当期事故合计", "服务器事故", "版本事故", "累计事故数"]
for j, x in enumerate(h, 1):
    ws.cell(row=2, column=j, value=x)
style_header(ws, 2, 5)
appAcc = [
    ("20260514", 0, 0, 0), ("20260521", 0, 0, 0), ("20260528", 0, 0, 0), ("20260604", 0, 0, 0),
    ("20260610", 1, 1, 0), ("20260617", 1, 1, 0), ("20260625", 1, 1, 0), ("20260702", 2, 1, 1),
    ("20260708", 0, 0, 0), ("20260715", 1, 0, 1), ("20260722", 1, 0, 1), ("20260724", 0, 0, 0),
    ("20260729", 0, 0, 0),
]
cum = 0
for i, (v, total, server, ver) in enumerate(appAcc):
    cum += total
    r = 3 + i
    ws.cell(row=r, column=1, value=v)
    ws.cell(row=r, column=2, value=total)
    ws.cell(row=r, column=3, value=server)
    ws.cell(row=r, column=4, value=ver)
    ws.cell(row=r, column=5, value=cum)
style_body(ws, 3, 15, 5)
add_smooth_line(ws, "App · 线上事故（服务器 / 版本 / 累计）", 3, 5, 2, 3, 15, 1, "G2", width=16)

ws["A18"] = "二、事故详情"
ws["A18"].font = section_font
h = ["项目", "时间", "根因", "关键节点", "影响", "备注"]
for j, x in enumerate(h, 1):
    ws.cell(row=19, column=j, value=x)
style_header(ws, 19, 6)
details = [
    ("chamet", "20260702", "公会分账计算代理费时，错误排除「速配金豆」", "7.4 15:47 用户反馈；7.5 20:00 问题全部解决", "该时间段内所有通过速配获得金豆的代理名下用户", "需求/用例评审遗漏"),
    ("chamet", "20260702", "CDN 加速节点异常，导致主页、消息页图片加载失败", "7.2 14:23 大量用户反馈；剔除异常节点后于 14:50 恢复", "以哥伦比亚用户为主", "—"),
    ("chamet", "20260715", "礼物分账逻辑变更后，返利统计从总账户改为充值账户，导致用户返利减少", "7.15 11:14 用户反馈；14:00 定位问题；下个版本修复；已审批给受影响用户补发钻石", "7.2–7.15 期间有消费的所有用户", "需求评审遗漏消费来源属性，仅关注钻石去向属性"),
    ("chamet", "20260722", "代理页从客户端改为 H5 后，未按用户国家推荐代理", "7.28 反馈排序不正确", "7.22–7.28 进入代理充值 H5 页的用户", "测试遗漏：只检查了数据展示，未验证排序逻辑"),
    ("chamet", "20260626", "服务器显卡授权过期，游戏卡顿，3D 赛车看不到终点线", "6.26 11:00 用户反馈；更换显卡并重启服务器后，15:32 恢复", "事故期间所有 3D 赛车玩家", "—"),
    ("chamet", "20260618", "多名用户反馈无法接通来电", "6.18 09:33 用户反馈；确认 6.18 14:00–16:00 融云异常；现已恢复", "6.18 14:00–16:00 进行通话的用户", "—"),
    ("chamet", "20260611", "代理无法登录后台，页面提示错误信息", "6.11 17:18 用户反馈；关联阿里云服务升级；约 17:30 恢复", "6.11 17:00 左右打开代理后台的用户", "—"),
]
for i, row in enumerate(details):
    r = 20 + i
    for j, val in enumerate(row, 1):
        ws.cell(row=r, column=j, value=val)
        ws.cell(row=r, column=j).border = thin
        ws.cell(row=r, column=j).alignment = left
autosize(ws, [10, 12, 45, 45, 35, 30])

# ========== App 埋点自动化 ==========
ws = wb.create_sheet("App-埋点自动化")
ws["A1"] = "一、作图数据（对应 chart-app-auto）"
ws["A1"].font = section_font
h = ["阶段", "人工回归(min/版本)", "节省时长(min/版本)", "累计回归效率提升(%)"]
for j, x in enumerate(h, 1):
    ws.cell(row=2, column=j, value=x)
style_header(ws, 2, 4)
app_auto_chart = [
    ("曝光/点击埋点(3.8~4.16)", 120, 120, 100),
    ("充值/登录/送礼(5.11~6.2)", 240, 240, 100),
]
for i, row in enumerate(app_auto_chart):
    r = 3 + i
    for j, val in enumerate(row, 1):
        ws.cell(row=r, column=j, value=val)
style_body(ws, 3, 4, 4)
add_smooth_line(ws, "App · 埋点自动化（节省时长 / 累计效率提升%）", 3, 4, 2, 3, 4, 1, "F2", width=14)

ws["A8"] = "二、明细表"
ws["A8"].font = section_font
h = ["时间", "模块", "用例数", "人工回归", "节省时长", "累计回归效率提升"]
for j, x in enumerate(h, 1):
    ws.cell(row=9, column=j, value=x)
style_header(ws, 9, 6)
app_auto_detail = [
    ("3.8 ~ 4.16", "自动化框架搭建，完成曝光222、点击223自动化埋点测试", "49 条", "120min / 版本", "120min / 版本", "100%"),
    ("5.11 ~ 6.2", "完成主流程充值、登录、送礼相关埋点", "59 条", "240min / 版本", "240min / 版本", "100%"),
    ("合计", "—", "—", "360min / 版本", "360min / 版本", "100%"),
]
for i, row in enumerate(app_auto_detail):
    r = 10 + i
    for j, val in enumerate(row, 1):
        ws.cell(row=r, column=j, value=val)
        ws.cell(row=r, column=j).border = thin
        ws.cell(row=r, column=j).alignment = left if j == 2 else center
ws["A15"] = "说明：HTML图中未画「人工回归时长」曲线，仅保留节省时长与累计效率；本表仍保留人工回归列便于核对。"
ws["A15"].font = note_font
autosize(ws, [16, 48, 10, 16, 16, 16])

out = r"C:\Users\mym\Desktop\测试组累计数据报表_作图数据.xlsx"
wb.save(out)
print("OK", out)
print("sheets:", wb.sheetnames)
