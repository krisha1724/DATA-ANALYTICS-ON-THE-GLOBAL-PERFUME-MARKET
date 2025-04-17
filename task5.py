import pandas as pd
import numpy as np
from sklearn.preprocessing import OneHotEncoder

# Load the dataset
df = pd.read_csv("cleaned_perfume_data.csv")

# ------------------ 🔍 1. Data Profiling ------------------
print("🧾 Dataset Info:")
print(df.info())
print("\n📊 Descriptive Statistics:")
print(df.describe(include='all'))

# ------------------ 🧼 2. Handle Incomplete Data ------------------
# Option 1: Fill numeric missing values using Exponential Moving Average Smoothing
numeric_cols = df.select_dtypes(include=[np.number]).columns
for col in numeric_cols:
    df[col] = df[col].fillna(df[col].ewm(span=3, adjust=False).mean())

# Option 2: Fill categorical missing values with mode (optional)
categorical_cols = df.select_dtypes(include='object').columns
for col in categorical_cols:
    df[col] = df[col].fillna(df[col].mode()[0])

# ------------------ 🔄 3. One-Hot Encoding ------------------
df_encoded = pd.get_dummies(df, columns=categorical_cols, drop_first=True)

# ------------------ ✅ Final Transformed Data ------------------
print("\n✅ Final Transformed DataFrame shape:", df_encoded.shape)
print(df_encoded.head())
