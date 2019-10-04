#!/usr/bin/env python
# coding: utf-8

# In[18]:


# version_check function recieves two version strings s1 and s2, and compare them. 
def version_check(s1,s2):
        
    if s1>s2:
        return print('{} is greater than {}'.format(s1,s2))
    elif s1==s2:
        return print('{} is equal {}'.format(s1,s2))
    else:
        return print('{} is less than {}'.format(s1,s2))

#test for different test cases
if __name__ == '__main__':
    
    test_cases=[('1.1.1','1.1'),('2.1','1.1'),('1','1.1'),('v1.3','v1.2'),('3-1','3-3'),('3/1','3/22'),('10.1','10.1')]
    
    for s1,s2 in test_cases:
        version_check(s1,s2)

