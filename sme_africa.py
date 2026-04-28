import requests
import pandas as pd
import matplotlib.pyplot as plt
import plotly.graph_objects as go
from plotly.subplots import make_subplots

# Countries to analyse
countries = {
    'KE': 'Kenya',
    'NG': 'Nigeria',
    'GH': 'Ghana',
    'ET': 'Ethiopia',
    'RW': 'Rwanda'
}

# Indicators to pull
indicators = {
    'FX.OWN.TOTL.ZS': 'Account Ownership (%)',
    'FX.OWN.TOTL.FE.ZS': 'Female Account Ownership (%)',
    'FS.AST.PRVT.GD.ZS': 'Private Credit (% of GDP)',
}

def fetch_indicator(country_code, indicator_code, country_name, indicator_label):
    url = f"https://api.worldbank.org/v2/country/{country_code}/indicator/{indicator_code}?format=json&per_page=100"
    response = requests.get(url)
    parsed = response.json()
    if len(parsed) < 2 or parsed[1] is None:
        return pd.DataFrame()
    data = parsed[1]
    df = pd.DataFrame([{'year': int(d['date']), 'value': d['value']} for d in data])
    df = df.dropna()
    df['country'] = country_name
    df['indicator'] = indicator_label
    return df

# Fetch all data
all_data = pd.concat([
    fetch_indicator(code, ind_code, name, ind_label)
    for code, name in countries.items()
    for ind_code, ind_label in indicators.items()
])

print(all_data)
print("\nData pulled successfully!")

colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd']

# Country comparison charts for each indicator
for ind_label in indicators.values():
    fig = go.Figure()
    subset = all_data[all_data['indicator'] == ind_label]
    for i, country in enumerate(countries.values()):
        country_data = subset[subset['country'] == country].sort_values('year')
        fig.add_trace(go.Scatter(
            x=country_data['year'],
            y=country_data['value'],
            name=country,
            mode='lines+markers',
            line=dict(width=2.5, color=colors[i]),
            marker=dict(size=7)
        ))
    fig.update_layout(
        title=dict(text=f'{ind_label} by Country', font=dict(size=18)),
        xaxis_title='Year',
        yaxis_title=ind_label,
        template='plotly_white',
        legend=dict(orientation='h', yanchor='bottom', y=1.02, xanchor='right', x=1),
        hovermode='x unified',
        width=1000,
        height=550
    )
    filename = ind_label.replace(' ', '_').replace('(%)', '').replace('/', '').strip() + '.html'
    fig.write_html(filename)
    print(f"Saved {filename}")

# Financing gap bar chart
GLOBAL_BENCHMARK = 130

latest_credit = (
    all_data[all_data['indicator'] == 'Private Credit (% of GDP)']
    .sort_values('year', ascending=False)
    .groupby('country')
    .first()
    .reset_index()
)

# Remove Ethiopia - most recent World Bank data is 2008, too old for a current comparison
latest_credit = latest_credit[latest_credit['country'] != 'Ethiopia']

latest_credit['gap'] = GLOBAL_BENCHMARK - latest_credit['value']
latest_credit = latest_credit.sort_values('gap', ascending=False)

fig = go.Figure(go.Bar(
    x=latest_credit['country'],
    y=latest_credit['gap'],
    marker_color=colors,
    text=latest_credit['gap'].apply(lambda x: f'{x:.1f}%'),
    textposition='outside'
))

fig.update_layout(
    title=dict(text='SME Financing Gap by Country<br><sup>Distance from Global Average Private Credit (% of GDP)</sup>', font=dict(size=18)),
    xaxis_title='Country',
    yaxis_title='Financing Gap (% of GDP)',
    template='plotly_white',
    width=900,
    height=550
)

fig.write_html('financing_gap.html')
print("Saved financing_gap.html")
