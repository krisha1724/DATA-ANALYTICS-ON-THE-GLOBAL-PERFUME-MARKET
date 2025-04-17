
import pandas as pd

# Load the cleaned dataset
df = pd.read_csv("E:/Ds/my_project/cleaned_perfume_data.csv")

# ---- Central Tendency ----
print("Central Tendency Measures:")
print(f"Mean Price (USD): {df['Price (USD)'].mean():.2f}")
print(f"Median Price (USD): {df['Price (USD)'].median():.2f}")
print(f"Mode Price (USD): {df['Price (USD)'].mode()[0]:.2f}")

print(f"\nMean Rating: {df['Rating'].mean():.2f}")
print(f"Median Rating: {df['Rating'].median():.2f}")
print(f"Mode Rating: {df['Rating'].mode()[0]}")

# ---- Variation Analysis ----
print("\nVariation Analysis:")
print(f"Range of Price (USD): {df['Price (USD)'].max() - df['Price (USD)'].min():.2f}")
print(f"Variance of Price (USD): {df['Price (USD)'].var():.2f}")
print(f"Standard Deviation of Price (USD): {df['Price (USD)'].std():.2f}")

print(f"\nRange of Rating: {df['Rating'].max() - df['Rating'].min():.2f}")
print(f"Variance of Rating: {df['Rating'].var():.2f}")
print(f"Standard Deviation of Rating: {df['Rating'].std():.2f}")

# ---- Cross-tabulation ----
print("\nCross-tabulation (Gender vs Rating Category):")
df['rating_category'] = pd.cut(df['Rating'], bins=[0, 2, 4, 5], labels=["Low", "Medium", "High"])
crosstab_result = pd.crosstab(df['Gender'], df['rating_category'])
print(crosstab_result)

# ---- Frequency Distribution ----
print("\nFrequency Distribution of Ratings:")
print(df[['Rating', 'rating_category']].value_counts().reset_index(name='Count'))
