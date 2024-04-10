import pandas as pd

# Read the first CSV file
df1 = pd.read_csv('./dataset/credit_data.csv')

# Read the second CSV file
df2 = pd.read_csv('./dataset/results.csv')

# Add column 'Id' to df2 and autonumber it starting from 0
df2['Id'] = range(len(df2))

print(df2)

# Merge df1 and df2 based on a common column
merged_df = pd.merge(df1, df2, on='Id')

# Print the merged dataframe
print(merged_df)

# Save the merged dataframe to a new CSV file
merged_df.to_csv('./dataset/dataset.csv', index=False)