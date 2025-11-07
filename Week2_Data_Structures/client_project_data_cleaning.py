# Remove duplicates and filter data

data = ["apple", "banana", "apple", "orange", "banana"]
unique_data = list(set(data))
filtered_data = [item for item in unique_data if len(item) > 5]

print("Unique Data:", unique_data)
print("Filtered Data:", filtered_data)
