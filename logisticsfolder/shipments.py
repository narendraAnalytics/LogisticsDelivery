from datetime import datetime, timedelta
import random
import pandas as pd

# Generate the Shipments Table for 5000 Customers
# Reuse Customer IDs and Location IDs from Customers Table

num_shipments = 10000  # Number of shipments to create
customer_ids = list(range(1, 5001))  # CustomerID: 1 to 5000
location_ids = list(range(1, 16))  # LocationID: 1 to 15
provider_ids = list(range(1, 6))  # ProviderID: 1 to 5

# Generate random ShipmentDate within the given range
start_date = datetime(2021, 12, 25)
end_date = datetime(2024, 12, 20)
date_range = (end_date - start_date).days

shipments_data = []
for shipment_id in range(1, num_shipments + 1):
    customer_id = random.choice(customer_ids)  # Randomly assign CustomerID
    provider_id = random.choice(provider_ids)  # Randomly assign ProviderID
    origin_location = random.choice(location_ids)  # Random Origin
    destination_location = random.choice(location_ids)  # Random Destination (can repeat origin for simplicity)
    while origin_location == destination_location:  # Ensure origin != destination
        destination_location = random.choice(location_ids)
    shipment_date = start_date + timedelta(days=random.randint(0, date_range))
    delivery_date = shipment_date + timedelta(days=random.randint(4, 22))  # 4-22 days after ShipmentDate

    shipment_status = random.choice(["In-Transit", "Delivered", "Pending"])
    delivery_status = "Completed" if shipment_status == "Delivered" else random.choice(["Returned", "Delayed", "Canceled"])

    shipments_data.append([
        shipment_id, provider_id, customer_id, origin_location, destination_location,
        shipment_status, delivery_status, shipment_date.strftime("%Y-%m-%d"), delivery_date.strftime("%Y-%m-%d")
    ])

# Create DataFrame for Shipments Table
shipments_df = pd.DataFrame(shipments_data, columns=[
    "ShipmentID", "ProviderID", "CustomerID", "OriginLocationID", "DestinationLocationID",
    "ShipmentStatus", "DeliveryStatus", "ShipmentDate", "DeliveryDate"
])

# Save to CSV file
shipments_df.to_csv("shipments.csv", index=False)

# Display the first 5 rows of the DataFrame
shipments_df.head(5)
