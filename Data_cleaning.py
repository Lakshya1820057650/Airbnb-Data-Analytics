import pandas as pd

# Load the dataset
df = pd.read_csv("Airbnb.csv")

# Helper function to clean numeric columns
def clean_numeric(x, default=1.0, upper_limit=7.0):
    try:
        val = str(x).replace('+', '').replace('$', '').replace(',', '').strip()
        val = float(val)
        return val if val <= upper_limit else default
    except:
        return default

# Clean numerical fields
df['bathrooms'] = df['bathrooms'].apply(lambda x: clean_numeric(x, default=1.0))
df['bedrooms'] = df['bedrooms'].apply(lambda x: clean_numeric(x, default=1.0))
df['beds'] = df['beds'].apply(lambda x: clean_numeric(x, default=1.0))
df['price'] = df['price'].apply(lambda x: clean_numeric(x, default=df['price'].median(), upper_limit=10000))

# Categorical columns to encode
categorical_cols = ['property_type', 'room_type', 'bed_type', 'cancellation_policy']

# One-hot encode categorical columns
df_dummies = pd.get_dummies(df[categorical_cols], prefix=categorical_cols)

# Drop original categorical + unwanted columns
df_cleaned = pd.concat([df.drop(columns=categorical_cols + ['Unnamed: 0']), df_dummies], axis=1)

# Optional: Save to new CSV
# df_cleaned.to_csv("Airbnb_Cleaned.csv", index=False)

# Preview cleaned data
print(df_cleaned.head())
