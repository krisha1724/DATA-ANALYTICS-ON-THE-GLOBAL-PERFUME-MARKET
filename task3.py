# Import necessary libraries
import pandas as pd

# Load the dataset
file_path = r"E:\Ds\my_project\data.csv"  # Input file path
cleaned_file_path = r"E:\Ds\my_project\cleaned_perfume_data.csv"  # Output file path

# Load the CSV file
df = pd.read_csv(file_path)

# Check missing values in 'Fragrance Notes', 'Rating', 'Price (USD)', and 'Launch Year'
print("Missing values BEFORE filling:")
missing_values = df[['Fragrance Notes', 'Rating', 'Price (USD)', 'Launch Year']].isnull().sum()
print(missing_values)

# Fill missing values
df['Fragrance Notes'] = df['Fragrance Notes'].fillna('UNKNOWN')  # Replace missing fragrance notes with 'UNKNOWN'
df['Rating'] = df['Rating'].fillna(0)  # Replace missing ratings with '0'
df['Price (USD)'] = df['Price (USD)'].fillna(df['Price (USD)'].median())  # Replace missing prices with median value
df['Launch Year'] = df['Launch Year'].fillna(df['Launch Year'].mode()[0])  # Replace missing years with mode (most common year)

# Remove duplicates
df.drop_duplicates(inplace=True)

# Show missing values after filling
print("\nMissing values AFTER filling:")
print(df[['Fragrance Notes', 'Rating', 'Price (USD)', 'Launch Year']].isnull().sum())

# Save the cleaned data to a new CSV file
df.to_csv(cleaned_file_path, index=False)

print(f"\nData cleaning complete. File saved as '{cleaned_file_path}'.")