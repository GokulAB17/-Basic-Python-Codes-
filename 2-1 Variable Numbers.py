#!/usr/bin/env python
# coding: utf-8

# # Variables:
# Variables are used to store information, which can be used across the program. Variables can be changed across the program. It is like a name to the location where data/ value is stored.

# In python, declaring and initialising of the variables is done at same time.

# In[2]:


#example:
variable_1 = "hello world!"


# "=" acts as a assignment operator which means right side of the value is getting assignment to left side variable.

# # *Follow the rules of identifiers for naming convention of Variables.

# # DataTypes
# Datatypes are type of data which will be stored in variable, tell the compiler or interpretor how the programmer intends to use the data.
# We have following Datatypes in Python:
#     1. Numbers
#     2. String
#     3. Boolean
#     4. List
#     5. Tuple
#     6. Set
#     7. Dictionary

# # Numbers:
# Numbers consists of three categories in python:
#     1. Integers, which are whole numbers eg: 1,2,3,4
#     2. Float , which are fractions eg: 1.0,1.2,2.3
#     3. Complex Numbers, eg: a+bi, where a & b are whole numbers

# ## Integers
# Integers are similar to whole numbers numbers. int is the function which can convert float into integers. You can have apply all mathmatical operation on integers.

# In[3]:


int_variable1 = 2
int_variable2 = 10


# In[12]:


#summation/ addition
float(int_variable1)+int_variable2


# In[5]:


#Subtraction
int_variable1-int_variable2


# In[6]:


#multiplication
int_variable1*int_variable2


# In[14]:


#division
int_variable1//int_variable2


# In[9]:


#division
int_variable1%int_variable2


# In[10]:


#power
int_variable2**int_variable1


# In[11]:


#we can used type function to know which datatype is the variable:
type(int_variable1)


# ## Float 
# Float are fractions. We can convert int into floats. 
# Even 10.0 is also float and also 10.0000000089

# In[16]:


float_variable1 = 1.23
float_variable2 = 2.56


# In[17]:


#Addition:
int(float_variable1) + int(float_variable2)


# In[22]:


#Substraction:
float_variable1 - float_variable2


# In[23]:


#multiplication:
float_variable1 * float_variable2


# In[24]:


#Division:
float_variable1/float_variable2


# In[25]:


#Division:
float_variable1%float_variable2


# In[26]:


#power
float_variable1**float_variable2


# In[18]:


#Float can store upto 15 decimals
float_variable3 = 1.00000000000000000000000000002


# In[19]:


float_variable3


# In[ ]:




