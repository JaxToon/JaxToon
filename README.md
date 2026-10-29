<!-- Header -->
<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&height=200&color=0:134E5E,100:71B280&text=Firgy%20Matannatikka&fontColor=ffffff&fontSize=46&fontAlignY=36&desc=Data%20%C2%B7%20AI%20%C2%B7%20Human%20Capital&descAlignY=56&descSize=18&animation=fadeIn" alt="header"/>
  <br/>
  <img src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=500&size=18&pause=1200&color=71B280&center=true&vCenter=true&width=640&height=30&lines=Officer+Development+Program+%40+BNI;Researching+why+LLMs+hallucinate;Ex-StickEarn+%C2%B7+Telkomsel+%C2%B7+Solve+Education!;Turning+messy+data+into+maps%2C+models+%26+decisions;Jakarta-based%2C+Pekanbaru-rooted+%F0%9F%8C%BF" alt="typing intro"/>
</p>

<p align="center">
  <a href="https://www.linkedin.com/in/firgy-matannatikka"><img src="https://img.shields.io/badge/LinkedIn-Firgy%20Matannatikka-0A66C2?style=flat-square&logo=linkedin&logoColor=white" alt="LinkedIn"/></a>
  <img src="https://img.shields.io/badge/Based%20in-Jakarta-71B280?style=flat-square" alt="Jakarta"/>
  <img src="https://img.shields.io/badge/Telkom%20University-Data%20Science%20'25-134E5E?style=flat-square" alt="Telkom University"/>
  <img src="https://komarev.com/ghpvc/?username=JaxToon&style=flat-square&color=134E5E&label=profile+views" alt="profile views"/>
</p>

---

### 👋 Hey, I'm Firgy

I'm a data person living in **Jakarta**, with my roots and family back in **Pekanbaru, Riau**, where I still head home often. I can't stop exploring: nature, new tech, new hobbies, whatever comes next.
At work, that curiosity turns into pipelines, maps and models. I've worked across **advertising, ed-tech, telco and now banking**, and I like sitting where data science, AI and people meet.

```sql
-- whoami.sql
SELECT
  'Firgy Matannatikka'                              AS name,
  'Officer Development Program @ BNI'               AS now,        -- Data Analytics track
  ['Data Analyst @ StickEarn',
   'Research Intern @ Telkomsel',
   'Data Analyst @ Solve Education!']               AS before,
  'B.Sc. Data Science, Telkom University (2025)'    AS alma_mater,
  'Jakarta'                                         AS based_in,
  'Pekanbaru, Riau'                                 AS hometown,   -- still go home a lot
  ['LLM hallucination', 'geospatial analytics',
   'computer vision', 'data pipelines']             AS works_on,
  ['nature', 'new tech', 'new hobbies',
   'anything I haven''t tried yet']                 AS explores,
  'Bahasa Indonesia · English'                      AS speaks
FROM `earth.indonesia`
WHERE curiosity > 0   -- always true
LIMIT 1;
```

### 🔭 Right now

