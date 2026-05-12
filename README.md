# The SME Financing Gap in Sub-Saharan Africa

## What This Project Is

Sub-Saharan Africa has a structural problem with credit. Across the region, private credit as a share of GDP sits well below global averages, leaving small and medium businesses systematically underfunded. The "missing middle" — companies too large for microfinance but too risky for commercial banks — is one of the largest unaddressed financing gaps in the global economy, and it is the reason structures like blended finance exist.

This project quantifies the scale of that gap, calculates what closing it would mean in dollar terms, and tests econometrically whether private credit deepening has historically translated into faster growth across the region. All data is pulled live from the World Bank Open Data API.

## Why I Built It

I worked at Water Unite, a blended finance fund investing in water and sanitation SMEs across Sub-Saharan Africa, and kept hearing about the "missing middle" as a structural barrier. I wanted to see the numbers myself rather than take them on trust, and to understand whether the case for closing the gap holds up under proper empirical scrutiny.

## Interactive Charts

- [Account Ownership by Country](https://kr6243.github.io/sme-africa-analysis/Account_Ownership_.html)
- [Female Account Ownership by Country](https://kr6243.github.io/sme-africa-analysis/Female_Account_Ownership_.html)
- [Private Credit by Country](https://kr6243.github.io/sme-africa-analysis/private_credit.html)
- [SME Financing Gap by Country](https://kr6243.github.io/sme-africa-analysis/financing_gap.html)

## Key Findings

**The gap is large.** Across Kenya, Nigeria, Ghana, and Rwanda, private credit as a share of GDP sits between 9% and 32%. The global average is around 50%. Closing that gap to the global benchmark would require an additional $200 billion in private credit across these four markets alone.

**Financial inclusion has improved, but unevenly.** Account ownership in Kenya has grown from 42% in 2011 to 90% in 2024, driven largely by mobile money. Ghana and Nigeria have also progressed substantially. Ethiopia remains well below the regional average, and the gender gap persists across every country in the sample.

**The relationship between credit and growth is more nuanced than headlines suggest.** A two-way fixed effects panel regression across 40 Sub-Saharan African countries over six decades finds no statistically significant link between lagged private credit and subsequent GDP growth, once inflation, trade openness, and government spending are controlled for. The result holds across subsamples and a non-linear specification. Growth in the region has been shaped more by macroeconomic stability and openness than by credit access alone.

This does not mean the financing gap is unimportant. It means the channel from credit to aggregate growth is conditional on the broader environment, and any financing intervention is operating in a system where other factors matter at least as much.

## Methodology

Data is pulled live from the World Bank Open Data API across five indicators: account ownership, female account ownership, private credit to GDP, GDP growth, inflation, trade openness, and government consumption. The country-level analysis covers Kenya, Nigeria, Ghana, Ethiopia, and Rwanda. The panel regression expands to all 40 Sub-Saharan African countries with complete data.

The regression uses a two-way fixed effects panel estimator with standard errors clustered at the country level. Private credit is lagged by one year to address simultaneity. Robustness checks include subsample analysis (post-2000, excluding the 2008-2009 GFC) and a quadratic specification to test for non-linearities.

## Limitations

The Findex survey runs every three years, so account ownership trend lines connect points from 2011, 2014, 2017, 2021 and 2024 with interpolation in between. Rwanda's most recent account ownership figure is from 2017, and Ethiopia is excluded from the financing gap chart because its most recent private credit data is from 2008. Private credit figures themselves come with a one to two year reporting lag. The 50% benchmark is a global average; middle-income countries typically sit closer to 60-80% and high-income closer to 130%, so comparisons vary depending on the reference group used.

## Tech Stack

Python, pandas, statsmodels, linearmodels, Plotly, World Bank Open Data API.

## Repository

The full analysis lives in `sme_africa_analysis.ipynb`. Live charts are deployed via GitHub Pages.