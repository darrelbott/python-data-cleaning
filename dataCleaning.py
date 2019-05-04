# -*- coding: utf-8 -*-
"""
Created to show some ways to clean data
Used Spyder:  Python 3.6
Issues are as follow:
    1) UTF-8 can't decode byte 0xff in position 7: invalid start byte
    2) Inconsistent Column Names
    3) Missing data
    4) Duplicated entries
    5) Data Type Inconsistencies
    6) Renaming columns
    7) Splitting column into multiple columns
    8) Finding a String/Exp and replace
    9) Join 2 columns

@author: Darrel Bott
"""

import pandas as pd
import numpy as np




# ISSUE 1:
# *UTF-8 can't decode byte 0xff in position 7: invalid start byte*
#df = pd.read_csv("unclean_data.csv")

# SOLUTION 1
# utf encoding
df1 = pd.read_csv("unclean_data.csv",encoding='latin1')

df1.head()

# SOLUTION 2
# use in text editor and save it under ENCODING as UTF-8, ISO-8859-1, latin1





# ISSUE 2:
# *Inconsistent Column Names*
# Changing cases
df1.columns
df1.columns = df1.columns.str.upper()
# Renaming columns:
# change DURATION into TIME
df1.rename(columns = {'DURATION':'TIME'})





# ISSUE 3:
# *Missing data*
# delete the row/column with missing data:
# To check for missing data...false means no missing data
df1.isnull() # all data, all columns, all rows shown
df1.isnull().any() # just columns, aggregated all rows
df1.isnull().any().any() # is there any data missing at all from the set?
df1.isnull().sum() # just columns, shown how many per column
df1.isnull().sum().sum() # gives total number of missing data cells
# interpolate the rows, filling NaN with 0
df1_with_0 = df1.fillna(0)
df1_with_0.head() # show to see it worked
# OR interpolate the rows, filling NaN with a mean of all the 
    # numbers in that column
df1['DURATION'].mean() # find the mean of that column
# now fill NaN with the new mean
df1_with_mean = df1.DURATION.fillna(df1['DURATION'].mean()) 





# ISSUE 4:
# *Duplicated entries*
df1.duplicated('MOVIE_TITLE') # check to see if there are any duplicates
df1_drop_dup = df1.drop_duplicates('MOVIE_TITLE') # drop duplicates by
    # movie title





# ISSUE 5:
# *Data Type Inconsistencies*
df = pd.read_csv('file.csv', dtype={'column1':float})
df.dtypes # check what each column data type is
#change GROSS from int64 to float
df.GROSS.dtypes # check
df.GROSS.astype(float) # change





# ISSUE 6:
# *Renaming columns*
df = pd.read_csv("dataset.csv")
df.head() # check data
df.columns # check columns to see if everything is consistant
df.columns = df.columns.str.lower() # make all columns lower case

# Rename some columns
df.rename(columns = {'full name':'full_name', 
                     'date of birth':'date_of_birth'},inplace=True)
df.columns # check





# ISSUE 7
# *Splitting column into multiple columns*
# SOLUTION 1
df.full_name # check
df['firstname'] = df.full_name.str.split(" ").str.get(0) # get all first names
df.firstname # check
df['lastname'] = df.full_name.str.split(" ").str.get(1) # get all last names
df.lastname # check

# SOLUTION 2
df.full_name # check
df1 = df
df1.full_name.str.split(" ",n=1,expand=True)
df.head(3) # check





# ISSUE 8
# *Finding a String/Exp and replace*
df['income.1'] # check
df['income.1'].dtype # check type
df['income.1'].str.replace("$"," ") # replace $ with an empty space 
    #for calculations

df.Salary # check
df.Salary.str.contains('19') # check all strings in salary that contains 19
    #as a boolean
# Could also use MATCH
df.Salary.str.match('19') # check all strings in salary that contains 19
    #as a boolean
# Since there are 1000 rows, using sum might be beneficial to see if there are
    #any that are True and are possibly cut-off
df.Salary.str.contains('19').sum() # 58 total rows
df[df.Salary.str.contains('19')] # show all data rows containing the string 19
    #in the salary column
df[df.Salary.str.contains('19|17')] # show all rows containing the string 19 
    #OR 17 in the salary column





# ISSUE 9
# *Join 2 columns*
df.head() # check
# not the best example in the world but...
df.firstname + df.email # joining first name and their email to check
dfall = df[['firstname','email']].apply("_".join,axis=1) # joining
dfall # check



