import requests
import pandas as pd
import matplotlib.pyplot as plt

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

# Plot country comparisons for each indicator
for ind_label in indicators.values():
    fig, ax = plt.subplots(figsize=(12, 6))
    subset = all_data[all_data['indicator'] == ind_label]
    for country in countries.values():
        country_data = subset[subset['country'] == country].sort_values('year')
        ax.plot(country_data['year'], country_data['value'], marker='o', label=country, linewidth=2)
    ax.set_title(f'{ind_label} by Country', fontsize=14, fontweight='bold')
    ax.set_xlabel('Year')
    ax.set_ylabel(ind_label)
    ax.legend()
    ax.grid(True, alpha=0.3)
    plt.tight_layout()
    filename = ind_label.replace(' ', '_').replace('(%)', '').replace('/', '').strip() + '.png'
    plt.savefig(filename, dpi=150, bbox_inches='tight')
    plt.close()
    print(f"Saved {filename}")
    