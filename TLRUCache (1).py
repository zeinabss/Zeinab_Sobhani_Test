#!/usr/bin/env python
# coding: utf-8

# In[8]:


from collections import OrderedDict
import time as t
from time import time

#define a class for each entry in the cache where value is specified
#put_time is the time the entry is entered in the cache

class Entry:
    def __init__(self, value,put_time=time()):
        self.value=value
        self.put_time=put_time


# define a class for Time-aware Least Recently Used Cache 
# capacity is the capacity of the cache default is 10 slots
# ttu (Time To Use) is the time the entries will remain in the cache in seconds

class TLRUCache:
    def __init__(self, capacity=10,ttu=20):
        self.capacity=capacity
        self.cache_dict=OrderedDict()
        self.ttu=ttu

    # get method extracts the data from cache if exists, in this version if the key does not exists, returns -1
    # but in a network, we can run a query to find the key from Main storage or database (commented lines)
    # to be more efficient, we can only check if the questioned key is expired or not
    def get(self, key):
        try: 
            entry=self.cache_dict[key]
            self.cache_dict.pop(key)
            if time()-entry.put_time>self.ttu:
                print('key={} was not found in cache'.format(key))
                return -1
            self.cache_dict[key]= entry
            value=entry.value
            print('value of key={} is {}'.format(key,value))
        except KeyError:
            #value=self.query(key)
            #self.put(key, value)
            value=-1
            print('key={} was not found in cache'.format(key))
        
        return value

    
    # put method, first, updates the cache to remove expired entries
    # then creates an Entry and put it in the cache using LRU method
    def put(self, key, value):
        self.update()
        try: 
            self.cache_dict.pop(key)
        except KeyError:
            if len(self.cache_dict) >= self.capacity:
                self.cache_dict.popitem(last=False)
        self.cache_dict[key]=Entry(value)
        print('key={}, value={}  added successfully'.format(key,value))
        
    
    # update method checks for expired entries and removes them
    def update(self):
        for key in list(self.cache_dict.keys()):
            if time()-self.cache_dict[key].put_time>self.ttu:
                self.cache_dict.pop(key)
            else:
                break
        
    # query method is a reference to search the main storage or database 
    # (the search method is defined in the main storage class, not included in this code)  
    # def query(key):
    #    value=Main.search(key)

    
if __name__ == '__main__':
    lru=TLRUCache(3)
    lru.put(1,1)
    lru.put(2,2)
    lru.get(1)
    lru.put(3,3)
    lru.put(4,4)
    lru.get(2)
    lru.put(3,3)
    lru.get(3)
    t.sleep(20)
    lru.get(3)
    

