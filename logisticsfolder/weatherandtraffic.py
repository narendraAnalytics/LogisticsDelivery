from datetime import datetime, timedelta
import random
import pandas as pd

# Load existing Locations Table
location_ids = list(range(1, 16))  # Assuming LocationID: 1 to 15

# Generate Weather and Traffic Data Table
weather_conditions = ["Clear", "Rainy", "Foggy", "Snowy", "Windy"]
traffic_conditions = ["Light", "Moderate", "Heavy"]
start_date = datetime(2021, 12, 25)
end_date = datetime(2024, 12, 20)
date_range = (end_date - start_date).days

weather_traffic_data = []
record_id = 1

for _ in range(10000):  # 10,000 records for Weather and Traffic Data
    location_id = random.choice(location_ids)  # Random LocationID
    weather_condition = random.choice(weather_conditions)  # Random Weather Condition
    traffic_condition = random.choice(traffic_conditions)  # Random Traffic Condition
    recorded_date = start_date + timedelta(days=random.randint(0, date_range))
    recorded_time = datetime.strptime(f"{random.randint(0, 23)}:{random.randint(0, 59)}:00", "%H:%M:%S")
    recorded_datetime = datetime.combine(recorded_date, recorded_time.time())

    weather_traffic_data.append([
        record_id, location_id, weather_condition, traffic_condition, recorded_datetime.strftime("%Y-%m-%d %H:%M:%S")
    ])
    record_id += 1

# Create DataFrame for Weather and Traffic Data Table
weather_traffic_df = pd.DataFrame(weather_traffic_data, columns=[
    "WeatherTrafficID", "LocationID", "WeatherCondition", "TrafficCondition", "RecordedDateTime"
])

# Save to CSV file
weather_traffic_df.to_csv("weathertraffic.csv", index=False)

# Display the first 5 rows of the DataFrame
weather_traffic_df.head(5)
