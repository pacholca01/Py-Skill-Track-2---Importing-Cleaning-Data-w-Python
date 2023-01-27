from urllib.request import urlretrieve
import pandas as pd

# from matplotlib import pyplot as plt


""" file = 'winequality-white.csv' video """
#import csv

url = 'http://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-white.csv'
file = 'winequality-white.csv'
urlretrieve(url, file)

df = pd.read_csv(file, sep=';')
print(df.head())

""" Importing flat files from the web: your turn! """
url = 'https://assets.datacamp.com/production/course_1606/datasets/winequality-red.csv'  # Assign url of file: url
file = 'winequality-red.csv'
urlretrieve(url, file)  # Save file locally

# Read file into a DataFrame and print its head
df = pd.read_csv(file, sep=';')
print(df.head())

"""Opening and reading flat files from the web"""
df = pd.read_csv(url, sep=';')  # Read url directly into a DataFrame: df
print(df.head())

# Plot first column of df
# Error here for numpy with matpolt lib
# https://github.com/matplotlib/matplotlib/issues/22333
"""
# https://stackoverflow.com/questions/70591652/type-error-in-pycharm-using-pandas-and-seaborn
pip3 install numpy==1.22.2

That didn't work. Try running this section in a jupyter notebook

df.iloc[:, 0].hist()
plt.xlabel('fixed acidity (g(tartaric acid)/dm$^3$)')
plt.ylabel('count')
plt.show()
"""

""" Importing non-flat files from the web """
"""
url = 'https://assets.datacamp.com/course/importing_data_into_r/latitude.xls'
xls = pd.read_excel(url, sheet_name=None)           # in order to import all sheets you need to pass None to the argument sheet_name
print(xls.keys())        # Print the names of the sheets in the Excel spreadsheet; these will be the keys of the dictionary
print(xls['1700'].head())       # Print the head of the first sheet (using its name, NOT its index)
"""

#
from urllib.request import urlopen, Request

url = "https://www.wikipedia.org/"
request = Request(url)
response = urlopen(request)
html = response.read()
response.close()

from urllib.request import urlopen, Request

url = "https://www.wikipedia.org/"
request = Request(url)
response = urlopen(request)
html = response.read()
response.close()

import requests

r = requests.get(url)
text = r.text
print(text)

"""Performing HTTP requests in Python using urllib"""
url = "https://campus.datacamp.com/courses/1606/4135?ex=2"  # Specify the url
request = Request(url)  # This packages the request: request
response = urlopen(request)  # Sends the request and catches the response: response
print(type(response))  # Print the datatype of response
response.close()  # Be polite and close the response!

"""Printing HTTP request results in Python using urllib"""
url = "https://campus.datacamp.com/courses/1606/4135?ex=2"
request = Request(url)  # This packages the request
response = urlopen(request)  # Sends the request and catches the response: response
html = response.read()  # Extract the response: html
print(html)
response.close()

"""Performing HTTP requests in Python using requests"""
import requests

url = "http://www.datacamp.com/teach/documentation"
r = requests.get(url)  # Packages the request, send the request and catch the response: r
text = r.text  # Extract the response: text
print(text)

"""
from bs4 import BeautifulSoup

url = 'https//www.crummy.com/software/BeautifulSoup/'
r = requests.get(url)
html_doc = r.text
soup = BeautifulSoup(html_doc)
"""

from bs4 import BeautifulSoup

url = 'https://www.python.org/~guido/'
r = requests.get(url)           # Package the request, send the request and catch the response: r
html_doc = r.text           # Extracts the response as html: html_doc

soup = BeautifulSoup(html_doc)      # Create a BeautifulSoup object from the HTML: soup
pretty_soup = soup.prettify()       # Prettify the BeautifulSoup object: pretty_soup

print(pretty_soup)


"""Turning a webpage into data using BeautifulSoup: getting the text
"""
url = 'https://www.python.org/~guido/'
r = requests.get(url)
html_doc = r.text

# Create a BeautifulSoup object from the HTML: soup
soup = BeautifulSoup(html_doc)

# Get the title of Guido's webpage: guido_title
guido_title = soup.title
print(guido_title)

# Get Guido's text: guido_text
guido_text = soup.text
print(guido_text)

