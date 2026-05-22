# Ireland Housing Affordability Dashboard — Focus Ireland

**End-to-end data analytics project | Python · Power BI · CSO HPA02 Dataset**

> Analysed 184,596 Irish residential property transactions (2010–2024) for Focus Ireland, a national homelessness charity — delivering an interactive Power BI dashboard to identify affordability pressure, regional price trends, and investor activity across all 26 counties.

---

## Table of Contents
- [Project Overview](#project-overview)
- [Business Problem](#business-problem)
- [Dataset](#dataset)
- [Project Workflow](#project-workflow)
- [Key Findings](#key-findings)
- [SDG Alignment](#sdg-alignment)
- [Tools & Technologies](#tools--technologies)
- [Folder Structure](#folder-structure)
- [How to Run](#how-to-run)
- [Skills Demonstrated](#skills-demonstrated)

---

## Project Overview

Focus Ireland is a national charity that prevents and solves homelessness across Ireland. This project analysed the CSO HPA02 Residential Dwelling Property Transactions dataset to identify where housing is least affordable, where investor activity is highest, and where Focus Ireland can most effectively direct its resources.

**Association:** University College Cork · MSc Business Analytics  
**Client:** Focus Ireland

---

## Business Problem

> "How can housing transaction data be used to identify where affordability pressure is highest across Ireland, and where Focus Ireland should prioritise its prevention and rehousing efforts?"

---

## Dataset

| Attribute | Detail |
|-----------|--------|
| Source | CSO HPA02 — Residential Dwelling Property Transactions |
| Raw records | 186,624 rows |
| Clean records | 184,596 rows (removed 2,028 missing VALUE rows) |
| Period | 2010–2024 |
| Coverage | All 26 Irish counties + Dublin sub-regions |

**Key features:** County · Year · Dwelling Status · Type of Buyer · Type of Sale · Mean Sale Price · Median Sale Price · Value of Sales · Volume of Sales

---

## Project Workflow

### 1. Data Cleaning — Python
- Loaded raw HPA02 CSV using Pandas
- Dropped 2,028 rows with missing VALUE entries
- Standardised all column names to snake_case
- Fixed data types — Year as integer, VALUE as numeric
- Standardised categorical values for consistent grouping
- Created 3 summary tables for Power BI ingestion
- Exported 4 clean CSV files to cleaned_data folder

### 2. Dashboard — Power BI
Built a relational data model with fact and dimension tables and 6 interactive visuals:

| Visual | Purpose |
|--------|---------|
| County bar chart | Volume of sales by county — identifies high-pressure areas |
| Stacked area chart | Transaction value by year and dwelling status |
| Donut chart | Share of sales by buyer type — highlights investor activity |
| Combo chart | Median price vs sales volume over time |
| Scatter chart | Price by dwelling status and year |
| Combo chart | Annual median vs mean price — shows luxury sale effect |

---

## Key Findings

| Insight | Value |
|---------|-------|
| Highest median price (2024) | Dublin — EUR 475,000 |
| Lowest median price (2024) | Donegal — EUR 180,000 |
| Price gap | EUR 295,000 between highest and lowest county |
| Price trend | U-shaped — fell 2010–2013, rising sharply to 2024 |
| New vs existing | New homes consistently 15–25% more expensive |
| Investor activity | Non-household buyers hold significant share in high-price counties |

---

## SDG Alignment

| SDG | Target | Relevance |
|-----|--------|-----------|
| SDG 11 — Sustainable Cities | 11.1 — Safe affordable housing | Core focus — mapping affordability gaps across Ireland |
| SDG 1 — No Poverty | 1.4 — Equal access to resources | Investor activity pushing low-income households out of ownership |

---

## Tools & Technologies

| Category | Tools |
|----------|-------|
| Data Cleaning | Python · Pandas · NumPy |
| Environment | VS Code |
| Business Intelligence | Power BI · DAX · Relational Data Model |
| Data Source | CSO HPA02 DataHub |
| Reporting | PDF Report |

---

## Folder Structure

Ireland-Housing-Affordability-Dashboard/
│
├── ireland_housing_cleaning.py
├── HPA02.csv
├── cleaned_data/
│   ├── HPA02_cleaned.csv
│   ├── county_summary.csv
│   ├── dwelling_summary.csv
│   └── buyer_summary.csv
├── Ireland_Housing_Dashboard.pbix
├── IS6051-Group_3R.pdf
├── requirements.txt
├── LICENSE
└── README.md

---

## How to Run

**Step 1 — Clone the repository**
```bash
git clone https://github.com/Khushi-Dhargawe/Ireland-Housing-Affordability-Dashboard.git
```

**Step 2 — Install dependencies**
```bash
pip install -r requirements.txt
```

**Step 3 — Run the cleaning script**
```bash
python ireland_housing_cleaning.py
```

**Step 4 — Open Power BI dashboard**

Open `Ireland_Housing_Dashboard.pbix` in Power BI Desktop and refresh the data source.

---

## Business Recommendations

1. **Prioritise Dublin and Cork** for homelessness prevention and rapid-rehousing
2. **Target Donegal, Leitrim, Longford** for acquisitions — lower prices stretch budget further
3. **Focus on existing properties** — new builds are 15–25% more expensive
4. **Advocate for investor restrictions** — non-household buyers compete with low-income households
5. **Update dashboard regularly** with new CSO releases to monitor emerging trends

---

## Skills Demonstrated

`Data Cleaning` `Python` `Pandas` `Power BI` `DAX` `Data Modelling` `EDA`
`Data Visualisation` `Business Analysis` `SDG Alignment` `Stakeholder Reporting`
`Housing Analytics` `Policy Recommendations`

---

*Project completed as part of MSc Business Analytics — University College Cork*  
*Client: Focus Ireland | Dataset: CSO HPA02*

