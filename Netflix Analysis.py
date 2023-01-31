#!/usr/bin/env python
# coding: utf-8

# In[1]:


#import libraries
import pandas as pd
import matplotlib.pyplot as plt


# In[2]:


#read file
netflix_data= pd.read_csv(r'/Users/yaa.adobea/Downloads/netflix_titles (1).csv')


# In[3]:


#view first and last five rows of your data
netflix_data.head()


# In[4]:


netflix_data.tail()


# In[5]:


#to see the columns
netflix_data.columns


# In[6]:


netflix_data.info()


# In[7]:


netflix_data.describe()  #statiscal analysis


# In[8]:


netflix_data.describe(include= object)


# In[9]:


netflix_data['country']


# In[10]:


netflix_data['type'].unique()


# In[11]:


netflix_data.isnull().sum()  #check for null values


# In[12]:


#checking for duplicates
netflix_data.duplicated(subset='director').sum()


# In[13]:


netflix_data.iloc[0]      #iloc is used for indexing rows by positions


# In[14]:


netflix_data.set_index('title',inplace=True)


# In[15]:


netflix_data.head()


# In[16]:


netflix_data.iloc[0]


# In[17]:


pd.DataFrame(netflix_data.loc['Ganglands'])     #loc is used to index by name(indexed column)


# In[18]:


netflix_data[netflix_data['type']=='Movie'] #filtering only movies 


# In[19]:


netflix_data[netflix_data['release_year']>1990]


# In[20]:


netflix_data[netflix_data['country']== 'Ghana']   #the number of movies starred in Ghana


# In[21]:


netflix_data['type'].value_counts()


# In[22]:


netflix_data['country'].value_counts()[:10].plot(kind='bar')


# In[23]:


#when was the oldest movie/tv show release
netflix_data['release_year'].min()


# In[24]:


netflix_data[netflix_data['release_year']==1925]


# In[25]:


#rewarding top 10 directors with the top 10 movies
netflix_data['director'].value_counts()[:10]


# In[50]:


#recommending a 30 minutes movies for a friend
movies=netflix_data[netflix_data['type']=='Movie']
movies


# In[51]:


movies['mins']=movies['duration'].str.replace('min', ' ')


# In[52]:


movies


# In[53]:


movies['mins']=pd.to_numeric(movies['mins'])


# In[54]:


movies


# In[55]:


movies['mins'].min()


# In[59]:


movies[movies['mins']<=30]


# In[61]:


movies[movies['mins']<=30].tail()


# In[66]:


#Recommending LBGTQ movies
movies[movies['listed_in'].str.contains('LGBTQ')]


# In[ ]:




