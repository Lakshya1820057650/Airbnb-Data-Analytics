import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import os

# Load dataset
df = pd.read_csv("Airbnb.csv")

# Create folder to save visualizations
output_dir = "airbnb_visuals"
os.makedirs(output_dir, exist_ok=True)

# Clean data
df = df.dropna(subset=['price', 'room_type'])
df['price'] = df['price'].replace('[\$,]', '', regex=True).astype(float)

# --- 1. Bar Chart: Room Type Distribution ---
plt.figure(figsize=(8, 6))
sns.countplot(data=df, x='room_type', hue='room_type', palette='Set2', legend=False)
plt.title('Distribution of Room Types')
plt.xlabel('Room Type')
plt.ylabel('Count')
plt.xticks(rotation=30)
plt.tight_layout()
plt.savefig(f"{output_dir}/room_type_distribution.png")
plt.close()

# --- 2. Box Plot: Price Distribution by Room Type ---
plt.figure(figsize=(10, 6))
sns.boxplot(data=df, x='room_type', y='price', hue='room_type', palette='Pastel1', legend=False)
plt.yscale('log')
plt.title('Price Distribution by Room Type')
plt.xlabel('Room Type')
plt.ylabel('Price (Log Scale)')
plt.tight_layout()
plt.savefig(f"{output_dir}/price_by_room_type.png")
plt.close()

# --- 3. Scatter Plot: Reviews vs Price ---
plt.figure(figsize=(10, 6))
sns.scatterplot(data=df, x='number_of_reviews', y='price', hue='room_type', alpha=0.6)
plt.yscale('log')
plt.title('Number of Reviews vs Price')
plt.xlabel('Number of Reviews')
plt.ylabel('Price (Log Scale)')
plt.legend(title='Room Type')
plt.tight_layout()
plt.savefig(f"{output_dir}/reviews_vs_price.png")
plt.close()

# --- 4. Interactive Plot: Availability vs Price ---
import plotly.express as px

fig = px.scatter(
    df,
    x='minimum_nights',            # existing column
    y='price',
    color='room_type',
    hover_data=['property_type', 'bed_type'],
    title='Price vs Minimum Nights (Interactive)',
    labels={'minimum_nights': 'Minimum Nights', 'price': 'Price'}
)

fig.write_html("airbnb_visuals/interactive_price_vs_minimum_nights.html")
