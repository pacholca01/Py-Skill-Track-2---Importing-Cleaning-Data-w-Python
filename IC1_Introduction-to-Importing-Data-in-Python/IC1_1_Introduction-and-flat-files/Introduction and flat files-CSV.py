# Importing flat files using pandas

import pandas as pd
filename = 'titanic.csv'
newdata = pd.read_csv(filename)
print(newdata.head(20))
dataNPArray = newdata.values
print(dataNPArray)


import pandas as pd

# Assign the filename: file
file = 'titanic.csv'

# Read the file into a DataFrame: df
df = pd.read_csv(file)

# View the head of the DataFrame
print(df.head())

"""
# Assign the filename: file
file = 'digits.csv'

# Read the first 5 rows of the file into a DataFrame: data
data = pd.read_csv(file, nrows=5, header=None)

# Build a numpy array from the DataFrame: data_array
data_array= data.values

# Print the datatype of data_array to the shell
print(type(data_array))
"""
"""
Customizing your pandas import
The pandas package is also great at dealing with many of the issues you will encounter when importing data as a data scientist, 
such as comments occurring in flat files, empty lines and missing values. Note that missing values are also commonly 
referred to as NA or NaN. To wrap up this chapter, you're now going to import a slightly corrupted copy of
 the Titanic dataset titanic_corrupt.txt, which

contains comments after the character '#'
is tab-delimited.
Instructions
100 XP
Complete the sep (the pandas version of delim), comment and na_values arguments of pd.read_csv(). comment takes 
characters that comments occur after in the file, which in this case is '#'. na_values takes a list of strings to 
recognize as NA/NaN, in this case the string 'Nothing'.
Execute the rest of the code to print the head of the resulting DataFrame and plot the histogram of the 'Age' 
of passengers aboard the Titanic."""

'''# Import matplotlib.pyplot as plt
import matplotlib.pyplot as plt

# Assign filename: file
file = 'titanic_corrupt.txt'

# Import file: data
data = pd.read_csv(file, sep='\t', comment='#', na_values='Nothing')

# Print the head of the DataFrame
print(data.head())

# Plot 'Age' variable in a histogram
pd.DataFrame.hist(data[['Age']])
plt.xlabel('Age (years)')
plt.ylabel('count')
plt.show()

'''
