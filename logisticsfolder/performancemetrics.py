import pandas as pd
import random

# Load existing Shipments Table
shipments_df = pd.read_csv("/workspaces/LogisticsDelivery/logisticsfolder/shipment_details_table.csv")

# Generate Performance Metrics Table
metric_data = []
metric_id = 1

for shipment_id in shipments_df["ShipmentID"].tolist():
    
    # Customer Satisfaction: 1-5 rating
    customer_satisfaction = random.randint(1, 5)

    metric_data.append([metric_id, shipment_id,customer_satisfaction])
    metric_id += 1

# Create DataFrame for Performance Metrics Table
performance_metrics_df = pd.DataFrame(metric_data, columns=[
    "MetricID", "ShipmentID", "CustomerSatisfaction"
])

# Save to CSV file
performance_metrics_df.to_csv("performancemetricstable.csv", index=False)

# Display the first 5 rows of the DataFrame
performance_metrics_df.head(5)
