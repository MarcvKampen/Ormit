import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV file with the appropriate delimiter
data = pd.read_csv("Customers.csv", delimiter=";")

# Split orders by "/"
order_counts = data["order"].str.split("/", expand=True).stack().value_counts()

# Create the bar chart
plt.bar(order_counts.index, order_counts.values)

# Customize the chart
plt.xlabel("Order Type")
plt.ylabel("Count")
plt.title("Order Type Count")
plt.xticks(rotation=90)

# Save the chart as a JPEG file
plt.savefig("order_type_count.jpeg")

# Display the chart
plt.show()

# Print the list of different orders
orders = order_counts.index.tolist()
print(orders)