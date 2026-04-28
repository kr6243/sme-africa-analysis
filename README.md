# SME Financing Gap in Sub-Saharan Africa

## Overview
This project looks at financial access and private credit trends across five Sub-Saharan African markets - Kenya, Nigeria, Ghana, Ethiopia, and Rwanda. The central question is simple: how large is the gap between what businesses in these countries can actually access and what a functioning credit market would provide? All data is pulled live from the World Bank API.

## Motivation
I built this after working on investor relations for a blended finance fund deploying capital into water and sanitation SMEs across Sub-Saharan Africa. I kept coming across the concept of the "missing middle" - the idea that SMEs in the region are too large for microfinance but too risky for commercial banks, leaving them with almost no access to growth capital. I wanted to quantify that gap myself.

## What the Data Shows

Financial inclusion has grown fast, but unevenly. Kenya has gone from 42% account ownership in 2011 to 90% in 2024, largely off the back of mobile money. Ethiopia remains well below 50%, while Nigeria has reached around 63% but still lags behind Kenya and Ghana, pointing to uneven progress across the region.

The gender gap has not closed. Female account ownership has risen across all five markets but consistently sits below overall ownership, meaning the gains in financial inclusion have not been equally shared.

Private credit tells the real story. Across these five countries, private credit as a share of GDP sits between 9% and 32%. The global average across all countries is around 50% of GDP - meaning that in a typical economy, private sector lending is roughly half the size of the entire economy. In Kenya, the most financially developed market in this group, it sits at 32%. In Ghana and Nigeria it is closer to 10%. That gap of 18 to 41 percentage points is not a rounding error - it represents a structural failure of credit markets to reach businesses that need capital to grow, and it is exactly why blended finance structures exist. Note: Ethiopia is excluded from the financing gap chart as the most recent World Bank private credit data available is from 2008.

## Charts
- [Account Ownership by Country](https://kr6243.github.io/sme-africa-analysis/Account_Ownership_.html)
- [Female Account Ownership by Country](https://kr6243.github.io/sme-africa-analysis/Female_Account_Ownership_.html)
- [Private Credit by Country](https://kr6243.github.io/sme-africa-analysis/Private_Credit_(%_of_GDP).html)
- [SME Financing Gap by Country](https://kr6243.github.io/sme-africa-analysis/financing_gap.html)

## Tech Stack
Python, Pandas, Plotly, World Bank API