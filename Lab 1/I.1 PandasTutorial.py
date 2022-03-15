#!/usr/bin/env python
# coding: utf-8

# # Introducing Pandas
# 
# Pandas is a Python library that makes handling tabular data easier. Since we're doing data science - this is something we'll use from time to time!
# 
# It's one of three libraries you'll encounter repeatedly in the field of data science:
# 
# ## Pandas
# Introduces "Data Frames" and "Series" that allow you to slice and dice rows and columns of information.
# 
# ## NumPy
# Usually you'll encounter "NumPy arrays", which are multi-dimensional array objects. It is easy to create a Pandas DataFrame from a NumPy array, and Pandas DataFrames can be cast as NumPy arrays. NumPy arrays are mainly important because of...
# 
# ## Scikit_Learn
# The machine learning library we'll use throughout this course is scikit_learn, or sklearn, and it generally takes NumPy arrays as its input.
# 
# So, a typical thing to do is to load, clean, and manipulate your input data using Pandas. Then convert your Pandas DataFrame into a NumPy array as it's being passed into some Scikit_Learn function. That conversion can often happen automatically.
# 
# Let's start by loading some comma-separated value data using Pandas into a DataFrame:

# In[13]:


import pandas as pd

df = pd.read_csv("PastHires.csv")

df


# head() is a handy way to visualize what you've loaded. You can pass it an integer to see some specific number of rows at the beginning of your DataFrame:

# In[11]:


df.head(3)


# You can also view the end of your data with tail():

# In[15]:


df.tail(4)


# In[16]:


type(df)


# We often talk about the "shape" of your DataFrame. This is just its dimensions. This particular CSV file has 13 rows with 7 columns per row:

# In[4]:


df.shape


# The total size of the data frame is the rows * columns:

# In[5]:


df.size


# The len() function gives you the number of rows in a DataFrame:

# In[6]:


len(df)


# If your DataFrame has named columns (in our case, extracted automatically from the first row of a .csv file,) you can get an array of them back:

# In[7]:


df.columns


# Extracting a single column from your DataFrame looks like this - this gives you back a "Series" in Pandas:

# In[18]:


df[['Years Experience','Hired']]


# You can also extract a given range of rows from a named column, like so:

# In[21]:


df['Hired'][3:5]


# Or even extract a single value from a specified column / row combination:

# In[23]:


df['Hired'][5]


# To extract more than one column, you pass in a list of column names instead of a single one:

# In[11]:


df[['Years Experience', 'Hired']]


# You can also extract specific ranges of rows from more than one column, in the way you'd expect:

# In[12]:


df[['Years Experience', 'Hired']][:5]


# Sorting your DataFrame by a specific column looks like this:

# In[25]:


df.sort_values(['Years Experience','Hired'])


# You can break down the number of unique values in a given column into a Series using value_counts() - this is a good way to understand the distribution of your data:

# In[27]:


degree_counts = df['Level of Education'].value_counts()
degree_counts


# Pandas even makes it easy to plot a Series or DataFrame - just call plot():

# In[29]:


get_ipython().run_line_magic('matplotlib', 'inline')
degree_counts.plot(kind='bar')


# ## Exercise
# 
# Try extracting rows 5-10 of our DataFrame, preserving only the "Previous Employers" and "Hired" columns. Assign that to a new DataFrame, and create a histogram plotting the distribution of the previous employers in this subset of the data.

# In[33]:


df_new = df[['Previous employers', 'Hired']][5:11]

df_new


# In[37]:


counts = df_new['Previous employers'].value_counts()


# In[38]:


counts.plot(kind='bar')


# In[ ]:




