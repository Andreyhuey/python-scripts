import matplotlib.pyplot as plt
import os

# Data
items = [
    "Rice", "Beans", "Vegetable Oil", "Chicken", "Eggs", "Milk", 
    "Bread", "Tomatoes", "Onions", "Pepper", "Fish", "Yam", 
    "Garri", "Soap", "Detergent", "Salt", "Sugar", "Groundnut Oil", 
    "Spices", "Fruits"
]
prices = [
    25000, 7500, 6000, 6000, 2400, 3000, 1600, 2400, 1400, 500, 5000, 
    2100, 3000, 1500, 1200, 200, 800, 3000, 2000, 5000
]

# Create a bar chart
plt.figure(figsize=(12, 8))
plt.barh(items, prices, color='skyblue')
plt.xlabel('Price (₦)')
plt.ylabel('Items')
plt.title('Monthly Grocery Budget Distribution (₦50,000)')
plt.grid(axis='x', linestyle='--', alpha=0.7)

# Build folder path
build_folder = 'build'

# Ensure the build folder exists
if not os.path.exists(build_folder):
    os.makedirs(build_folder)

# Save the bar chart as a PNG image in the build folder
output_path = os.path.join(build_folder, 'grocery_budget_distribution_bar.png')
plt.savefig(output_path)
plt.close()
