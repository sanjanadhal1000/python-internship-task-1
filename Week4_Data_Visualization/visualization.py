import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Create simple data
data = {"Age": [22, 25, 47, 52, 46, 56],
        "Salary": [20000, 25000, 45000, 50000, 48000, 52000]}

df = pd.DataFrame(data)

# Scatter plot
plt.scatter(df["Age"], df["Salary"])
plt.title("Age vs Salary")
plt.xlabel("Age")
plt.ylabel("Salary")
plt.show()

# Seaborn heatmap
sns.heatmap(df.corr(), annot=True, cmap="coolwarm")
plt.title("Correlation Heatmap")
plt.show()
