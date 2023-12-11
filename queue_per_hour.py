import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('queue.csv', delimiter=';')

df['start'] = pd.to_datetime(df['start'])
df['end'] = pd.to_datetime(df['end'], format='%H:%M', errors='coerce')
df['queue_time'] = pd.to_timedelta(df['queue_time']).dt.total_seconds()

df['hour'] = df['start'].dt.hour

df = df[(df['hour'] >= 11) & (df['hour'] <= 23)]

mean_queue_time_by_hour = df.groupby(['stall', 'hour'])['queue_time'].mean().reset_index()

stalls = df['stall'].unique()

for stall in stalls:
    stall_data = mean_queue_time_by_hour[mean_queue_time_by_hour['stall'] == stall]

    busiest_hour = stall_data.loc[stall_data['queue_time'].idxmax()]['hour']
    busiest_hour_mean_time = stall_data.loc[stall_data['queue_time'].idxmax()]['queue_time']

    print(f'{stall} - Busiest Hour: {busiest_hour}:00 (Mean Queue Time: {busiest_hour_mean_time:.2f} seconds)')

    fig, ax = plt.subplots(figsize=(10, 6))
    ax.bar(stall_data['hour'], stall_data['queue_time'], color='b')

    ax.set_xlabel('Hour of the Day')
    ax.set_ylabel('Mean Queue Time (seconds)')
    ax.set_title(f'{stall} - Busiest Hours')
    
    plt.grid(True)
    plt.savefig(f'{stall}_busiest_hours.png')
    plt.close()
