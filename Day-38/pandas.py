import pandas as pd

prices = [2999, 3456, 8966, 2345, 6543]
products = ["Wireless Earbuds","SmartPhone","Laptop","SmartWatch","Bluetooth Speaker"]

# Create a Pandas Series using the prices as values
# and product names as the index/labels.
product_prices = pd.Series(prices, index=products)

# Each product name is displayed along with its corresponding price.
print(product_prices)

# Calculate and display the average,total price all products,largest product price,lowest product price.
print("Mean", product_prices.mean())
print("Sum", product_prices.sum())
print("Max", product_prices.max())
print("Min", product_prices.min())

# head(3) returns the first three records.
print("Head (First 3 Elements):\n", product_prices.head(3))

# tail(2) returns the last two records.
print("Tail (Last 2 Elements):\n", product_prices.tail(2))

# Use the apply() function to perform an operation on every price.
print(
    "Apply (Adding 18% GST):\n",
    product_prices.apply(
        lambda x: f"₹{x + (x * 0.18)}"
    )
)

# Use the map() function to apply an operation to every price.
print(
    "Map (Formatting as Currency):\n",
    product_prices.map(
        lambda x: f"₹{x:.2f}"
    )
)

# Sort the products according to their prices.
print(product_prices.sort_values())

# Sort the Series according to the product names (index)..
print(product_prices.sort_index())

# Sort the product names in descending alphabetical order.
print(product_prices.sort_index(ascending=False))

# Count how many times each price appears in the Series.
print("Value counts:\n", product_prices.value_counts())

