import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Create folders if not exist
os.makedirs("visuals", exist_ok=True)

# Load the dataset
file_path = "data/sales_data.csv"
df = pd.read_csv(file_path)


# Display basic info
print("🔍 Dataset Overview:")
print(df.info())
print(df.head())

# 1️⃣ Total Sales by Product
product_sales = df.groupby("Product")["Revenue"].sum().sort_values(ascending=False)
print("\n🏆 Total Sales by Product:\n", product_sales)

plt.figure(figsize=(8, 5))
sns.barplot(x=product_sales.index, y=product_sales.values, palette="viridis")
plt.title("Total Sales by Product")
plt.xlabel("Product")
plt.ylabel("Total Revenue")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("visuals/sales_by_product.png")
plt.show()

# 2️⃣ Sales Trends Over Time
df["Date"] = pd.to_datetime(df["Date"])
daily_sales = df.groupby("Date")["Revenue"].sum()

plt.figure(figsize=(10, 5))
daily_sales.plot(color="darkorange", marker="o")
plt.title("Sales Trends Over Time")
plt.xlabel("Date")
plt.ylabel("Revenue")
plt.grid(True)
plt.tight_layout()
plt.savefig("visuals/sales_trends_over_time.png")
plt.show()

# 3️⃣ Sales by Region
region_sales = df.groupby("Region")["Revenue"].sum()

plt.figure(figsize=(6, 4))
region_sales.plot(kind="pie", autopct="%1.1f%%", colors=sns.color_palette("pastel"))
plt.title("Sales by Region")
plt.ylabel("")  # Hide y-label
plt.tight_layout()
plt.savefig("visuals/sales_by_region.png")
plt.show()

# 4️⃣ Top Salespersons
salesperson_performance = df.groupby("Salesperson")["Revenue"].sum().sort_values(ascending=False)

plt.figure(figsize=(7, 4))
sns.barplot(x=salesperson_performance.index, y=salesperson_performance.values, palette="magma")
plt.title("Top Salespersons by Revenue")
plt.xlabel("Salesperson")
plt.ylabel("Revenue")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("visuals/sales_by_salesperson.png")
plt.show()

print("\n🎯 Analysis Complete! Check the 'visuals' folder for charts.")
