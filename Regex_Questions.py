#!/usr/bin/env python
# coding: utf-8

# In[5]:


# Regex Expression Codes
import re
numRegex = re.compile(r'\d+')


# In[6]:


numRegex.sub('X', '12 drummers,11 pipers, five rings, 3 hens') 


# In[7]:


numRegex.sub("aryan",'1 has 11 Girlfriends')


# In[12]:


new_Regex=re.compile(r'girlfriends')


# In[13]:


new_Regex.sub("arya","someone has 1 girlfriends")


# In[20]:


#usintg the re.verose function
#re.VERBOSE is used  to convert the data into comments multuline commands


new_Regex=re.compile(r"""\d+
                        \s    # uses a tab 
                        \d+""",re.VERBOSE)

new_Regex.search("1 3").group()


# In[25]:


# since compile takes only 2 parameters so we have to use piping to combine all the characters
regex=re.compile(r"foo",re.VERBOSE|re.DOTALL|re.IGNORECASE)


# In[26]:


regex.search("aryan has FOO").group()


# In[42]:


"""" we have to write a regex in such a way it can read all data in the format of 
'42'
•	 '1,234'
•	 '6,368,745'
but not the following:
•	 '12,34,567' (which has only two digits between the commas)
•	 '1234' (which lacks commas)"""
# Here expression ^\d{1,3} contains atleast one to 3 numers
#(,\d{3})*$ it expresses a set of 3 numbers which is having a comma precedding and multiple instances of 3 set
new_regex=re.compile(r"^\d{1,3}(,\d{3})*$")
new_regex.search("13,455,678").group()
                     
                     


# In[52]:


# writinng a regex for finding the name of the person whose name starts with a capital letter
new_regex=re.compile(r"[A-Z]\w+\sNakamoto")
new_regex.search("Aryan Nakamoto is 89").group()
new_regex.search("Mr. Nakamoto").group()
"""AttributeError                            Traceback (most recent call last)
Cell In [51], line 4
      2 new_regex=re.compile(r"[A-Z]\w+\sNakamoto")
      3 new_regex.search("Aryan Nakamoto is 89").group()
----> 4 new_regex.search("Mr. Nakamoto ").group()

AttributeError: 'NoneType' object has no attribute 'group"""


# In[55]:


"""How would you write a regex that matches a sentence where the first
word is either Alice, Bob, or Carol; the second word is either eats, pets, or
throws; the third word is apples, cats, or baseballs; and the sentence ends
with a period? This regex should be case-insensitive. It must match the
following:"""

new_regex=re.compile(r"""(Alice|Bob|Carol)   # first name is Either one of them
                        \s(eats|pets|throws) # either the given word
                        \s (apples|cats|baseballls)  # either of the given word""",re.VERBOSE)
new_regex.search("Alice eats apples")


# In[78]:


"""Write a function that uses regular expressions to make sure the password
string it is passed is strong. A strong password is defined as one that is at
least eight characters long, contains both uppercase and lowercase characters, and has at least one digit.
You may need to test the string against multiple regex patterns to validate its strength."""
# length >8 contains a uppercase and lowercase characters atleast one digit in it

    
                    
check_pass()


# In[66]:


new_regex=re.compile(r"[A-Za-z0-9]+")
new_regex.search("aryan has Hello9").group()


# In[84]:


def check_pass():
    while True:
        password=input()
    
        # checking for the length of the input password
        if len(password)<9:
            print("Oops, Your password length should be greater than 8")
            continue
    # for defining the uppercase characters
        regex_up=re.compile(r"[A-Z]")
        if regex_up.search(password)==None:
            print("Please enter a Uppercase character in the upper bound")
            continue
        regex_down=re.compile(r"[a-z]")
        if regex_down.search(password)==None:
            print("Please enter a Lowercase Character to make your password secure")
            continue
        # for finding whther it contains a digit
        regex_digit=re.compile(r"[0-9]")
        if regex_digit.search(password)==None:
            print("PLease enter a digit in the Password")
            continue
        # for checking that it does not contains a space
        regex_space=re.compile(r"\s")
        if regex_space.search(password)!=None:
            print("The Password should not contains blank Spaces")
            continue
        else:
            print("You entered a Correct Password")
            break


check_pass()


# In[102]:


"""Write a function that takes a string and does the same thing as the strip()
string method. If no other arguments are passed other than the string to
strip, then whitespace characters will be removed from the beginning and
end of the string. Otherwise, the characters specified in the second argument to the function
will be removed from the string."""

# strip function remove whitespaces from the beginning or end of the characters
def prac_3(text,para=None):
    regex_left=re.sub()
    regex_right=re.co
    
    

    
    


# In[114]:


regex_left=re.compile(r"^\s")
re.sub("\s",""," Hello")




# In[99]:


regex=re.compile(r"\w+")
regex.findall("Hello My name is aryan awasthi")


# In[125]:


def rem_spac(s,char=None):
    if char is None:
        regex_left=re.compile(r"\s+")
        regex_right=re.compile(r"\s+")
        
        # substituting the left and right spaces at the certain instances
        s=re.sub("^\s*","",s)
        s=re.sub("\s*$","",s)
        
    else:
        s=re.sub("char","",s)
    return s
    


# In[128]:


rem_spac("Hello:a",":")


# In[ ]:




