import random
import pandas as pd

# Ensure all providers are represented randomly while avoiding strict ordering
provider_ids = [1, 5, 3, 2, 4, 1, 3, 4, 2, 5]

# Update the ProviderID in the salespersons_data to this shuffled sequence
salespersons_data = {
    "SalesPersonID": list(range(1, 11)),  # 10 Salespersons
    "SalesPersonName": [
        "John Doe", "Jane Smith", "Robert Brown", "Emily Davis", "Michael Johnson",
        "Sarah Wilson", "David Lee", "Laura Martinez", "James White", "Emma Thomas"
    ],
    "SalesPersonContact": [
        "9123456789", "8123456780", "7234567890", "6345678901", "5456789012",
        "4567890123", "3678901234", "2789012345", "1890123456", "1001234567"
    ],
    "SalesPersonEmail": [
        "john.doe@logistics.com", "jane.smith@couriers.com", "robert.brown@express.com",
        "emily.davis@freight.com", "michael.johnson@movers.com", "sarah.wilson@logistics.com",
        "david.lee@couriers.com", "laura.martinez@express.com", "james.white@freight.com",
        "emma.thomas@movers.com"
    ],
    "ProviderID": provider_ids  # Randomized provider assignment ensuring all providers are covered
}

# Create DataFrame
salespersons_df = pd.DataFrame(salespersons_data)

# Save to CSV file
salespersons_df.to_csv("salespersons.csv", index=False)

# Display the first 5 rows of the DataFrame
salespersons_df.head(5)
