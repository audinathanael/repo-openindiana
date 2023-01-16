import pandas as pd

url = 'https://pkg.openindiana.org/dev/en/catalog.shtml'

# Use pandas to read the HTML table
dfs = pd.read_html(url)

# Extract the first table
df = dfs[0]

# Filter the rows that have ':' in package version 
df_filtered = df[df['Version'].str.contains(':')]

# Save the data into an excel file
df_filtered.to_excel('package_data.xlsx', index=False)
