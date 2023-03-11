#!/usr/bin/env python
# coding: utf-8

# import matplotlib.pyplot as plt
# x=[13,7,84,90]
# y=[48,93,9,35]
# plt.plot(x,y)
# plt.xlabel("ось x")
# 

# In[9]:


import matplotlib.pyplot as plt 
x=[13,7,84,90] 
y=[48,93,9,35] 
plt.scatter(x,y, color='yellow' ,marker="o") 
plt.xlabel("ось x")
plt.ylabel("ось y")
plt.title("мой график")
plt.show


# In[24]:


import matplotlib.pyplot as plt
x=["apple","samsung","HTC","honor","POCO"]
y=[236,4734,636,669,2883]
plt.bar(x,y) 
plt.plot(x,y,color="pink",label="линия продаж")
plt.xlabel("наименование компаний")
plt.ylabel("количество продаж")
plt.title("обьем продаж смартфонов")
plt.grid ()
plt.text(4,8,"тренд")
plt.show


# In[30]:


import matplotlib.pyplot as plt
labels=["apple","samsung","HTC","honor","POCO"]
vals=[236,4734,636,669,2883]
plt.pie(vals,labels=labels)
plt.title("обьем продаж")
plt.show ()


# In[ ]:




