import pandas as pd

data = {"Name": ["A", "B", "C"], "Age": [25, 30, 35], "Salary": [40000, 50000, 60000]}
df = pd.DataFrame(data)
print(df)
print("\nAverage Salary:", df["Salary"].mean())
