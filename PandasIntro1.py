
# coding: utf-8

# In[1]:

import numpy as np
import pandas as pd


# Create 5 random numbers:

# In[2]:

s = pd.Series(np.random.randn(5), index=['a', 'b', 'c', 'd', 'e'])


# Call "s" to see its values:

# In[3]:

s


# data type is given automatically (float)

# Automatically create random numbers and assign indexes (with no names)

# In[4]:

pd.Series(np.random.randn(5))


# The follwong creates a dictionnary assigning to "columns" (1 value to each column, in this case)

# In[5]:

d = {'a' : 0., 'b' : 1., 'c' : 2.}


# Let's check how "d" looks like.

# In[6]:

d


# Another way to visualize it using the "Series" class:

# In[7]:

pd.Series(d)


# If I want to read values in any desired order:

# In[8]:

pd.Series(d, index=['b', 'c', 'd', 'a'])


# Notice "NaN" (not a number). Standard value in Pandas.

# ndarray: let's first call "s" and then its first value

# In[9]:

s


# In[10]:

s[0]


# We can use as well regular slice notation:

# In[11]:

s[:3]


# If I want a subset of the data (for example only the values above the median) Pandas allow us to do so easily:

# In[12]:

s[s > s.median()]


# Another syntax to print out a subset of values (using double square brackets)

# In[13]:

s[[4, 3, 1]]


# To run the exponential of each value in the series (!s" in our case):

# In[14]:

np.exp(s)


# Calling a value using its index ("a" in this case):

# In[15]:

s['a']


# I can even explicitly set any value in a series (we assign the value 12 to "e"):

# In[16]:

s['e'] = 12


# In[17]:

s


# We can as well check if a value is or isn't in a series:

# In[19]:

'e' in s


# In[18]:

'f' in s


# It can turn useful in creating code:

# In[20]:

if "e" in s:
    print(s["e"])


# To get a value back (but only if it exists, otherwise it doesn't return anything):

# In[21]:

s.get('f')


# In[22]:

s.get('e')


# In[ ]:




# In[23]:

s.get('f', np.nan)


# We can apply any operation to our vectors:

# In[24]:

s + s


# In[25]:

s * 2


# In[26]:

np.exp(s)


# Let's see how we can use different slices of series, and their possible interactions/operations:

# In[27]:

s[1:]


# In[28]:

s[:-1]


# In[29]:

s[1:] + s[:-1]


# Notice how we are returned "NaN" values. This happens because "a" is not present in the first element and "e" is not present in the second one.
# The code then returns us a "NaN", since for those pairs one of the 2 addends is a NaN.

# DATA FRAME:

# In[30]:

d = {'one' : pd.Series([1., 2., 3.], index=['a', 'b', 'c']), 'two' : pd.Series([1., 2., 3., 4.], index=['a', 'b', 'c', 'd'])}


# We assign "d" to "df" defining it as a data frame:

# In[31]:

df = pd.DataFrame(d)


# We tehn call the data frame we just created:

# In[32]:

df


# If we want to select a subset of the data frame (we exclude "c" here):

# In[33]:

pd.DataFrame(d, index=['d', 'b', 'a'])


# If we want to reorder the columns and/or add new columns:

# In[34]:

pd.DataFrame(d, index=['d', 'b', 'a'], columns=['two', 'three'])


# Another syntax to create dictionnaries:

# In[35]:

d = {'one' : [1., 2., 3., 4.],'two' : [4., 3., 2., 1.]}


# In[36]:

pd.DataFrame(d)


# We can then assign new indexes:

# In[37]:

pd.DataFrame(d, index=['a', 'b', 'c', 'd'])


# We create an array filled with value "0" (in different formats) and assign columns names and related types (integer, float and string) and length (i4, f4, a10):

# In[38]:

data = np.zeros((2,), dtype=[('A', 'i4'),('B', 'f4'),('C', 'a10')])


# In[39]:

data


# We can then assign new values to the array created above:

# In[40]:

data[:] = [(1,2.,'Hello'), (2,3.,"World")]


# And then see how it looks by calling it:

# In[41]:

data


# We then created a related dataframe:

# In[42]:

pd.DataFrame(data)


# We can then assign different names to the rows/indexes:

# In[43]:

pd.DataFrame(data, index=['first', 'second'])


# Or assign different names to the columns:

# In[44]:

pd.DataFrame(data, columns=['C', 'A', 'B'])


# From a list of dicts:

# In[47]:

data2 = [{'a': 1, 'b': 2}, {'a': 5, 'b': 10, 'c': 20}]


# In[48]:

pd.DataFrame(data2)


# In[49]:

pd.DataFrame(data2, index=['first', 'second'])


# In[50]:

pd.DataFrame(data2, columns=['a', 'b'])


# From a dict of tuples:

# In[51]:

pd.DataFrame({('a', 'b'): {('A', 'B'): 1, ('A', 'C'): 2},
('a', 'a'): {('A', 'C'): 3, ('A', 'B'): 4},
('a', 'c'): {('A', 'B'): 5, ('A', 'C'): 6},
('b', 'a'): {('A', 'C'): 7, ('A', 'B'): 8},
('b', 'b'): {('A', 'D'): 9, ('A', 'B'): 10}})


# Column selection, addition, deletion:

# Selection:

# In[52]:

df['one']


# Addition (multiplication here):

# In[53]:

df['three'] = df['one'] * df['two']


# In[54]:

df


# We can create a new column and populate it with a selected conditional value ("flag"-> true/false here):

# In[55]:

df['flag'] = df['one'] > 2


# In[56]:

df


# Deletion:

# In[57]:

del df['two']


# Deletion using "pop" (to use the value deleted allowing us to process it, if needed):

# In[58]:

three = df.pop('three')


# In[60]:

three


# In[59]:

df


# Inserting a scalar value, it gets propagated to the whole column:

# In[61]:

df['foo'] = 'bar'


# In[62]:

df


# Inserting a Series that does not have the same index as the DataFrame

# In[63]:

df['one_trunc'] = df['one'][:2]


# In[64]:

df


# If we insert a new column (1) giving it a value of "bar" with the name "one":

# In[65]:

df.insert(1, 'bar', df['one'])


# In[66]:

df


# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:



