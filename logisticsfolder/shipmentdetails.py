import pandas as pd
import random

# Load existing tables (Products and Shipments)
products_df = pd.read_csv("/workspaces/LogisticsDelivery/logisticsfolder/products.csv")  # Products Table
shipments_df = pd.read_csv("/workspaces/LogisticsDelivery/logisticsfolder/shipments.csv")  # Shipments Table

# Generate Shipment Details Table
shipment_ids = shipments_df["ShipmentID"].tolist()  # Shipment IDs from Shipments Table
product_ids = products_df["ProductID"].tolist()  # Product IDs from Products Table

shipment_details_data = []
shipment_detail_id = 1

for shipment_id in shipment_ids:
    # Assign a random number of products per shipment (1 to 5 products)
    num_products = random.randint(1, 5)
    for _ in range(num_products):
        product_id = random.choice(product_ids)  # Random ProductID
        quantity = random.randint(1, 10)  # Quantity between 1 and 10
        product_price = products_df.loc[products_df['ProductID'] == product_id, 'BasePricePerUnit'].values[0]
        total_item_price = product_price * quantity
        additional_charges = round(random.uniform(50, 500), 2)  # Additional charges between ₹50 and ₹500
        total_price = round(total_item_price + additional_charges, 2)
        item_weight = random.randint(1, 50)  # Random weight in kg (1-50)

        shipment_details_data.append([
            shipment_detail_id, shipment_id, product_id, item_weight, quantity,
            total_item_price, additional_charges, total_price
        ])
        shipment_detail_id += 1

# Create DataFrame for Shipment Details Table
shipment_details_df = pd.DataFrame(shipment_details_data, columns=[
    "ShipmentDetailID", "ShipmentID", "ProductID", "ItemWeight", "Quantity",
    "TotalItemPrice", "AdditionalCharges", "TotalPrice"
])

# Save to CSV file
shipment_details_df.to_csv("shipment_details_table.csv", index=False)

# Display the first 5 rows of the DataFrame
print(shipment_details_df.head(5))
