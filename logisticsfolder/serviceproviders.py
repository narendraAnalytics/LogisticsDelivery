import pandas as pd

# Sample data for Service Providers Table
service_providers_data = {
    "ProviderID": [1, 2, 3, 4, 5],
    "ProviderName": [
        "ABC Logistics", 
        "XYZ Couriers", 
        "Speedy Express", 
        "Global Freight", 
        "Rapid Movers"
    ],
    "ContactNumber": ["9876543210", "8765432109", "7654321098", "6543210987", "5432109876"],
    "EmailAddress": [
        "abc@logistics.com", 
        "xyz@couriers.com", 
        "speedy@express.com", 
        "global@freight.com", 
        "rapid@movers.com"
    ]
}

# Create DataFrame
service_providers_df = pd.DataFrame(service_providers_data)

# Save the table to a CSV file for future use
service_providers_df.to_csv("serviceproviders.csv", index=False)

# Display the first 3 rows
service_providers_df.head(3)
