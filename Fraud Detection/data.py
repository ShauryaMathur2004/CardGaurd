import pandas as pd
from sklearn.preprocessing import StandardScaler

df = pd.read_csv("Fraud Detection\compressed_data.csv")

#Drop duplicate rows (if any)
df.drop_duplicates(inplace=True)

#Standardize 'Amount' and 'Time' columns
scaler = StandardScaler()
df['Amount'] = scaler.fit_transform(df[['Amount']])
df['Time'] = scaler.fit_transform(df[['Time']])

#Rename 'Class' to 'IsFraud' 
df.rename(columns={'Class': 'IsFraud'}, inplace=True)

#Display first 5 rows of the cleaned data
print(df.head())
