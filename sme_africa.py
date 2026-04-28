import requests
import pandas as pd
import matplotlib.pyplot as plt

indicators = {
    'FX.OWN.TOTL.ZS': 'Account Ownership (%)',
    'FX.OWN.TOTL.FE.ZS': 'Female Account Ownership (%)',
    'FS.AST.PRVT.GD.ZS': 'Private Credit (% of GDP)',
    'SL.UEM.TOTL.ZS': 'Unemployment Rate (%)'
}

def fetch_indicator(indicator_code, label):
    url = f"https://api.worldbank.org/v2/country/ZF/indicator/{indicator_code}?format=json&per_page=100"
    response = requests.get(url)
    parsed = response.json()
    if len(parsed) < 2 or parsed[1] is None:
        print(f"No data found for {label}, skipping.")
        return pd.DataFrame()
    data = parsed[1]
    df = pd.DataFrame([{'year': int(d['date']), 'value': d['value']} for d in data])
    df = df.dropna()
    df['indicator'] = label
    return df

all_data = pd.concat([fetch_indicator(code, label) for code, label in indicators.items()])

print(all_data)
print("\nData pulled successfully!")

# Plot each indicator over time
fig, axes = plt.subplots(2, 2, figsize=(14, 10))
fig.suptitle('SME Financing & Financial Access in Sub-Saharan Africa', fontsize=16, fontweight='bold')

axes = axes.flatten()

for i, (indicator_label, ax) in enumerate(zip(indicators.values(), axes)):
    subset = all_data[all_data['indicator'] == indicator_label]
    subset = subset.sort_values('year')
    ax.plot(subset['year'], subset['value'], marker='o', linewidth=2, color='steelblue')
    ax.set_title(indicator_label, fontsize=11)
    ax.set_xlabel('Year')
    ax.set_ylabel('Value')
    ax.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('sme_africa_analysis.png', dpi=150, bbox_inches='tight')
plt.show()
print("Chart saved!")