- 🏦 **Officer Development Program @ BNI**, Data Analytics track, rotating across units to see the bank from the inside
- 🔬 **Researching LLM hallucination**: why models answer confidently when key evidence is missing, and how to make them stop ([details below](#-featured-research-epistemic-access-architecture))
- 🤝 **[BNI Nex](https://github.com/JaxToon/ValueChainCostumerAcquisitions)** (team capstone): a relationship-manager copilot for value-chain acquisition, combining knowledge graphs, ML, RAG and agentic LLMs
- 🎮 **Side quest**: a [Dota 2 draft coach](https://github.com/JaxToon/Dota2MetaFinder) built on public match data

### 🔬 Featured research: [Epistemic Access Architecture](https://github.com/JaxToon/Epistemic-Access-Architecture)

> **LLMs often *know* their evidence is missing. They just don't act on it unless that knowledge is given authority.**

Inspired by split-brain experiments, where the speaking hemisphere confidently explains things it never saw, I cut the evidence channel between a *reader* and a *generator* on HotpotQA and measured what happens. Every study was pre-registered with its failure criteria, run on Qwen2.5 1.5B / 3B / 7B on a single 8 GB laptop GPU.

- 🧩 **Missing evidence → confident wrong answers.** Remove the answer paragraph and 75–84% of the answers models still give are wrong, across all three sizes.
- 🪞 **Confabulation is built from leftovers.** 74–84% of fabricated answers are stitched from the evidence that remains, not recalled from memory.
- 🧠 **The model already knows.** A 3.4M-parameter head reading the frozen model's hidden states detects insufficient evidence with **0.99** paired accuracy.
- ⚖️ **Advice vs authority.** Given to the model as a hint, that signal works no better than a shuffled placebo. Used as a binding gate, it cuts hallucination from **22.6% to 9.3%**, replicated on 400 new questions and on Gemma. The honest trade-off: the model answers less often.

<p align="center">
  <img src="https://raw.githubusercontent.com/JaxToon/Epistemic-Access-Architecture/main/09_reports/figures/setup_saran_vs_perintah.png" width="85%" alt="The same signal is inert as advice but effective as authority"/>
</p>

`PyTorch` · `Transformers` · `Qwen2.5` · `HotpotQA` · `pre-registration` · `McNemar + bootstrap CIs`

### 🧪 Open-source projects

| Project | What it does | Stack |
|---|---|---|
| **[BNI Nex: RM Copilot](https://github.com/JaxToon/ValueChainCostumerAcquisitions)** · *team capstone* | Finds new customers through the value chains of existing ones: knowledge graph + ML scoring + a local LLM with RAG and 4-layer guardrails. Graph features lift acquisition ROC-AUC to **0.725** vs a 0.529 business baseline (synthetic data) | Neo4j · LightGBM · SHAP · Gemma · Streamlit · DeepEval |
| **[Hyper-personalized banking ads](https://github.com/JaxToon/hyperpersonalization-ads)** | Next-best-action model for 24 banking products plus real-time ad copy assembly, served behind consent, eligibility and frequency-cap guardrails | LightGBM · FastAPI · Redis |
| **[Customer 360 copilot](https://github.com/JaxToon/Costumer360)** | Knowledge-graph copilot that gives relationship managers a full view of each customer; one `docker compose up` to run | Neo4j · Streamlit · scikit-learn |
| **[Data & Analytics Hub PoC](https://github.com/JaxToon/AnalyticHub)** | Discover → Request → Consume → Govern portal: data catalog, glossary, access requests, and an H3 regional-potential map, with 44 test scenarios | FastAPI · H3 · pytest |
| **[Quant trading research](https://github.com/JaxToon/quant-trade-crypto)** | SMC/FVG signals, a GNN and multi-agent LLM debate. My own audit found the backtest "edge" came from an optimistic fill assumption; at realistic fills it loses money, and the README says so | PyTorch Geometric · Neo4j · DuckDB |
| **[Dota 2 Meta Finder](https://github.com/JaxToon/Dota2MetaFinder)** | Tier lists, counters, hero synergy and a draft coach from ~20k public matches | Python stdlib · SQLite |

### 🛠️ At work

| Project | What it does | Stack |
|---|---|---|
| **AI talent matching** · *Telkomsel* | Semantic matching scores between candidates and roles. Cut screening time by **90%+**, rated 4.4–4.75/5 by HR experts, and registered as IP (HKI) | NLP · LLMs · Python |
| **Billboard × POI scoring** · *StickEarn* | Scores the points of interest around each billboard, plus Foursquare-based regional brand-impression analysis | BigQuery · Foursquare · H3 |
| **CCTV crowd counting** · *StickEarn* | People counting on CPU-only machines; moved from YOLOv11 tracking to MobileCount density estimation | PyTorch · OpenCV · GCP |
| **BigQuery → ClickHouse migration** · *StickEarn* | Airflow DAGs moving analytics workloads off BigQuery | Airflow · BigQuery · ClickHouse |
| **Mobility data audit** · *StickEarn* | Forensic audit of mobile ad-ID data: caught iOS over-representation, timezone batch spikes posing as commute peaks, and synthetic sources | SQL · Python |
| **Learner analytics** · *Solve Education!* | Research on **1M+ users** and a containerised pipeline feeding dashboards | Docker · Airflow · Metabase · Looker Studio |

<sub>Most of this lives in company or private repos, so ask me about it anytime.</sub>

### 🏅 Registered IP

> 📜 **Semantic Technologies for High-Precision Talent Matching in Modern Recruitment**<br/>
> Registered intellectual property (HKI) · No. **EC002025068378**<br/>
> <sub>The research behind the AI talent-matching system built at Telkomsel.</sub>

### 🧭 Journey

| When | Where | Role |
|---|---|---|
| Jul 2026 – now | 🏦 BNI | Officer Development Program · Data Analytics |
| Jan – Jul 2026 | 📍 StickEarn | Data Analyst |
| Feb – Jul 2025 | 📡 Telkomsel | Research Intern |
| Jul 2024 – Jan 2025 | 📚 Solve Education! Foundation | Data Analyst → Program Assistant |
| Feb – Jul 2024 | 📡 Telkomsel | Data Analytics Intern (MSIB 6) |
| 2021 – 2025 | 🎓 Telkom University | B.Sc. Data Science |

### 🤝 Organizations

| When | Where | Role |
|---|---|---|
| 2023 – 2024 | HIMADS Telkom University | **Vice Chairman** · also Head of PR for GALAKSI (leadership program), Head of Logistics for Campus Life Introduction, Event Supervisor, and mentor for AI and Algorithm Complexity courses |
| 2024 | Telkomsel MSIB 6 | **Head of Representative** for the intern cohort |
| 2022 – 2023 | Telkom University | **Head of the Orientation Program (PKKMB)** for Data Science, Market Day logistics, and community service on personal-data protection |

### 🧰 Toolbox

**Data & Cloud**<br/>
<img src="https://img.shields.io/badge/BigQuery-669DF6?style=for-the-badge&logo=googlebigquery&logoColor=white"/>
<img src="https://img.shields.io/badge/Google%20Cloud-4285F4?style=for-the-badge&logo=googlecloud&logoColor=white"/>
<img src="https://img.shields.io/badge/Airflow-017CEE?style=for-the-badge&logo=apacheairflow&logoColor=white"/>
<img src="https://img.shields.io/badge/ClickHouse-FFCC01?style=for-the-badge&logo=clickhouse&logoColor=black"/>
<img src="https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white"/>
<img src="https://img.shields.io/badge/Neo4j-4581C3?style=for-the-badge&logo=neo4j&logoColor=white"/>
<img src="https://img.shields.io/badge/Redis-DC382D?style=for-the-badge&logo=redis&logoColor=white"/>
<img src="https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white"/>
<img src="https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white"/>

**ML, NLP & Vision**<br/>
<img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white"/>
<img src="https://img.shields.io/badge/PyTorch-EE4C2C?style=for-the-badge&logo=pytorch&logoColor=white"/>
<img src="https://img.shields.io/badge/Keras-D00000?style=for-the-badge&logo=keras&logoColor=white"/>
<img src="https://img.shields.io/badge/scikit--learn-F7931E?style=for-the-badge&logo=scikitlearn&logoColor=white"/>
<img src="https://img.shields.io/badge/OpenCV-5C3EE8?style=for-the-badge&logo=opencv&logoColor=white"/>
<img src="https://img.shields.io/badge/LLMs%20%26%20RAG-134E5E?style=for-the-badge"/>

**Geospatial & BI**<br/>
<img src="https://img.shields.io/badge/Foursquare-3333FF?style=for-the-badge&logo=foursquare&logoColor=white"/>
<img src="https://img.shields.io/badge/H3-71B280?style=for-the-badge"/>
<img src="https://img.shields.io/badge/Metabase-509EE3?style=for-the-badge&logo=metabase&logoColor=white"/>
<img src="https://img.shields.io/badge/Looker%20Studio-4285F4?style=for-the-badge&logo=looker&logoColor=white"/>
<img src="https://img.shields.io/badge/Tableau-E97627?style=for-the-badge&logo=tableau&logoColor=white"/>
<img src="https://img.shields.io/badge/Power%20BI-F2C811?style=for-the-badge&logo=powerbi&logoColor=black"/>

### 📈 On GitHub

<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/JaxToon/JaxToon/output/stats-dark.svg"/>
    <img height="160" src="https://raw.githubusercontent.com/JaxToon/JaxToon/output/stats.svg" alt="GitHub stats"/>
  </picture>
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/JaxToon/JaxToon/output/langs-dark.svg"/>
    <img height="160" src="https://raw.githubusercontent.com/JaxToon/JaxToon/output/langs.svg" alt="Most used languages"/>
  </picture>
</p>

<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/JaxToon/JaxToon/output/github-snake-dark.svg"/>
    <img src="https://raw.githubusercontent.com/JaxToon/JaxToon/output/github-snake.svg" alt="snake eating my contribution graph"/>
  </picture>
</p>

<p align="center"><i>Always happy to talk about maps, models, or the next thing worth exploring.</i></p>

<!-- Footer -->
<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&height=110&color=0:134E5E,100:71B280&section=footer" alt="footer"/>
</p>
