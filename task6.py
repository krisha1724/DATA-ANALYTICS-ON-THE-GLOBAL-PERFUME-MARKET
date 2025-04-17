import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.tsa.seasonal import seasonal_decompose

# Load the dataset
df = pd.read_csv("cleaned_perfume_data.csv")

# ------------------ 🔍 1. Data Profiling ------------------
print("🧾 Dataset Info:")
print(df.info())
print("\n📊 Descriptive Statistics:")
print(df.describe(include='all'))

# ------------------ 🧼 2. Handle Incomplete Data ------------------
# Convert the 'date' column to datetime (if it exists)
df['date'] = pd.to_datetime(df['date'], errors='coerce')

# Drop rows where 'date' column is null after conversion
df = df.dropna(subset=['date'])

# Option 1: Fill numeric missing values using Exponential Moving Average Smoothing
numeric_cols = df.select_dtypes(include=[np.number]).columns
for col in numeric_cols:
    df[col] = df[col].fillna(df[col].ewm(span=3, adjust=False).mean())

# Option 2: Fill categorical missing values with mode (optional)
categorical_cols = df.select_dtypes(include='object').columns
for col in categorical_cols:
    df[col] = df[col].fillna(df[col].mode()[0])

# ------------------ 🔄 3. Time Series Visualization ------------------
# Group data by date (assuming 'sales' is the column we want to analyze)
df_grouped = df.groupby(df['date'].dt.date)['sales'].sum()

# Plotting the time series (Sales Trend Over Time)
plt.figure(figsize=(12, 6))
plt.plot(df_grouped.index, df_grouped.values, label='Sales Over Time', color='tab:blue')
plt.title('Sales Trend Over Time')
plt.xlabel('Date')
plt.ylabel('Sales')
plt.xticks(rotation=45)
plt.legend()
plt.show()

# ------------------ 🔄 4. Seasonal Decomposition ------------------
# Perform seasonal decomposition (assuming daily data)
result = seasonal_decompose(df_grouped, model='additive', period=365)  # Period=365 for yearly seasonality

# Plot the seasonal decomposition
result.plot()
plt.show()

# ------------------ 🔄 5. Seasonal Patterns by Month ------------------
# Extract month and year from the 'date' column for seasonal analysis
df['month'] = df['date'].dt.month
df['year'] = df['date'].dt.year

# Group by month to observe seasonal trends
monthly_sales = df.groupby('month')['sales'].sum()

# Plot the seasonal pattern by month
plt.figure(figsize=(10, 6))
monthly_sales.plot(kind='bar', color='tab:green')
plt.title('Seasonal Sales Pattern by Month')
plt.xlabel('Month')
plt.ylabel('Total Sales')
plt.xticks(range(12), ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
plt.show()

# ------------------ 🔄 6. Rolling Average Trend ------------------
# Calculate rolling average (smooth out short-term fluctuations)
df_grouped_rolling = df_grouped.rolling(window=30).mean()

# Plotting the rolling average trend
plt.figure(figsize=(12, 6))
plt.plot(df_grouped.index, df_grouped.values, label='Sales', color='gray', alpha=0.5)
plt.plot(df_grouped.index, df_grouped_rolling, label='30-Day Rolling Average', color='tab:orange', linewidth=2)
plt.title('Sales Trend with Rolling Average')
plt.xlabel('Date')
plt.ylabel('Sales')
plt.xticks(rotation=45)
plt.legend()
plt.show()
