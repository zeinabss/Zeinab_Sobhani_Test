# Zeinab_Sobhani_Test

Question A: 
Your goal for this question is to write a program that accepts two lines (x1,x2) and (x3,x4) on the x-axis and returns whether they overlap. As an example, (1,5) and (2,6) overlaps but not (1,5) and (6,8).

Please find the solution in the Python (.py) or Jupyter (.ipynb) folders under the name "Overlap Check". The test cases is shown in the Jupyter Notebook file. 




Question B:

The goal of this question is to write a software library that accepts 2 version string as input and returns whether one is greater than, equal, or less than the other. As an example: “1.2” is greater than “1.1”. Please provide all test cases you could think of.

Please find the solution in the Python (.py) or Jupyter (.ipynb) folders under the name "Version Compare". The test cases is shown in the Jupyter Notebook file. 



Question C

At Ormuco, we want to optimize every bits of software we write. Your goal is to write a new library that can be integrated to the Ormuco stack. Dealing with network issues everyday, latency is our biggest problem. Thus, your challenge is to write a new Geo Distributed LRU (Least Recently Used) cache with time expiration. This library will be used extensively by many of our services so it needs to meet the following criteria:

 
1 - Simplicity. Integration needs to be dead simple.
2 - Resilient to network failures or crashes.
3 - Near real time replication of data across Geolocation. Writes need to be in real time.
4 - Data consistency across regions
5 - Locality of reference, data should almost always be available from the closest region
6 - Flexible Schema
7 - Cache can expire
    
Please find the solution in the Python (.py) or Jupyter (.ipynb) folders under the name "TLRUCache". The test cases is shown in the Jupyter Notebook file. 
In this solution, LRU method was used to remove the key values when the capacity is full. The LRU has an expiry time for all the keys, from the time they are added to the cache. 
The distributed system is connected to the main source. In case the key does not exist in the cache, we run a query on the main source, to find the value. Then add the value to the cache for future use. A search method is defined in the main database, which is not included in this code. Therefore the parts related to the main source are commented out.
Instead, when the key does not exist in the cache, the "get" method returns -1. 
