#!/usr/bin/env python
# coding: utf-8

# In[2]:


s = "kshitij"


# In[3]:


type(s)


# In[4]:


l = ["kshitij", "18", "data science", "2.0", True]


# In[5]:


type(l)


# In[6]:


n = 23.567


# In[7]:


type(n)


# In[8]:


t = ("kshitij", 18, "data science", 2.0, True)


# In[9]:


type(t)


# In[10]:


var1 = ''


# In[11]:


type(var1)


# In[12]:


var2 = '[DS,ML,Python]'


# In[13]:


type(var2)


# In[14]:


var3 = ['DS','ML','Python']


# In[15]:


type(var3)


# In[16]:


var4 = 1


# In[17]:


type(var4)


# In[18]:


a = 20
b = 10
c = 20/10


# In[19]:


c


# In[20]:


a1 = 20
b1 = 10
c1 = 20%10


# In[21]:


c1


# In[22]:


a2 = 20
b2 = 10
c2 = 20//10


# In[23]:


c2


# In[24]:


a4 = 20
b4 = 10
c4 = 20**10


# In[25]:


c4


# In[26]:


l1 = ["kshitij", 18, 15+4j, True, [1,2,3,4,4], (2,4,5,6), 23.456, [1,2,3,(4,5,6),7,9], False, "me"]


# In[30]:


for i in l1:
    print(i)


# In[1]:


a = int(input())
b = int(input())
count = 0
while a%b == 0:
    a = a//b
    count+=1
if count>0:
    print(f"{a} is divisible by {b} a total of {count} times")
else:
    print(f"{a} is not divisible by {b}")


# In[2]:


l2 = [1,2,3,4,6,8,9,21,12,45,67,89,90,45,32,33,99,66,54,30,5,6,7,8,9]


# In[4]:


for i in l2:
    if i%3 == 0:
        print("divisible by 3")
    else:
        print("not divisible by 3")


# In[5]:


l2


# In[6]:


l2[3] = 5


# In[7]:


l2


# In[11]:


t1 = ("kshitij", 18, "data science", 2.0, True)


# In[12]:


t1[1] = 19


# In[ ]:




