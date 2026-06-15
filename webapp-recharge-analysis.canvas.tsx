import {
  Stack, Row, Grid, H1, H2, H3, Text, Stat, Card, CardHeader, CardBody,
  Table, Divider, Callout, LineChart, BarChart, PieChart, useHostTheme,
} from "cursor/canvas";

const hourlyData = [
  { h: "0", amount: 5.8771, users: 4665, arppu: 12.6 },
  { h: "1", amount: 8.9016, users: 6915, arppu: 12.87 },
  { h: "2", amount: 10.5691, users: 8306, arppu: 12.72 },
  { h: "3", amount: 9.2026, users: 7942, arppu: 11.59 },
  { h: "4", amount: 7.7392, users: 6008, arppu: 12.88 },
  { h: "5", amount: 5.7033, users: 4479, arppu: 12.73 },
  { h: "6", amount: 4.4377, users: 3119, arppu: 14.23 },
  { h: "7", amount: 3.1543, users: 2391, arppu: 13.19 },
  { h: "8", amount: 2.6497, users: 2134, arppu: 12.42 },
  { h: "9", amount: 2.5949, users: 2290, arppu: 11.33 },
  { h: "10", amount: 2.8906, users: 2769, arppu: 10.44 },
  { h: "11", amount: 3.3883, users: 3134, arppu: 10.81 },
  { h: "12", amount: 3.615, users: 3706, arppu: 9.75 },
  { h: "13", amount: 4.2037, users: 4234, arppu: 9.93 },
  { h: "14", amount: 4.6519, users: 4622, arppu: 10.06 },
  { h: "15", amount: 4.5853, users: 4617, arppu: 9.93 },
  { h: "16", amount: 4.9235, users: 4739, arppu: 10.39 },
  { h: "17", amount: 5.0047, users: 5139, arppu: 9.74 },
  { h: "18", amount: 5.1293, users: 5265, arppu: 9.74 },
  { h: "19", amount: 4.7636, users: 4638, arppu: 10.27 },
  { h: "20", amount: 4.2576, users: 4022, arppu: 10.59 },
  { h: "21", amount: 3.7858, users: 3560, arppu: 10.63 },
  { h: "22", amount: 3.7896, users: 3479, arppu: 10.89 },
  { h: "23", amount: 4.5038, users: 3738, arppu: 12.05 },
];

const sceneData = [
  { scene: "个人页", users: 14408, orders: 38826, total: 317392.69, arppu: 22.03, pct: 66.31 },
  { scene: "约聊余额不足", users: 5451, orders: 12073, total: 94751.31, arppu: 17.38, pct: 19.80 },
  { scene: "礼物橱窗", users: 887, orders: 2290, total: 33255.99, arppu: 37.49, pct: 6.95 },
  { scene: "直播间浮层", users: 427, orders: 945, total: 11507.95, arppu: 26.95, pct: 2.40 },
  { scene: "等级页", users: 511, orders: 843, total: 10154.07, arppu: 19.87, pct: 2.12 },
  { scene: "游戏", users: 146, orders: 509, total: 6652.37, arppu: 45.56, pct: 1.39 },
  { scene: "升级弹框", users: 793, orders: 909, total: 4081.01, arppu: 5.15, pct: 0.85 },
  { scene: "交友房浮层", users: 37, orders: 67, total: 835.72, arppu: 22.59, pct: 0.17 },
];

const firstPayScene = [
  { scene: "个人页", users: 169, total: 730.91, arppu: 4.32, pct: 63.61 },
  { scene: "约聊余额不足", users: 90, total: 323.05, arppu: 3.59, pct: 28.11 },
  { scene: "升级单弹窗", users: 14, total: 23.94, arppu: 1.71, pct: 2.08 },
  { scene: "等级页", users: 8, total: 13.64, arppu: 1.71, pct: 1.18 },
  { scene: "礼物橱窗", users: 5, total: 55.74, arppu: 11.15, pct: 4.85 },
  { scene: "游戏", users: 1, total: 0.88, arppu: 0.88, pct: 0.07 },
  { scene: "直播间浮层", users: 1, total: 0.88, arppu: 0.88, pct: 0.07 },
];

