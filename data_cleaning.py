import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV file with the appropriate delimiter
data = pd.read_csv("Customers.csv", delimiter=";")

# Split orders by "/"
order_counts = data["order"].str.split(" ", expand=True).stack().value_counts()
order_counts = order_counts[order_counts.index != ""]

# Replace [food_list] and [drinks_list] with your actual lists
food_list = ['fries', 'kebab', 'spaghetti_bolo', 'pad_thai', 'durum', 'extra_fries', 'pizza_margherita', 'arrabiata_vegi', 'pizza_pepperoni', 'chicken_poke', 'croquette_balls', 'carbonara', 'mayo', 'cocktail_sauce', 'caesar_salad', 'spring_rolls', 'mexicano', 'greek_salad', 'tofu_poke', 'bicky', 'pizza_4_cheeses', 'bacon_&_baked_brie_salad', 'green_curry_pork', 'green_curry_tofu', 'quarter_pizza_margherita', 'quarter_pizza_pepperoni', 'quarter_pizza_4_cheeses', 'ketchup', 'garlic_bread', 'salmon_poke', 'green_sauce', 'kebab_vegi', 'red_curry_tofu', 'durum_vegi', 'frikandel', 'garlic_bread', 'garlic_sauce', 'green_curry_chicken', 'kebab_vegi', 'ketchup', 'red_curry_chicken', 'red_curry_pork', 'red_curry_tofu', 'salmon_poke', 'salmon_tofu']

drinks_list = ['beer', 'coke', 'still_water', 'white_wine', 'desperados', 'cava', 'red_wine', 'aperol_spritz', 'sparkling_water', 'red_berry_madness_juice', 'passion_delight_juice', 'turkish_coffee', 'green_&_clean_juice']

# Separate orders into food and drinks
food_order_counts = order_counts[order_counts.index.isin(food_list)]
drinks_order_counts = order_counts[order_counts.index.isin(drinks_list)]

# Create the bar chart for food
plt.figure(figsize=(10, 12))
plt.bar(food_order_counts.index, food_order_counts.values)
for i, count in enumerate(food_order_counts.values):
    plt.text(i, count, str(count), ha='center', va='bottom', fontsize=8)
plt.xlabel("Food Type")
plt.ylabel("Count")
plt.title("Food Type Count")
plt.xticks(rotation=90)
plt.savefig("food_orders.jpeg")
plt.show()

# Create the bar chart for drinks
plt.figure(figsize=(10, 12))
plt.bar(drinks_order_counts.index, drinks_order_counts.values)
for i, count in enumerate(drinks_order_counts.values):
    plt.text(i, count, str(count), ha='center', va='bottom', fontsize=8)
plt.xlabel("Drink Type")
plt.ylabel("Count")
plt.title("Drink Type Count")
plt.xticks(rotation=90)
plt.savefig("drinks_orders.jpeg")
plt.show()

