# Importing entire text files
# Open a file: file
file = open('mobydick.txt', mode='r')

# Print it
# print(file.read())

# Check whether file is closed
print(file.closed)

# Close file
file.close()

# Check whether file is closed
print(file.closed)


# Read & print the first 3 lines
with open('mobydick.txt') as file:
    print(file.readline())
    print(file.readline())
    print(file.readline())

# Importing flat files using NumPy

import numpy as np
filename = 'MNIST_test.txt'
data = np.loadtxt(filename, delimiter=',')
print(data)

"""
import numpy as np
filename = 'MNIST_header.txt'
data = np.loadtxt(filename, delimiter=',', skiprows=1, usecols=[0,2])
print(data)"""

'''
data = np.loadtxt(filename, delimiter=',', dtype = str)   #Ensures all datatypes are imported as stings
'''

"""
Using NumPy to import flat files
In this exercise, you're now going to load the MNIST digit recognition dataset using the numpy function loadtxt() and see just how easy it can be:

The first argument will be the filename.
The second will be the delimiter which, in this case, is a comma.
You can find more information about the MNIST dataset here on the webpage of Yann LeCun, who is currently Director of AI Research at Facebook and Founding Director of the NYU Center for Data Science, among many other things.

Instructions
100 XP
Fill in the arguments of np.loadtxt() by passing file and a comma ',' for the delimiter.
Fill in the argument of print() to print the type of the object digits. Use the function type().
Execute the rest of the code to visualize one of the rows of the data."""

# Test
data = np.loadtxt('MNIST_test.txt', delimiter=',')
print(type(data))

# Import package
import numpy as np
import matplotlib.pyplot as plt

# Assign filename to variable: file
file = 'MNIST_test.txt'

# Load file as array: digits
digits = np.loadtxt(file, delimiter=',')

# Print datatype of digits
print(type(digits))

# Select and reshape a row
im = digits[21, 1:]
im_sq = np.reshape(im, (28, 28))

# Plot reshaped data (matplotlib.pyplot already loaded as plt)
plt.imshow(im_sq, cmap='Greys', interpolation='nearest')
plt.show()
plt.clf()
"""
Customizing your NumPy import
What if there are rows, such as a header, that you don't want to import? What if your file has a delimiter other than a comma? What if you only wish to import particular columns?

There are a number of arguments that np.loadtxt() takes that you'll find useful:

delimiter changes the delimiter that loadtxt() is expecting.
You can use ',' for comma-delimited.
You can use '\t' for tab-delimited.
skiprows allows you to specify how many rows (not indices) you wish to skip
usecols takes a list of the indices of the columns you wish to keep.
The file that you'll be importing, digits_header.txt, has a header and is tab-delimited.

Instructions
100 XP
Complete the arguments of np.loadtxt(): the file you're importing is tab-delimited, you want to skip the first row and you only want to import the first and third columns.
Complete the argument of the print() call in order to print the entire array that you just imported."""

# Test
data = np.loadtxt('MNIST_test.txt', delimiter=',', skiprows=1, usecols=[0, 2])
print(data)

'''
# Import numpy
import numpy as np

# Assign the filename: file
file = 'digits_header.txt'

# Load the data: data
data = np.loadtxt(file, delimiter='\t', skiprows=1, usecols=[0,2])

# Print data
print(data)
'''

"""
# Assign filename: file
file = 'seaslug.txt'

# Import file: data
data = np.loadtxt(file, delimiter='\t', dtype=str)

# Print the first element of data
print(data[0])

# Import data as floats and skip the first row: data_float
data_float = np.loadtxt(file, delimiter='\t', dtype=float, skiprows=1)

# Print the 10th element of data_float
print(data_float[9])

# Plot a scatterplot of the data
plt.scatter(data_float[:, 0], data_float[:, 1])
plt.xlabel('time (min.)')
plt.ylabel('percentage of larvae')
plt.show()
"""


# Assign the filename: file
file = 'titanic.csv'

# Import file using np.recfromcsv: d
d = np.recfromcsv(file)

# Print out first three entries of d
print(d[:3])