const priceBuckets = [
  { bucket: "≤1", users: 274, avgPrice: 0.88, total: 241.12 },
  { bucket: "(1,3]", users: 209, avgPrice: 2.60, total: 542.47 },
  { bucket: "(3-5]", users: 54, avgPrice: 3.56, total: 192.15 },
  { bucket: "(5-10]", users: 41, avgPrice: 8.68, total: 355.77 },
  { bucket: "(10-30]", users: 34, avgPrice: 16.30, total: 554.34 },
  { bucket: "(30-50]", users: 3, avgPrice: 35.50, total: 106.50 },
  { bucket: ">50", users: 2, avgPrice: 88.43, total: 176.85 },
];

const countryPeak = [
  { country: "英国", peakArppu: 59.96, troughArppu: 44.64, peakPct: 0.92, troughPct: 2.14 },
  { country: "美国", peakArppu: 55.73, troughArppu: 31.33, peakPct: 2.51, troughPct: 4.94 },
  { country: "加拿大", peakArppu: 47.12, troughArppu: 25.78, peakPct: 0.78, troughPct: 1.54 },
  { country: "阿联酋", peakArppu: 41.20, troughArppu: 21.35, peakPct: 1.49, troughPct: 1.89 },
  { country: "卡塔尔", peakArppu: 30.56, troughArppu: 26.87, peakPct: 0.70, troughPct: 0.83 },
  { country: "沙特", peakArppu: 27.01, troughArppu: 19.18, peakPct: 1.02, troughPct: 1.96 },
  { country: "巴基斯坦", peakArppu: 23.80, troughArppu: 11.85, peakPct: 0.93, troughPct: 1.52 },
  { country: "土耳其", peakArppu: 23.50, troughArppu: 16.32, peakPct: 0.70, troughPct: 1.17 },
  { country: "印度", peakArppu: 18.03, troughArppu: 10.88, peakPct: 80.93, troughPct: 69.93 },
  { country: "孟加拉国", peakArppu: 16.24, troughArppu: 14.28, peakPct: 1.29, troughPct: 0.87 },
  { country: "印尼", peakArppu: 11.13, troughArppu: 7.39, peakPct: 1.09, troughPct: 1.52 },
];

