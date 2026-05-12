# SME Financing Gap in Sub-Saharan Africa

## Overview
This project looks at financial access and private credit trends across five Sub-Saharan African markets - Kenya, Nigeria, Ghana, Ethiopia, and Rwanda. The central question is simple: how large is the gap between what businesses in these countries can actually access and what a functioning credit market would provide? All data is pulled live from the World Bank API.

## Motivation
I built this after working on investor relations for a blended finance fund deploying capital into water and sanitation SMEs across Sub-Saharan Africa. I kept coming across the concept of the "missing middle" - the idea that SMEs in the region are too large for microfinance but too risky for commercial banks, leaving them with almost no access to growth capital. I wanted to quantify that gap myself.

## What the Data Shows

Financial inclusion has grown fast, but unevenly. Kenya has gone from 42% account ownership in 2011 to 90% in 2024, largely off the back of mobile money. Ethiopia remains well below 50%, while Nigeria has reached around 63% but still lags behind Kenya and Ghana, pointing to uneven progress across the region.

The gender gap has not closed. Female account ownership has risen across all five markets but consistently sits below overall ownership, meaning the gains in financial inclusion have not been equally shared.

Private credit tells the real story. Across these five countries, private credit as a share of GDP sits between 9% and 32%. The global average across all countries is around 50% of GDP - meaning that in a typical economy, private sector lending is roughly half the size of the entire economy. In Kenya, the most financially developed market in this group, it sits at 32%. In Ghana and Nigeria it is closer to 10%. That gap of 18 to 41 percentage points is not a rounding error - it represents a structural failure of credit markets to reach businesses that need capital to grow, and it is exactly why blended finance structures exist. Note: Ethiopia is excluded from the financing gap chart as the most recent World Bank private credit data available is from 2008. Account ownership data for Rwanda is from 2017, the most recent available in the World Bank Findex for that country.

## Charts
- [Account Ownership by Country](https://kr6243.github.io/sme-africa-analysis/Account_Ownership_.html)
- [Female Account Ownership by Country](https://kr6243.github.io/sme-africa-analysis/Female_Account_Ownership_.html)
- [Private Credit by Country](https://kr6243.github.io/sme-africa-analysis/private_credit.html)
- [SME Financing Gap by Country](https://kr6243.github.io/sme-africa-analysis/financing_gap.html)

## Methodology and Limitations

The data comes from the World Bank Open Data API, pulled live every time the script runs. Three indicators are used:

- Account ownership at a financial institution or mobile money provider (% of population aged 15+), from the Global Findex database
- Female account ownership, from the same source
- Domestic credit to private sector by banks (% of GDP), from IMF International Financial Statistics

The 50% benchmark in the financing gap chart is the World Bank's global average for private credit to GDP across all income levels.

A few things worth flagging on the data itself. The Findex survey only runs every three years, so the account ownership trend lines connect points from 2011, 2014, 2017, 2021 and 2024. Years in between are interpolated rather than measured. Rwanda's most recent figure is from 2017 because that's the latest available in the database. Ethiopia is excluded from the financing gap chart entirely because the most recent private credit data the World Bank has for the country is from 2008, which is too far out of date to be a fair current comparison. Private credit figures themselves come with a one to two year lag depending on the country, with Nigeria's most recent from 2022, Kenya from 2023, and Ghana and Rwanda from 2024.

The 50% benchmark is a global average and hides a lot of variation. Middle income countries typically sit closer to 60-80%, and high income countries average around 130%, so the gap looks different depending on which comparison you're making.

## What Closing the Gap Would Mean

The financing gap is easy to dismiss as abstract until you put a dollar figure on it. Below is a rough estimate of how much additional private credit each market would need to reach the 50% global benchmark, calculated as the percentage point gap multiplied by each country's most recent GDP.

| Country | Current Private Credit (% of GDP) | Gap to 50% | Approx. GDP (USD bn) | Additional Credit Needed (USD bn) |
|---------|----------------------------------:|-----------:|---------------------:|----------------------------------:|
| Kenya   | 31.8% | 18.2 pp | 113 | 21 |
| Rwanda  | 22.6% | 27.4 pp | 14  | 4  |
| Nigeria | 9.6%  | 40.4 pp | 363 | 147 |
| Ghana   | 9.0%  | 41.0 pp | 76  | 31 |

For Nigeria alone, the gap represents roughly $147 billion in additional credit that businesses cannot currently access. Across these four markets, the gap totals over $200 billion. That figure isn't a forecast, it's a rough scale of the problem, and it's the kind of number that helps explain why commercial banks alone cannot close it and why structures like blended finance exist.

GDP figures are approximate, drawn from World Bank latest available data. These are illustrative rather than precise forecasts.

## Tech Stack
Python, Pandas, Plotly, World Bank API