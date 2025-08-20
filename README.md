# 2024 MRR Growth – Quarterly Analysis

**Contact:** 24f3003609@ds.study.iitm.ac.in

This pull request adds a lightweight analytics module (Python) and visuals to assess 2024 MRR growth against the industry target of **15**.

## Data
- Q1: 2.18  
- Q2: 10.82  
- Q3: 12.13  
- Q4: 14.11  

**Average (2024): 9.81**

> Data source: Provided quarterly MRR growth figures for 2024.

## How to run
```bash
python -m venv .venv && source .venv/bin/activate  # On Windows: .venv\Scripts\activate
pip install -r requirements.txt
python analysis.py
```

This generates two charts under `assets/`:
- `mrr_trend.png` – MRR growth trend across quarters
- `mrr_vs_target.png` – Bars by quarter with a horizontal line at the target (=15)

## Key Findings
1. **Consistent QoQ improvement**: Growth rose each quarter (2.18 → 10.82 → 12.13 → 14.11).  
2. **Below benchmark**: Despite improvements, all quarters remained **below the target of 15**.  
3. **Closing the gap**: The Q4 value (14.11) is closest, leaving a **gap of 0.89** to the target.  
4. **Run-rate implication**: The year’s **average is 9.81**, far short of 15, indicating the upswing was backloaded.

## Business Implications
- **Pipeline Health**: The progressive improvement suggests recent initiatives moved the needle, but **sustainability is unproven** (only Q4 approached target).
- **Revenue Predictability**: A sub-target average (9.81) implies **forecast risk**—we need more resilient, diversified growth drivers to de-risk seasonality and late-year surges.
- **Competitive Positioning**: Being under the 15 benchmark may **impact perception** among enterprise buyers and investors unless a clear plan is articulated.

## Recommendations (to reach 15+ reliably)
1. **Primary Strategy – Expand into new market segments**  
   - Identify 2–3 **adjacent ICPs** (e.g., SMB premium, mid-market in new verticals, or geographies with lower CAC).  
   - Build **segment-specific value propositions**, landing pages, and pricing/packaging.  
   - Run **controlled experiments** (A/B offers, 90-day pilots) to validate lift in trial-to-paid conversion and expansion MRR.

2. **Segmented GTM Motions**
   - **Partner-led motion** for new geographies; **marketplace listings** for fast discovery.
   - **Verticalized messaging** (case studies, integrations) to boost **pipeline velocity**.

3. **Product-Led Expansion**
   - Introduce **usage-based add-ons** and **tiered expansion levers** to increase ARPA in high-fit segments.
   - Instrument **in-app nudges** tied to activation milestones that correlate with paid conversion.

4. **Operational Guardrails**
   - Set a **quarterly target path**: 13 → 15 → 16.5 to overshoot the benchmark by Q4.  
   - Add a **leading indicator dashboard**: activation rate, PQL volume, win rates by segment, and expansion MRR share.

## Files in this PR
- `data.csv` – Quarterly MRR growth data
- `analysis.py` – Analysis and chart generation (Python)
- `assets/mrr_trend.png` – MRR growth trend
- `assets/mrr_vs_target.png` – MRR vs target visualization
- `README.md` – This data story, findings, and recommendations

---

*Prepared via LLM-assisted workflow (Jules/ChatGPT Codex capable).*
