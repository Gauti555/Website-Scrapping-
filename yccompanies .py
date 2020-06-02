#!/usr/bin/env python
# coding: utf-8

# In[1]:


import bs4 as bs
import lxml
from urllib import request


# In[10]:



import urllib
source = urllib.request.urlopen('https://www.ycombinator.com/topcompanies').read()


# In[11]:


soup = bs.BeautifulSoup(source, 'lxml')
soup


# In[12]:


print(soup.title)


# In[13]:


print(soup.title.string)


# In[14]:


print(soup.find_all('a'))


# In[24]:


website=[]
for url in soup.find_all('a'):
    website.append(url.text.strip('Apply'))
print(website)
   


# In[26]:


name=[]
for url in soup.find_all('a'):
    print(url.text)
  


# In[29]:


for url in soup.find_all('a'):
    print(url.text.strip('Apply'))
    


# In[33]:



for url in soup.find_all('a'):
    print(url.get('href'))

    


# In[ ]:





# In[20]:


for div in soup.find_all('div'):
    print(div)


# In[22]:


body  = soup.body
for paragraph in body.find_all('p'):
    print(paragraph.text)


# In[ ]:




