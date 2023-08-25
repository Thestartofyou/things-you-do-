import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

# Load your call data from a CSV or other source
# Make sure your data has columns 'timestamp' and 'duration' at least
# You might have additional columns like 'client_id', 'call_result', etc.
# df = pd.read_csv('call_data.csv')

# Convert the 'timestamp' column to datetime format
df['timestamp'] = pd.to_datetime(df['timestamp'])

# Extract hour and weekday from the timestamp
df['hour'] = df['timestamp'].dt.hour
df['weekday'] = df['timestamp'].dt.weekday  # Monday=0, Sunday=6

# Calculate average call duration by hour and weekday
avg_duration_by_hour = df.groupby('hour')['duration'].mean()
avg_duration_by_weekday = df.groupby('weekday')['duration'].mean()

# Plot the average call duration by hour
plt.figure(figsize=(10, 5))
plt.plot(avg_duration_by_hour.index, avg_duration_by_hour.values, marker='o')
plt.xlabel('Hour of the Day')
plt.ylabel('Average Call Duration')
plt.title('Average Call Duration by Hour')
plt.xticks(range(24))
plt.grid(True)
plt.show()

# Plot the average call duration by weekday
weekday_names = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
plt.figure(figsize=(10, 5))
plt.plot(weekday_names, avg_duration_by_weekday.values, marker='o')
plt.xlabel('Weekday')
plt.ylabel('Average Call Duration')
plt.title('Average Call Duration by Weekday')
plt.grid(True)
plt.show()

# Find the best time slots based on the above analysis
best_hour = avg_duration_by_hour.idxmax()
best_weekday = avg_duration_by_weekday.idxmax()

print(f"Best time to call clients:")
print(f"Hour: {best_hour} (local time)")
print(f"Weekday: {weekday_names[best_weekday]}")
