import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('queue.csv', delimiter=';')

df['start'] = pd.to_datetime(df['start'])
df['end'] = pd.to_datetime(df['end'], format='%H:%M', errors='coerce')
df['queue_time'] = pd.to_timedelta(df['queue_time']).dt.total_seconds()

df['hour'] = df['start'].dt.hour

mean_queue_time_by_hour = df.groupby(['stall', 'hour'])['queue_time'].mean().reset_index()

stalls = df['stall'].unique()

for stall in stalls:
    stall_data = mean_queue_time_by_hour[mean_queue_time_by_hour['stall'] == stall]

    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(stall_data['hour'], stall_data['queue_time'], marker='o', linestyle='-', color='b')

    ax.set_xlabel('Hour of the Day')
    ax.set_ylabel('Mean Queue Time (seconds)')
    ax.set_title(f'{stall} - Busiest Hours')
    
    plt.grid(True)
    plt.savefig(f'{stall}_busiest_hours.png')
    plt.close()
