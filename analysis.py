import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
data = pd.read_csv("students.csv")

print("Student Data:")
print(data)

# Average marks
average = data["Marks"].mean()
print("\nAverage Marks:", average)

# Highest marks
highest = data["Marks"].max()
print("Highest Marks:", highest)

# Lowest marks
lowest = data["Marks"].min()
print("Lowest Marks:", lowest)

# Top student
top_student = data.loc[data["Marks"].idxmax()]["Name"]
print("Top Student:", top_student)

# Create bar chart
plt.bar(data["Name"], data["Marks"])
plt.title("Student Marks Analysis")
plt.xlabel("Students")
plt.ylabel("Marks")

plt.show()