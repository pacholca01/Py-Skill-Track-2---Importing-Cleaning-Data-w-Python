# Numeric data or ... ?
import pandas as pd
filename = 'ride_sharing_new.csv'
ride_sharing = pd.read_csv(filename)

print(ride_sharing.info())
print(ride_sharing['user_type'].describe())

ride_sharing['user_type_cat'] = ride_sharing['user_type'].astype('category')
assert ride_sharing['user_type_cat'].dtype == 'category'
print(ride_sharing['user_type_cat'].head())
print(ride_sharing['user_type_cat'].describe())

ride_sharing['duration_int'] = ride_sharing['duration'].str.strip('minutes').astype('int')
assert ride_sharing['duration_int'].dtype == 'int'
print(ride_sharing['duration_int'].mean())

""""
ride_sharing['tire_sizes'] = ride_sharing['tire_sizes'].astype('int')
ride_sharing.loc[ride_sharing['tire_sizes'] > 27, 'tire_sizes'] = 27
ride_sharing['tire_sizes'] = ride_sharing['tire_sizes'].astype('category')

print(ride_sharing['tire_sizes'].describe())


# Convert ride_date to date
ride_sharing['ride_dt'] = pd.to_datetime(ride_sharing['ride_date']).dt.date

# Save today's date
today = dt.date.today()

# Set all in the future to today's date
ride_sharing.loc[ride_sharing['ride_dt'] > today, 'ride_dt'] = today

# Print maximum of ride_dt column
print(ride_sharing['ride_dt'].max())

# Find duplicates
duplicates = ride_sharing.duplicated(subset = ['ride_id'], keep = False)

# Sort your duplicated rides
duplicated_rides = ride_sharing[duplicates].sort_values(by = 'ride_id')

# Print relevant columns of duplicated_rides
print(duplicated_rides[['ride_id','duration','user_birth_year']])




# Treating duplicates
# Drop complete duplicates from ride_sharing
ride_dup = ride_sharing.drop_duplicates()

# Create statistics dictionary for aggregation function
statistics = {'user_birth_year': 'min', 'duration': 'mean'}

# Group by ride_id and compute new statistics
ride_unique = ride_dup.groupby('ride_id').agg(statistics).reset_index()

# Find duplicated values again
duplicates = ride_unique.duplicated(subset = 'ride_id', keep = False)
duplicated_rides = ride_unique[duplicates == True]

# Assert duplicates are processed
assert duplicated_rides.shape[0] == 0
"""


"""

# Print categories DataFrame
print(categories)

# Print unique values of survey columns in airlines
print('Cleanliness: ', airlines['cleanliness'].unique(), "\n")
print('Safety: ', airlines['safety'].unique(), "\n")
print('Satisfaction: ', airlines['satisfaction'].unique(), "\n")"""