"""Test of Json file Import"""
import json
with open('sample-data.json', mode='r') as json_file :
    json_data = json.load(json_file)
print(json_data)

"""Loading and exploring a JSON"""
# Load JSON: json_data
with open("a_movie.json") as json_file:
    json_data = json.load(json_file)

# Print each key-value pair in json_data
for k in json_data.keys():
    print(k + ': ', json_data[k])


"""APIs and interacting with the world wide web - Video"""
import requests
url = "https://www.omdbapi.com/?apikey=ff9aeef5&t=hackers"      #?t=hackers is a query string

""" We are asking the api to query the data from the movie hackers by using the 't' parameter
You need to go to https://www.omdbapi.com/ to register for an api key. Api keys will expire. """

r = requests.get(url)
json_data = r.json()
for k in json_data :
    print(k)
print('\n')
for k in json_data :
    print(json_data[k])

"""API requests"""
url = 'http://www.omdbapi.com/?apikey=72bc447a&t=the+social+network'
r = requests.get(url)
print(r.text)

"""JSON–from the web to Python"""
url = 'http://www.omdbapi.com/?apikey=72bc447a&t=social+network'
r = requests.get(url)
json_data = r.json()

for k in json_data.keys():
    print(k + ': ', json_data[k])

"""Checking out the Wikipedia API"""
url = 'https://en.wikipedia.org/w/api.php?action=query&prop=extracts&format=json&exintro=&titles=pizza'
r = requests.get(url)
json_data = r.json()

# Print the Wikipedia page extract
pizza_extract = json_data['query']['pages']['24768']['extract']
print(pizza_extract)

# Twitter API Key: 153xflf8iFVXnPeN6M9VJY9Fr
# Twitter API Key Secret: w6QxGGAb6gAVu9MDcW7EB0SdVVJbzFLTrDXGl4BaCK2pHeWrXT

"""Streaming tweets"""
# Store credentials in relevant variables
consumer_key = "nZ6EA0FxZ293SxGNg8g8aP0HM"
consumer_secret = "fJGEodwe3KiKUnsYJC3VRndj7jevVvXbK2D5EiJ2nehafRgA6i"
access_token = "1092294848-aHN7DcRP9B4VMTQIhwqOYiB14YkW92fFO8k8EPy"
access_token_secret = "X4dHmhPfaksHcQ7SCbmZa2oYBBVSD2g8uIHXsp5CTaksx"

# Create your Stream object with credentials
stream = tweepy.Stream(consumer_key, consumer_secret, access_token, access_token_secret)

# Filter your Stream variable
stream.filter(track =["clinton", "trump", "sanders", "cruz"])

"""
# Import package
import json

# String of path to file: tweets_data_path
tweets_data_path = 'tweets.txt'

# Initialize empty list to store tweets: tweets_data
tweets_data = []

# Open connection to file
tweets_file = open(tweets_data_path, "r")

# Read in tweets and store in list: tweets_data
for line in tweets_file:
    tweet = json.loads(line)
    tweets_data.append(tweet)

# Close connection to file
tweets_file.close()

# Print the keys of the first tweet dict
print(tweets_data[0].keys())

"""

"""Twitter data to DataFrame"""
"""
# Import package
import pandas as pd

# Build DataFrame of tweet texts and languages
df = pd.DataFrame(tweets_data, columns=['text', 'lang'])

# Print head of DataFrame
print(df.head())
"""

"""A little bit of Twitter text analysis
"""

"""# Initialize list to store tweet counts
[clinton, trump, sanders, cruz] = [0, 0, 0, 0]

# Iterate through df, counting the number of tweets in which
# each candidate is mentioned
for index, row in df.iterrows():
    clinton += word_in_text('clinton', row['text'])
    trump += word_in_text('trump', row['text'])
    sanders += word_in_text('sanders', row['text'])
    cruz += word_in_text('cruz', row['text'])"""

"""Plotting your Twitter data"""

"""# Import packages
import seaborn as sns
import matplotlib.pyplot as plt


# Set seaborn style
sns.set(color_codes=True)

# Create a list of labels:cd
cd = ['clinton', 'trump', 'sanders', 'cruz']

# Plot the bar chart
ax = sns.barplot(cd, [clinton, trump, sanders, cruz])
ax.set(ylabel="count")
plt.show()
"""