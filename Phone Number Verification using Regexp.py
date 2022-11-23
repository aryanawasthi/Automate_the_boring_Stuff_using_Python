#!/usr/bin/env python
# coding: utf-8

# In[8]:


#python program to find that the input number is a phone number is valid number or not


# In[46]:


def isphone_num(num):
    #checking for the lenth of the number and if it is not equal to 10 then return False
    if len(num)!=12:
        return False
    # for each starting characters we have to check whether the input if it is not decimel 
    for i in range(3):
        if not num[i].isdecimal():
            return False
    # if the character at 4 the position or 3rd index is not zero then we have return False
    if  num[3]!="-":
        return False
    for i in range(4,7):
        if not num[i].isdecimal():
            return False
        
    if num[7]!="-":
        return False
    for i in range(8,12):
        if not num[i].isdecimal():
            return False
    return True


        


# In[50]:


#for Indian Mobile Number in +91-7456830168 form 
def isphn_valid(num):
    if num[0]!="+":
        return False
    for i in range(1,3):
        if not num[i].isdecimal():
            return False
    if num[3]!="-":
        return False
    for i in range(4,14):
        if not num[i].isdecimal():
            return False
    return True


# In[145]:


# defining a function in a big text and finding the required regexp expression
def isregexp(text):
    #iterationg throughout the loop to break it into a set of 14 characters 
    for i in range(len(text)-13):
        if isphn_valid(text[i:i+14]):
            return True
    return False

        


# In[146]:


text="hello this is aryan awasthi my phone number is +81-8989898989"
isregexp(text)


# In[143]:


number="+91-7878908009"
print(isphn_valid(number))


# In[52]:


#using the regex expression to solve the same problem
#importing the necessary libraries
import re


# In[122]:


myregexp=re.compile(r'\+\d{2}\-\d{10}')


# In[125]:


mo=myregexp.search("+91-7456830168")


# In[126]:


print(mo.group())


# In[102]:


my_re=re.compile(r"\+abc")
mo1=my_re.search("Hello welcome to the +abc")


# In[103]:


print(mo1.group())


# In[148]:


# writing the same function using the regexp expression
def is_present_regex(text):
    #import the libraries
    import re
    # deinfing the regexp
    regexp=re.compile(r'\+\d{2}\-\d{10}')
    mo=regexp.search(text)
    print(f"The text is present at {mo.group()}")


# In[149]:


is_present_regex(text)


# In[ ]:




