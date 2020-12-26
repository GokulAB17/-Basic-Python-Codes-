#!/usr/bin/env python
# coding: utf-8

# # String:
# String is a datatype in python which consists sequence of characters, digits and special characters. Strings are are surrounded by quotes. We can use single or double 

# Defining & Initialising: Below are different ways of defining and initilising the string

# In[ ]:


# syntax for a string
string = " text/numbers/special characters"


# In[5]:


#Single Quotes:
str_variable1 = ""


# In[6]:


type(str_variable1)


# In[7]:


#Double Quotes:
str_variable2 = "Hello, World!"


# In[8]:


type(str_variable2)


# In[11]:


#Triple Quotes rule:

str_variable3 = """my name is "nikhil" and my age is "25" new"""


# In[13]:


print(str_variable3)


# In[5]:


type(str_variable3)


# Accessing and Indexing the Strings using positive and negative Index:

# ![caption](string-indexing.png)

# In[15]:


str_variable1 = "HELLO_WORLD"


# In[17]:


#accessing in Strings
str_variable1[-10]


# In[18]:


str_variable1[2:5]    #2,3,4   


# In[19]:


str_variable1[8:]


# In[20]:


str_variable1[:5]    #0,1,2,3,4


# In[22]:


#Using negative index:
str_variable1[-5]


# In[21]:


str_variable1[:-1]


# In[11]:


str_variable1[-10:-1]


# In[25]:


str_variable1[-9:1]


# * In python we cant access string more than the length of it, it throws index bound error.

# In[26]:


str_variable1[20]


# Strings are immutable, so once declared you cant change them but you can completely replace the strings in variable.

# In[29]:


#example:
str_variable1[5] = 5


# In[30]:


str_variable1 = "This is new string!!"


# In[31]:


del str_variable1[5]


# In[27]:


del str_variable1


# # Iteration over String:
# We can iterate on string using loops like:
#             1. for 
#             2. while

# In[33]:


for char in 'Hello!!':
    print(char)


# Concatenation of two strings:

# In[31]:


str_variable1 = "Hello "
str_variable2 = " world"


# In[32]:


str_variable1+ " "+str_variable2


# Repetition of strings:

# In[34]:


str_variable1*3


# In[36]:


#We cant concatenate string and Numbers:
str_variable1+str(1)


# In[14]:


#if we want to concatenate then chnage the datatype of number into string using str function
str_variable1+str(1)


# Membership test in strings:

# In[37]:


'h' in 'hello'


# In[38]:


chars = 'hello'
str_variable = 'hello wolrd'
print(chars in str_variable)


# Built In Functions:

# In[49]:


str_variable = 'Hello WORLD'


# In[40]:


#It will make string into camel case:
str_variable.capitalize()


# In[41]:


#It is used for to remove all case distinctions
str_variable.casefold()


# In[42]:


#It is used for padding at both ends
str_variable.center(20)


# In[43]:


#padding the strin with characters
str_variable.center(20,'*')


# In[47]:


#This function return boolean if string endswith characters or words
str_variable.endswith('D')


# In[50]:


str_variable.endswith('WORLD')


# In[51]:


#It finds where the character in the string
str_variable.find('W')


# In[52]:


str_variable.find('w')   #False or It cant find


# In[53]:


#It finds where the character in the string
str_variable.index('W')


# In[54]:


str_variable.index('w')


# ## *Difference between find and index, index throws an error if it does not find the characters in the string

# In[58]:


str_variable = "Hello world"


# In[57]:


#It will return boolean value if it is alpha numeric or not
str_variable.isalnum()


# In[59]:


str_variable = "ABC123"


# In[60]:


str_variable.isalnum()


# In[61]:


str_variable = "Hello"
str_variable.isalpha()


# In[62]:


str_variable.replace("H",'h')


# In[63]:


str_variable.replace("ell",'ol')


# In[66]:


#Splits the string by default with space
str_variable = "Hello;World"
str_variable.split(";")


# In[69]:


str_variable = "HelloWorld"
str_variable.split("o")


# In[70]:


#Returns string into upper case
str_variable = "hello world"
str_variable.upper()


# In[71]:


#Returns string into lower case
str_variable = "HELLO WORLD"
str_variable.lower()


# In[74]:


#Returns how many times the character in string
str_variable.count('HELLO')


# In[75]:


#Returns the length of the string
len(str_variable)


# In[ ]:




