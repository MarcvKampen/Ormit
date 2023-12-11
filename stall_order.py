import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("orders2.csv", delimiter=";")

order_counts = data["stall"].value_counts()
plt.bar(order_counts.index, order_counts.values)

for i, count in enumerate(order_counts.values):
    plt.text(i, count, str(count), ha='center', va='bottom')

plt.xlabel("Stall")
plt.ylabel("Count")
plt.title("Order Count per Stall")

plt.xticks(rotation=90)

plt.savefig("order_count_per_stall.jpeg")

plt.show()
