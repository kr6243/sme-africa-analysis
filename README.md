# SME Financing Gap in Sub-Saharan Africa

## Overview
This project looks at financial access and private credit trends across five Sub-Saharan African markets - Kenya, Nigeria, Ghana, Ethiopia, and Rwanda. The central question is simple: how large is the gap between what businesses in these countries can actually access and what a functioning credit market would provide? All data is pulled live from the World Bank API.

## Motivation
I built this after working on investor relations for a blended finance fund deploying capital into water and sanitation SMEs across Sub-Saharan Africa. I kept coming across the concept of the "missing middle" - the idea that SMEs in the region are too large for microfinance but too risky for commercial banks, leaving them with almost no access to growth capital. I wanted to quantify that gap myself.

## What the Data Shows

Financial inclusion has grown fast, but unevenly. Kenya has gone from 42% account ownership in 2011 to 90% in 2024, largely off the back of mobile money. Ethiopia and Nigeria are still well below 50%, pointing to deeper regulatory and infrastructure barriers.

The gender gap has not closed. Female account ownership has risen across all five markets but consistently sits below overall ownership, meaning the gains in financial inclusion have not been equally shared.

Private credit tells the real story. Across these five countries, private credit as a share of GDP sits between 9% and 32%. The global average is around 130%. That gap of 98 to 121 percentage points is not a rounding error - it represents a structural failure of credit markets to reach businesses that need capital to grow. It is also exactly why blended finance exists.

## Charts
- [Account Ownership by Country](https://kr6243.github.io/sme-africa-analysis/Account_Ownership_.html)
- [Female Account Ownership by Country](https://kr6243.github.io/sme-africa-analysis/Female_Account_Ownership_.html)
- [Private Credit by Country](https://kr6243.github.io/sme-africa-analysis/Private_Credit_(%_of_GDP).html)
- [SME Financing Gap by Country](https://kr6243.github.io/sme-africa-analysis/financing_gap.html)

## Tech Stack
Python, Pandas, Plotly, World Bank API