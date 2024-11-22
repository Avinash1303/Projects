# Step 1: Import Libraries
import pandas as pd
import matplotlib.pyplot as plt

# Step 2: Load the Dataset
data = pd.read_csv("supermarket_sales - Sheet1.csv")

# Step 3: Data Overview
print(data.info())  # Data summary
print(data.head())  # First few rows of data

# Step 4: Data Cleaning
# Check for missing values
print(data.isnull().sum())

# Drop rows with missing values (if any)
data = data.dropna()

# Convert Date column to datetime
data['Date'] = pd.to_datetime(data['Date'])

# Step 5: Data Analysis

# 5.1 Sales Trends Over Time
# Group by date and sum the total sales
daily_sales = data.groupby('Date')['Total'].sum()

# Plot daily sales trend
daily_sales.plot(figsize=(10, 5), title="Daily Sales Trend", color='b')
plt.ylabel("Total Sales")
plt.show()

# 5.2 Product Line Performance
# Calculate total sales for each product line
product_sales = data.groupby('Product line')['Total'].sum().sort_values()

# Plot sales by product line
product_sales.plot(kind='barh', title="Sales by Product Line")
plt.xlabel("Total Sales")
plt.show()

# 5.3 Gender-Wise Sales Distribution
# Gender-wise total sales
gender_sales = data.groupby('Gender')['Total'].sum()
gender_sales.plot(kind='pie', autopct='%1.1f%%', title="Sales Distribution by Gender")
plt.ylabel("")
plt.show()

# 5.4 Sales by Branch
# Sales by Branch
branch_sales = data.groupby('Branch')['Total'].sum()
branch_sales.plot(kind='bar', title="Total Sales by Branch", color=['#ff9999','#66b3ff','#99ff99'])
plt.xlabel("Branch")
plt.ylabel("Total Sales")
plt.show()

# 5.5 Sales by Payment Method
# Sales by Payment Method
payment_sales = data.groupby('Payment')['Total'].sum()
payment_sales.plot(kind='bar', color=['#ffcc99','#c2c2f0','#ffb3e6'], title="Sales by Payment Method")
plt.xlabel("Payment Method")
plt.ylabel("Total Sales")
plt.show()

# 5.6 Customer Type vs Spending
# Average spending by customer type
loyalty_sales = data.groupby('Customer type')['Total'].mean()
loyalty_sales.plot(kind='bar', color=['#ff6666','#66b2ff'], title="Average Spending by Customer Type")
plt.xlabel("Customer Type")
plt.ylabel("Average Spending")
plt.show()

# 5.7 Monthly Sales Trend
# Add 'Month' column
data['Month'] = data['Date'].dt.to_period('M')

# Group by month and sum the sales
monthly_sales = data.groupby('Month')['Total'].sum()

# Plot monthly sales trend
monthly_sales.plot(title="Monthly Sales Trend", color='purple')
plt.xlabel("Month")
plt.ylabel("Total Sales")
plt.show()

# Step 6: Final Insights
# You can print summary findings here, for example:
print("Key Insights:")
print("- Top performing product lines: ", product_sales.index[-3:])
print("- Peak sales month: ", monthly_sales.idxmax())
print("- Customer type with highest average spending: ", loyalty_sales.idxmax())
