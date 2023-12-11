import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("orders2.csv", delimiter=";")

data["arrival"] = pd.to_datetime(data["arrival"], format="%H:%M:%S")

data["hour"] = data["arrival"].dt.hour
stalls = data["stall"]

order_traffic = data.groupby(['stall', 'hour'])['order'].count().unstack().fillna(0)
skip_counts = data.groupby(['stall', 'hour'])['order'].apply(lambda x: x.isnull().sum()).unstack().fillna(0)

unique_stalls = order_traffic.index

overall_skip_counts = skip_counts.sum()

for stall in unique_stalls:
    plt.figure(figsize=(8, 5))

    order_data = order_traffic.loc[stall]
    skip_data = skip_counts.loc[stall]

    bars = plt.bar(order_data.index, order_data, alpha=0.7, label='Orders')
    skip_bars = plt.bar(skip_data.index, skip_data, alpha=0.7, bottom=order_data, color='red', label='Skips')

    for bar, order_count in zip(bars, order_data):
        plt.text(bar.get_x() + bar.get_width() / 2, bar.get_y() + bar.get_height() / 2,
                 f'{int(order_count)}', ha='center', va='center', color='white')

    for bar, skip_count in zip(skip_bars, skip_data):
        if skip_count > 0:
            plt.text(bar.get_x() + bar.get_width() / 2, bar.get_y() + bar.get_height() / 2,
                     f'{int(skip_count)}', ha='center', va='center', color='white')

    ticks = list(range(11, 24))
    labels = [f"{hour:02d}:00" for hour in range(11, 24)]
    plt.xticks(ticks, labels, rotation=45)

    plt.xlim(ticks[0] - 0.5, ticks[-1] + 0.5)

    plt.xlabel("Hour")
    plt.ylabel("Order Count")
    plt.title(f"Order Traffic for Stall {stall}")
    plt.legend()

    plt.savefig(f"order_traffic_stall_{stall}.jpeg")

    plt.show()

for hour, overall_skip_count in overall_skip_counts.items():
    print(f"{hour:02d}:00, {int(overall_skip_count)} skips")

total_skips = overall_skip_counts.sum()
print(f"Total Skips: {int(total_skips)}")
