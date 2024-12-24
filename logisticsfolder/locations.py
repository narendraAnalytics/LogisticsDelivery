import pandas as pd

# Sample dataset of Indian cities and their states
# Note: This dataset can be extended with a comprehensive list of Indian cities and states.
data = {
    "CityName": [
        "Mumbai", "Delhi", "Bengaluru", "Hyderabad", "Ahmedabad", "Chennai", "Kolkata",
        "Pune", "Jaipur", "Lucknow", "Kanpur", "Nagpur", "Indore", "Patna", "Bhopal"
    ],
    "StateName": [
        "Maharashtra", "Delhi", "Karnataka", "Telangana", "Gujarat", "Tamil Nadu", 
        "West Bengal", "Maharashtra", "Rajasthan", "Uttar Pradesh", "Uttar Pradesh",
        "Maharashtra", "Madhya Pradesh", "Bihar", "Madhya Pradesh"
    ]
}

# Creating a DataFrame
locations_df = pd.DataFrame(data)

# Adding a LocationID (Primary Key)
locations_df.reset_index(inplace=True)
locations_df.rename(columns={"index": "LocationID"}, inplace=True)
locations_df["LocationID"] += 1  # Start LocationID from 1

# Save the table to a CSV file for future use
locations_df.to_csv("locations.csv", index=False)

# Display the DataFrame
print(locations_df)
