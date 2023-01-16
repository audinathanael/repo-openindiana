import pandas as pd

# Read the Excel file into a dataframe
df = pd.read_excel("package_data.xlsx")

df['Name'] = 'pkg://openindiana.org/' + df['Name']+"/"+df["Version"]

df.drop("Version", axis=1, inplace=True)
data= df.to_string(index=False,header=False)

# data_with_text = data.replace("\n","df['Name'] = 'pkg://openindiana.org/' + df['Name']+'/'+df['Version']")

# # Write the string to a text file
with open("package_data.txt", "w") as f:
        f.write(data)
    
