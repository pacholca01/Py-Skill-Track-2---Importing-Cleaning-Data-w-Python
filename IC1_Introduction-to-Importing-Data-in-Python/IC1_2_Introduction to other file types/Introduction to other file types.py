# 2_Introduction to other file types
"""
import pickle
with open('pickled_fruit.pkl', 'rb') as file :
    data = pickle.load(file)
print(data)
"""

import pandas as pd
file = 'urbanpop.xlsx'
data = pd.ExcelFile(file)       # pip3 install openpyxl
print(data.sheet_names)

# parse sheets
df1 = data.parse('1960-1966')
df2 = data.parse(1)

print(df1.head())
print("\n")
print(df2.head())

# get files in current working directory as a list
import os
wd = os.getcwd()
print(os.listdir(wd))

"""
import pickle

# Open pickle file and load data: d
with open('data.pkl', 'rb') as file: # r = readonly b = binary
    d = pickle.load(file)

# Print d
print(d)

# Print datatype of d
print(type(d))
"""

# Import pandas
import pandas as pd

# Assign spreadsheet filename: file
file = 'battledeath.xlsx'

# Load spreadsheet: xls
xls = pd.ExcelFile(file)

# Print sheet names
print(xls.sheet_names)

# Load a sheet into a DataFrame by name: df1
df1 = xls.parse('2004')

# Print the head of the DataFrame df1
print(df1.head())

# Load a sheet into a DataFrame by index: df2
df2 = xls.parse(0)

# Print the head of the DataFrame df2
print(df2.head())

# Parse the first sheet and rename the columns: df1
df1 = xls.parse('2002', skiprows=1, names=['Country','AAM due to War (2002)'])

# Print the head of the DataFrame df1
print(df1.head())

# Parse the first column of the second sheet and rename the column: df2
df2 = xls.parse('2004', usecols=[0], skiprows=1, names=['Country'])

# Print the head of the DataFrame df2
print(df2.head())

"""
# Importing SAS/Stata files using pandas
import pandas as pd
from sas7bdat import SAS7BDAT
with SAS7BDAT('urbanpop.sas7bdat') as file
    dfsas = file.to_data_frame()

import pandas as pd
data = pd.read_stata('urbanpop.dta')
"""

# Import sas7bdat package
from sas7bdat import SAS7BDAT   # pip3 install sas7bdat

# Save file to a DataFrame: df_sas
with SAS7BDAT('sales.sas7bdat') as file:
    df_sas = file.to_data_frame()

# Print head of DataFrame
print(df_sas.head())

import matplotlib.pyplot as plt
# Plot histogram of DataFrame features (pandas and pyplot already imported)
pd.DataFrame.hist(df_sas[['P']])
plt.ylabel('count')
# plt.show()                    # Throws Exception Not sure why
plt.clf()

"""
Importing Stata files
Here, you'll gain expertise in importing Stata files as DataFrames using the pd.read_stata() function from pandas. 
The last exercise's file, 'disarea.dta', is still in your working directory."""

# Import pandas
import pandas as pd

# Load Stata file into a pandas DataFrame: df
df = pd.read_stata('disarea.dta')

# Print the head of the DataFrame df
print(df.head())

# Plot histogram of one column of the DataFrame
pd.DataFrame.hist(df[['disa10']])
plt.xlabel('Extent of disease')
plt.ylabel('Number of countries')
# plt.show()                    # Throws Exception Not sure why
plt.clf()

"""
# Importing HDF5 files
import h5py                         # pip3 install h5py

filename = 'L-L1_LOSC_4_V1-1126259446-32.hdf5'
data = h5py.File(filename, 'r')     # r for readonly
print(type(data))                   

# THIS THROWS EXCEPTION, NOT SURE WHY
# https://campus.datacamp.com/courses/introduction-to-importing-data-in-python/importing-data-from-other-file-types-2?ex=12

for k in data.keys() :
    print(K)
    
print(type(data['meta']))

# LIGO Data
# https://www.ligo.caltech.edu/page/ligo-data

for k in data['meta'].keys() :
    print(k)               

import numpy as np
print(np.array(data['meta']['Description'],data['meta']['Detector'] ))


# Exercises
# Import packages
import numpy as np
import h5py

# Assign filename: file
file = 'LIGO_data.hdf5'

# Load file: data
data = h5py.File(file, 'r')

# Print the datatype of the loaded file
print(type(data))

# Print the keys of the file
for k in data.keys() :
    print(k)
    
# Get the HDF5 group: group
# Assign the HDF5 group data['strain'] to group.
group = data['strain']

# Check out keys of group
for key in group.keys():
    print(key)

# Set variable equal to time series data: strain
# Assign the time series data data['strain']['Strain'] to a NumPy array called strain.
strain = np.array(data['strain']['Strain'])

# Set number of time points to sample: num_samples
# Set num_samples equal to 10000, the number of time points we wish to sample.
num_samples = 10000

# Set time vector
time = np.arange(0, 1, 1/num_samples)

# Plot data
plt.plot(time, strain[:num_samples])
plt.xlabel('GPS Time (s)')
plt.ylabel('strain')
plt.show()

"""

# Importing MATLAB files

# scipy.io.loadmat()    # read .mat files
# scipy.io.savemat()    # write .mat files

import scipy.io         # pip3 install scipy
filename = 'ja_data2.mat'
mat = scipy.io.loadmat(filename)
print(mat)
print(type(mat))
"""
keys = MARLAB variable names
values = objects assigned to variables
"""
# print(type(mat['x']))     # this array does not exist

# https://www.mcb.ucdavis.edu/faculty-labs/albeck/workshop.htm
# https://www.hylkerozema.nl/2021/09/27/introduction-to-importing-data-in-python/

# Import package
import scipy.io

# Load MATLAB file: mat
mat = scipy.io.loadmat('data1.mat')

# Print the datatype type of mat
print(type(mat))

import matplotlib.pyplot as plt
import numpy as np

# Print the keys of the MATLAB dictionary
print(mat.keys())

# Subset the array and plot it



mat2 = scipy.io.loadmat('data2.mat')

# Print the datatype type of mat
print(type(mat2))

import matplotlib.pyplot as plt
import numpy as np

# Print the keys of the MATLAB dictionary
print(mat2.keys())

mat3 = scipy.io.loadmat('data3.mat')

# Print the datatype type of mat
print(type(mat3))

import matplotlib.pyplot as plt
import numpy as np

# Print the keys of the MATLAB dictionary
print(mat3.keys())

# Print the type of the value corresponding to the key 'CYratioCyt'
print(type(mat2['CYratioCyt']))

# Print the shape of the value corresponding to the key 'CYratioCyt'
print(np.shape(mat2['CYratioCyt']))

# TODO: WHY WONT matplotlib WORK?
"""
data = mat2['CYratioCyt'][25, 5:]
fig = plt.figure()
plt.plot(data)
plt.xlabel('time (min.)')
plt.ylabel('normalized fluorescence (measure of expression)')
plt.show()
"""