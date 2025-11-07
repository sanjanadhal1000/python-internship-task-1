import pandas as pd
data = {"Name": ["A", "B", "C", "B"], "Score": [90, None, 85, 78]}
df = pd.DataFrame(data)

df.drop_duplicates(inplace=True)
df["Score"].fillna(df["Score"].mean(), inplace=True)

print("Cleaned Data:\n", df)
print(f"Average Score: {df["Score"].mean():.2f}")
