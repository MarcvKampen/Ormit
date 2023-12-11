import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime, timedelta

df = pd.read_csv('queue.csv', delimiter=';')

df['start'] = pd.to_datetime(df['start'])
df['end'] = pd.to_datetime(df['end'], format='%H:%M', errors='coerce') + timedelta(days=1)
df['queue_time'] = pd.to_timedelta(df['queue_time'])
df['preperation_time'] = pd.to_timedelta(df['preperation_time'])

df['hour'] = df['start'].dt.hour

df_filtered = df[(df['hour'] >= 11) & (df['hour'] <= 23)]

df_filtered['preparation_time_seconds'] = df_filtered['preperation_time'].dt.total_seconds()
df_filtered['queue_time_seconds'] = df_filtered['queue_time'].dt.total_seconds()

mean_queue_time_per_hour = df_filtered.groupby('hour')['queue_time_seconds'].mean()

plt.figure(figsize=(10, 6))
mean_queue_time_per_hour.plot(kind='bar', color='blue', alpha=0.7)
plt.xlabel('Hour')
plt.ylabel('Mean Queue Time (seconds)')
plt.title('Mean Queue Time per Hour')
plt.axhline(df_filtered['queue_time_seconds'].mean(), color='red', linestyle='dashed', linewidth=2, label='Overall Mean')

for i, v in enumerate(mean_queue_time_per_hour):
    plt.text(i, v, f'{v:.2f}', ha='center', va='bottom')

plt.legend()
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('mean_queue_time_per_hour.png')
plt.show()
