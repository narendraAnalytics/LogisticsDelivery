import pandas as pd
import random

# Industry categories and products from the uploaded file
categories = {
    "Consumer Electronics": ["Smartphones", "Laptops", "Televisions"],
    "Automobiles and Auto Parts": ["Sedans", "Engine Components", "Tires"],
    "Apparel and Footwear": ["T-Shirts", "Jeans", "Sneakers"],
    "Furniture": ["Sofas", "Dining Tables", "Office Chairs"],
    "Pharmaceuticals": ["Pain Relievers", "Antibiotics", "Vaccines"],
    "Perishable Foods": ["Fresh Produce", "Dairy Products", "Meat Products"],
    "Construction Materials": ["Cement", "Steel Beams", "Lumber"],
    "Industrial Machinery": ["CNC Machines", "Conveyor Belts", "Generators"],
    "Books and Educational Materials": ["Textbooks", "Novels", "Educational Kits"],
    "Household Appliances": ["Refrigerators", "Washing Machines", "Microwaves"],
    "Cosmetics and Personal Care Products": ["Skincare Creams", "Shampoos", "Perfumes"],
    "Toys and Games": ["Action Figures", "Board Games", "Puzzles"],
    "Sporting Goods": ["Tennis Rackets", "Footballs", "Yoga Mats"],
    "Office Supplies": ["Printers", "Notebooks", "Pens"],
    "Pet Supplies": ["Pet Food", "Leashes", "Pet Toys"]
}

# Generate realistic price ranges for each category
price_ranges = {
    "Consumer Electronics": (5000, 80000),
    "Automobiles and Auto Parts": (1000, 150000),
    "Apparel and Footwear": (500, 5000),
    "Furniture": (3000, 50000),
    "Pharmaceuticals": (50, 5000),
    "Perishable Foods": (20, 500),
    "Construction Materials": (500, 50000),
    "Industrial Machinery": (50000, 180000),
    "Books and Educational Materials": (100, 2000),
    "Household Appliances": (5000, 80000),
    "Cosmetics and Personal Care Products": (50, 10000),
    "Toys and Games": (100, 5000),
    "Sporting Goods": (500, 20000),
    "Office Supplies": (10, 5000),
    "Pet Supplies": (50, 2000)
}

# Generate products table
products_data = []
product_id = 1
for category, items in categories.items():
    for product in items:
        price = random.randint(*price_ranges[category])  # Generate price within the range
        products_data.append([product_id, product, category, price])
        product_id += 1

# Create DataFrame
products_df = pd.DataFrame(products_data, columns=["ProductID", "ProductName", "ProductCategory", "BasePricePerUnit"])

# Save to CSV file
products_df.to_csv("products_table.csv", index=False)

# Display the first 5 rows of the DataFrame
products_df.head(5)
