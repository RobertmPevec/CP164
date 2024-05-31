"""
------------------------------------------------------------------------
Lab 3, Task 5
------------------------------------------------------------------------
Author: Robert Pevec
ID:     169081145
Email:  peve1145@mylaurier.ca
__updated__ = '2024-05-24'
------------------------------------------------------------------------
"""
from Priority_Queue_array import Priority_Queue
pq = Priority_Queue()
pq.insert(10)
pq.insert(5)
pq.insert(20)
print(pq.remove())
print(pq._values)
