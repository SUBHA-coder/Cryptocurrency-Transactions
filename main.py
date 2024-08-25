import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

# Load the transaction data from the Excel file, skipping the first row
file_path = 'eth.xlsx'  # Replace with the path to your downloaded XLSX file
data = pd.read_excel(file_path, header=1)  # Skip the first row

# Display the column names and the first few rows of the dataset
print("Columns:", data.columns)
print(data.head())

# Clean the column names
data.columns = data.columns.str.strip()

# Check the cleaned column names
print("Cleaned Columns:", data.columns)

# Feature extraction (example features)
# Group by 'from_address' and aggregate 'value' and count transactions
try:
    features = data.groupby('from_address').agg({
        'value': 'sum',                # Total value sent
        'block_timestamp': 'count'     # Number of transactions
    }).reset_index()
except KeyError as e:
    print(f"KeyError: {e}")
    print("Available columns:", data.columns)
    exit()

# Rename columns for clarity
features.columns = ['address', 'total_value', 'transaction_count']

# Apply k-means clustering
kmeans = KMeans(n_clusters=3)  # Choose the number of clusters
features['cluster'] = kmeans.fit_predict(features[['total_value', 'transaction_count']])

# Print the clustered features
print(features)

# Visualize the clusters
plt.figure(figsize=(10, 6))
plt.scatter(features['total_value'], features['transaction_count'], c=features['cluster'], cmap='viridis', marker='o')
plt.xlabel('Total Value Sent (ETH)')
plt.ylabel('Number of Transactions')
plt.title('Clustering of Ethereum Addresses')
plt.colorbar(label='Cluster')
plt.show()