export default function WebAppRechargeAnalysis() {
  const theme = useHostTheme();
  const t = theme.tokens;
  const accent = t.syntax?.keyword ?? "#4fa";

  return (
    <Stack gap={28} style={{ padding: 24, maxWidth: 1100 }}>
      <Stack gap={4}>
        <H1>WebApp 充值数据分析</H1>
        <Text tone="secondary">数据日期：2026-05（全月趋势） · 2026.06.01（首充行为）· 库内时区</Text>
      </Stack>

      {/* KPIs */}
      <Grid columns={4} gap={16}>
        <Stat value="93,656" label="6/1 新注册用户" />
        <Stat value="617" label="7日内首充用户" />
        <Stat value="0.66%" label="7日首充转化率" tone="warning" />
        <Stat value="$3.52" label="首充平均客单（美元）" />
      </Grid>

      <Divider />

      {/* 24小时充值趋势 */}
      <Stack gap={12}>
        <H2>24小时充值趋势（2026-05，全月）</H2>
        <Text tone="secondary" size="small">高峰期：0–5 点；低谷期：8–10 点 · 充值金额单位：万美元</Text>
        <LineChart
          categories={hourlyData.map(d => d.h)}
          series={[
            { name: "充值金额（万美元）", data: hourlyData.map(d => d.amount) },
            { name: "付费用户数（百人）", data: hourlyData.map(d => Math.round(d.users / 100)) },
          ]}
          height={220}
          fill
          valueSuffix=""
          beginAtZero
          style={{ marginTop: 4 }}
        />
        <LineChart
          categories={hourlyData.map(d => d.h)}
          series={[{ name: "ARPPU（美元）", data: hourlyData.map(d => d.arppu) }]}
          height={140}
          valuePrefix="$"
          beginAtZero={false}
          referenceLines={[{ value: 11.0, label: "均值≈11", tone: "neutral" }]}
        />
        <Text tone="secondary" size="small">
          凌晨 1–3 点为绝对高峰（1点 $8.9万，2点 $10.6万），午间 8–10 点为最低谷。高峰期 ARPPU（$11.6–12.9）整体高于白天（$9.7–10.4），说明深夜付费用户客单价更高。
        </Text>
      </Stack>

      <Divider />

      {/* 充值场景 */}
      <Stack gap={12}>
        <H2>充值场景分布（全用户·5月）</H2>
        <Grid columns="1fr 1fr" gap={16}>
          <Stack gap={8}>
            <H3>各场景充值金额占比</H3>
            <PieChart
              data={sceneData.map(d => ({ label: d.scene, value: d.total }))}
              donut
              size={200}
            />
          </Stack>
          <Stack gap={8}>
            <H3>各场景 ARPPU（美元）</H3>
            <BarChart
              categories={sceneData.map(d => d.scene)}
              series={[{ name: "ARPPU", data: sceneData.map(d => d.arppu) }]}
              horizontal
              height={200}
              valuePrefix="$"
              showValues
            />
          </Stack>
        </Grid>
        <Table
          headers={["充值来源", "用户数量", "订单数量", "总充值金额（$）", "ARPPU（$）", "总充值占比"]}
          columnAlign={["left", "right", "right", "right", "right", "right"]}
          striped
          rows={sceneData.map((d, i) => [
            d.scene,
            d.users.toLocaleString(),
            d.orders.toLocaleString(),
            d.total.toLocaleString(),
            `$${d.arppu}`,
            `${d.pct}%`,
          ])}
          rowTone={[undefined, undefined, undefined, undefined, undefined, undefined, "warning", undefined]}
        />
        <Callout tone="info" title="关键发现">
          个人页是最大充值入口（66.3% 金额）；礼物橱窗与游戏场景人少但 ARPPU 极高（$37–$46），是高价值精准场景；升级弹框用户多（793）但人均仅 $5.15，转化效率最低。
        </Callout>
      </Stack>

      <Divider />

      {/* 首充场景 */}
      <Stack gap={12}>
        <H2>首充场景分布（6/1 注册 cohort）</H2>
        <Text tone="secondary" size="small">共 288 位首充用户能关联到场景</Text>
        <Grid columns="1fr 1fr" gap={16}>
          <Stack gap={6}>
            <H3>首充入口场景</H3>
            <PieChart
              data={firstPayScene.map(d => ({ label: d.scene, value: d.users }))}
              size={180}
            />
          </Stack>
          <Stack gap={6}>
            <H3>首充场景 ARPPU（美元）</H3>
            <BarChart
              categories={firstPayScene.map(d => d.scene)}
              series={[{ name: "ARPPU", data: firstPayScene.map(d => d.arppu) }]}
              horizontal
              height={180}
              valuePrefix="$"
              showValues
            />
          </Stack>
        </Grid>
        <Table
          headers={["来源", "用户数量", "总充值金额（$）", "ARPPU（$）", "总充值占比"]}
          columnAlign={["left", "right", "right", "right", "right"]}
          striped
          rows={firstPayScene.map(d => [
            d.scene,
            d.users.toString(),
            `$${d.total}`,
            `$${d.arppu}`,
            `${d.pct}%`,
          ])}
        />
        <Callout tone="info" title="关键发现">
          首充用户中，个人页（169人，63.6%）和约聊余额不足（90人，28.1%）合计覆盖 92% 金额。礼物橱窗虽仅 5 人却贡献 $55.74（ARPPU $11.15 在首充中最高），说明礼物场景首充用户质量最高。
        </Callout>
      </Stack>

      <Divider />

      {/* 首充时机 + 金额分布 */}
      <Grid columns="1fr 1fr" gap={20}>
        <Stack gap={10}>
          <H2>首充时机</H2>
          <H3>注册后7天内首充分布</H3>
          <BarChart
            categories={["0-1天", "1-3天", "3-5天", "5-7天"]}
            series={[{ name: "首充人数", data: [489, 57, 18, 7] }]}
            height={140}
            showValues
          />
          <H3>注册当天（1天内）首充时段</H3>
          <BarChart
            categories={["0-1h", "1-3h", "3-5h", "5-7h", "7-12h", "12-24h"]}
            series={[{ name: "首充人数", data: [441, 46, 8, 5, 8, 27] }]}
            height={140}
            showValues
          />
          <Callout tone="warning" title="注册即付">
            79.3% 首充（489/617）发生在注册当天，当天首充中 71.5%（441人）在注册后 1 小时内完成，黄金转化窗口极短。
          </Callout>
        </Stack>

        <Stack gap={10}>
          <H2>首充金额分布</H2>
          <BarChart
            categories={priceBuckets.map(d => d.bucket)}
            series={[{ name: "用户数", data: priceBuckets.map(d => d.users) }]}
            height={150}
            valueSuffix=" 人"
            showValues
          />
          <Table
            headers={["金额区间（$）", "用户数", "均价（$）", "合计（$）"]}
            columnAlign={["left", "right", "right", "right"]}
            striped
            rows={priceBuckets.map(d => [
              d.bucket,
              d.users.toString(),
              `$${d.avgPrice}`,
              `$${d.total}`,
            ])}
          />
          <Callout tone="neutral" title="低客单为主">
            首充以 ≤$1（274人，44%）和 $1–$3（209人，34%）为主，两档合计 78%。高客单（$10+）仅 39 人却贡献 $837（38.6%），高端用户价值显著。
          </Callout>
        </Stack>
      </Grid>

      <Divider />

      {/* 高峰低谷国家分布 */}
      <Stack gap={12}>
        <H2>高峰 vs 低谷期：分国家 ARPPU 与用户占比（2026-05）</H2>
        <Text tone="secondary" size="small">高峰期：0–5 点；低谷期：8–10 点</Text>
        <Grid columns="1fr 1fr" gap={16}>
          <Stack gap={6}>
            <H3>ARPPU 对比（美元）</H3>
            <BarChart
              categories={countryPeak.map(d => d.country)}
              series={[
                { name: "高峰期", data: countryPeak.map(d => d.peakArppu) },
                { name: "低谷期", data: countryPeak.map(d => d.troughArppu) },
              ]}
              horizontal
              height={260}
              valuePrefix="$"
            />
          </Stack>
          <Stack gap={6}>
            <H3>用户占比（%）</H3>
            <Table
              headers={["国家", "高峰占比", "低谷占比", "低谷变动"]}
              columnAlign={["left", "right", "right", "right"]}
              striped
              rows={countryPeak.map(d => {
                const delta = d.troughPct - d.peakPct;
                return [
                  d.country,
                  `${d.peakPct}%`,
                  `${d.troughPct}%`,
                  `${delta > 0 ? "+" : ""}${delta.toFixed(2)}%`,
                ];
              })}
              rowTone={countryPeak.map((d, i) => {
                if (d.country === "印度") return "info";
                if (d.troughPct - d.peakPct > 2) return "warning";
                return undefined;
              })}
            />
          </Stack>
        </Grid>
        <Callout tone="info" title="关键发现">
          印度用户占绝对主导（高峰 80.9%，低谷 69.9%），但 ARPPU 最低（$18 / $10.9）。英国、美国、加拿大等西方市场高峰期 ARPPU 显著高于低谷（英国 $60 vs $45），且低谷期占比上升（美国 +2.4%），说明高 ARPPU 国家在白天更活跃，是低谷期的主要贡献者。
        </Callout>
      </Stack>
    </Stack>
  );
}
