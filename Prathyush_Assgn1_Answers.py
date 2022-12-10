#!/usr/bin/env python
# coding: utf-8

# # 1. In the below elements which of them are values or an expression? eg:- values can be integer or string and expressions will be mathematical operators.
# * 
# 'hello'
# -87.8
# - 
# / 
# +	
# 6 
# 

# In[8]:


print('helo is a ::',type('hello'))
print('-87.8 is a ::',type(-87.8))
print('6 is a ::',type(6))


# In[ ]:


Answers :
       From Above we can conclude that : 
   1. 'helo' is a sting
   2. -87.8 is a float datatype
   3. -,/,+ are expression or mathematical operators
   4. 6 is a integer data type


# # 2. What is the difference between string and variable?
# Answer :
# A string is bascially a group of letters or numbers represented in a single quotes
# A variable is used to assigned some value to it, whihc can be dynamically changed later.

# # 3. Describe three different data types.
# string date type - example 'prathyush', '546PL'
# Interger data type - example 5,85,42569,99999
# float data type - example 25.36,99.0
# boolean data type - example- True, False
# 

# # 4. What is an expression made up of? What do all expressions do?
# Answer :
# An expressiin bascially does a mathematical operation/ logical operation/ assignment operation
# It will have comparitive, logical , varaibles combined to gether to perform s=certain action

# # 5. This assignment statements, like spam = 10. What is the difference between an expression and a statement?
# In programming language terminology, an “expression” is a combination of values and functions that are combined and interpreted by the compiler to create a new value, as opposed to a “statement” which is just a standalone unit of execution and doesn't return anything

# # 6. After running the following code, what does the variable bacon contain?
# bacon = 22
# bacon + 1
# 

# In[14]:


bacon=22
bacon+1


# In[15]:


bacon


# In[ ]:


Answer :
    Since we did not assign 'bacon' with new incremented value , previous value '22' will only be assigned to bacon


# # 7. What should the values of the following two terms be?
# 'spam' + 'spamspam'
# 'spam' * 3
# 

# In[18]:


'spam' + 'spamspam'


# In[19]:


'spam' * 3


# In[ ]:


Answer : Both return same output 'spamspamspam'


# # 8. Why is eggs a valid variable name while 100 is invalid?
# Answer :
#     eggs is basically a string data type we can assign a value to it. But 100 being a interger, it by itself is a value we cant assign a  value to a value.

# # 9. What three functions can be used to get the integer, floating-point number, or string version of a value?
# Answer :
# we have to use cast function to convert them to diff data types as below
# type conversion
# 

# In[21]:


A=25.260


# In[23]:


p=int(A)
print(p)
print(type(p))


# In[24]:


z=str(A)
print(z)
print(type(z))


# In[25]:


c=float(A)
print(c)
print(type(c))


# # 10. Why does this expression cause an error? How can you fix it?
# 'I have eaten ' + 99 + ' burritos.'
# Answer:
# We are trying to add a numerical value to a string , which is not possible
# to achieve it put 99 also in single quotes as below
# 

# In[27]:


'I have eaten ' + '99' + ' burritos.'

