# SME Financing Gap in Sub-Saharan Africa

## Overview
This project analyses financial access and SME financing trends across five key Sub-Saharan African markets — Kenya, Nigeria, Ghana, Ethiopia, and Rwanda — using World Bank data. It explores the structural funding gap that prevents small and medium enterprises in the region from accessing the capital they need to grow, the so-called "missing middle" that blended finance vehicles are working to address.

## Motivation
This project grew out of my interest in emerging market finance and impact investing, specifically the structural barriers that prevent SMEs in Sub-Saharan Africa from accessing growth capital. Having worked on investor relations for a blended finance fund focused on the region, I wanted to better understand the broader financing landscape through data.

## Data Source
All data is pulled directly from the World Bank API — no manual downloads required. The script fetches live data on:
- Account ownership (% of population ages 15+)
- Female account ownership (% of population ages 15+)
- Private credit (% of GDP)

## Key Findings

**Financial inclusion is growing but uneven**
Account ownership across the five countries has risen significantly since 2011, led by Kenya (42% to 90%) driven largely by mobile money adoption. Ethiopia and Nigeria lag behind, pointing to regulatory and infrastructure barriers.

**A persistent gender gap remains**
Female account ownership consistently trails overall ownership across all five markets, highlighting that financial inclusion gains have not been equally distributed.

**Private credit remains critically low**
Private credit as a % of GDP — a standard measure of credit accessibility for businesses — sits between 9% and 32% across these markets, compared to a global average of around 130%. This gap of 98-121 percentage points represents the structural financing shortfall that makes commercial lending to SMEs in the region unviable without catalytic capital.

**The case for blended finance**
The data illustrates why traditional commercial lenders alone cannot close this gap. Blended finance structures — combining first-loss capital from development-oriented sources with senior capital from private investors — are essential to de-risk lending in these markets and unlock private capital at scale.

## Charts
- `Account_Ownership_.png` — Account ownership trends by country (2011-2024)
- `Female_Account_Ownership_.png` — Female account ownership trends by country (2011-2024)
- `Private_Credit_(%_of_GDP).png` — Private credit trends by country
- `financing_gap.png` — Financing gap vs global average by country

## Tech Stack
- Python
- Pandas
- Matplotlib
- World Bank API