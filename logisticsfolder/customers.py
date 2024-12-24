from faker import Faker
import pandas as pd
import random

# Initialize Faker with locale for India
fake = Faker("en_IN")

# Generate sample data for 5000 customers using Faker
location_ids = list(range(1, 16))  # Assuming 15 LocationIDs

customers_data = {
    "CustomerID": list(range(1, 5001)),  # 5000 Customers
    "CustomerName": [fake.name() for _ in range(5000)],
    "Gender": [random.choice(["Male", "Female"]) for _ in range(5000)],
    "ContactNumber": [fake.phone_number() for _ in range(5000)],
    "EmailAddress": [fake.email() for _ in range(5000)],
    "Address": [fake.address() for _ in range(5000)],
    "LocationID": [random.choice(location_ids) for _ in range(5000)]
}

# Create DataFrame
customers_df = pd.DataFrame(customers_data)

# Save to CSV file
customers_df.to_csv("customers_table_with_faker.csv", index=False)

# Display the first 5 rows of the DataFrame
customers_df.head(5)
