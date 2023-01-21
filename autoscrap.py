import pandas as pd

url = 'https://pkg.openindiana.org/dev/en/catalog.shtml?version=0.5.11%2C0.5.11-0.148&action=Browse'


# Use pandas to read the HTML table
dfs = pd.read_html(url)

# Extract the first table
df = dfs[0]

# Filter the rows that have ':' in package version 
df_filtered = df[df['Version'].str.contains(':')]

# Save the data into an excel file
df_filtered.to_excel('package openindiana/148.xlsx', index=False)
