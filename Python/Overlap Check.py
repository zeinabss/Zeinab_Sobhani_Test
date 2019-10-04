#!/usr/bin/env python
# coding: utf-8

# In[15]:


# isoverlap function checks whether two priveded ranges in the format of two tuple range1=(x1,x2) and range2=(x3,x4) overlap
def isoverlap(range1,range2):
    ranges=[range1,range2]
    try:
        ranges=sorted(ranges, key=lambda x:x[0])
        x2=ranges[0][1]
        x3=ranges[1][0]
    except Exception:
        return print('arguments should be tuples')
    if x3<x2:
        return True 
    return False

#test for different test cases
if __name__ == '__main__':
    
    test_cases=[((1,2),(2,3)),((1,4),(2,3)),((2,4),(1,3)),((-1,0),(0,1)),((-1,1),(0,1)),((-5,-1),(-3,-2)),((-10,-5),(-4,-3)),((1,2),(1,2))]
    
    for range1,range2 in test_cases:
        if isoverlap(range1,range2):
            print('{} and {} overlap'.format(range1,range2))
        else:
            print("{} and {} don't overlap".format(range1,range2))
        

