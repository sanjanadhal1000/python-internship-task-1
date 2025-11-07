# Calculate average temperature from a week's data

temps = [float(x) for x in input("Enter 7 temperatures separated by space: ").split()]
avg_temp = sum(temps) / len(temps)
print(f"Average Temperature of the week: {avg_temp:.2f}°C")
