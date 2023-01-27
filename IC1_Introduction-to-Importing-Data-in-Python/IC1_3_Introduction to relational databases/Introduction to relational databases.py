# Introduction to relational databases
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sqlalchemy import create_engine                    # Import necessary module

# Codd's 12 Rules
# https://www.tutorialspoint.com/dbms/dbms_codds_rules.htm

""" What are the tables in the database? """
engine = create_engine('sqlite:///Chinook.sqlite')      # Create engine: engine
table_names = engine.table_names()                      # Save the table names to a list: table_names
print(table_names)                                      # Print the table names to the shell

""" Querying relational databases in Python  """
"""
con = engine.connect()
rs  = con.execute("SELECT * FROM Orders")               # rs - relevant sql
df  = pd.DataFrame(rs.fetchall())         
df.columns = rf.keys()              
con.close()

print(df.head())
"""

# alternatively you can use the context manager construct to open a connection
"""
with engine.connect() as con :
    rs  = con.execute("SELECT * FROM Orders")               # rs - relevant sql
    df  = pd.DataFrame(rs.fetchmany(5))                     # fetch 5
    df.columns = rf.keys()  
"""

"""The Hello World of SQL Queries!"""
engine = create_engine('sqlite:///Chinook.sqlite')                      # Create engine: engine
con = engine.connect()                                                  # Open engine connection: con
rs = con.execute("SELECT * FROM Album")                                 # Perform query: rs
df = pd.DataFrame(rs.fetchall())                                        # Save results of the query to DataFrame: df
con.close()                                                             # Close connection
print(df.head())                                                        # Print head of DataFrame df
print("\n")

"""Customizing the Hello World of SQL Queries"""
# Open engine in context manager
# Perform query and save results to DataFrame: df
with engine.connect() as con:
    rs = con.execute("SELECT LastName, Title FROM Employee")
    df = pd.DataFrame(rs.fetchmany(3))
    df.columns = rs.keys()

print(len(df))          # Print the length of the DataFrame df
print(df.head())        # Print the head of the DataFrame df
print("\n")

"""Filtering your database records using SQL's WHERE"""
engine = create_engine('sqlite:///Chinook.sqlite')    # Create engine: engine
# Open engine in context manager
# Perform query and save results to DataFrame: df
with engine.connect() as con:
    rs = con.execute("SELECT * FROM Employee WHERE EmployeeId >= 6")
    df = pd.DataFrame(rs.fetchall())
    df.columns = rs.keys()

print(df.head())        # Print the head of the DataFrame df
print("\n")

"""Ordering your SQL records with ORDER BY"""
engine = create_engine('sqlite:///Chinook.sqlite')        # Create engine: engine

# Open engine in context manager
with engine.connect() as con:
    rs = con.execute("SELECT * FROM Employee ORDER BY BirthDate ASC")
    df = pd.DataFrame(rs.fetchall())
    df.columns = rs.keys()      # Set the DataFrame's column names

print(df.head())        # Print head of DataFrame
print("\n")

""" Querying relational databases directly with pandas """
# Alternatively you can just use the following code to perform the same action as the engine in the context manager
engine = create_engine('sqlite:///Chinook.sqlite')      # Create engine: engine
df = pd.read_sql_query("SELECT * FROM Album", engine)      # Execute query and store records in DataFrame: df
print(df.head())        # Print head of DataFrame

# Open engine in context manager and store query result in df1
with engine.connect() as con:
    rs = con.execute("SELECT * FROM Album")
    df1 = pd.DataFrame(rs.fetchall())
    df1.columns = rs.keys()

print(df.equals(df1))       # Confirm that both methods yield the same result

"""Pandas for more complex querying"""
engine = create_engine('sqlite:///Chinook.sqlite')        # Create engine: engine
df = pd.read_sql_query("SELECT * FROM Employee WHERE EmployeeId >= 6 ORDER BY BirthDate",engine)       # Execute query and store records in DataFrame: df
print(df.head())        # Print head of DataFrame

"""The power of SQL lies in relationships between tables: INNER JOIN"""

# Open engine in context manager
# Perform query and save results to DataFrame: df
with engine.connect() as con:
    rs = con.execute("SELECT Title, Name FROM Album AS A INNER JOIN Artist AS B ON A.ArtistID = B.ArtistID")
    df = pd.DataFrame(rs.fetchall())
    df.columns = rs.keys()

print(df.head())        # Print head of DataFrame df

"""Filtering your INNER JOIN"""
# Execute query and store records in DataFrame: df
df = pd.read_sql_query("SELECT * FROM PlaylistTrack INNER JOIN Track on PlaylistTrack.TrackId = Track.TrackId WHERE Milliseconds < 250000", engine)

print(df.head())        # Print head of DataFrame