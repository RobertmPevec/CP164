"""
------------------------------------------------------------------------
Lab 3, Task 6
------------------------------------------------------------------------
Author: Robert Pevec
ID:     169081145
Email:  peve1145@mylaurier.ca
__updated__ = '2024-05-24'
------------------------------------------------------------------------
"""
from Priority_Queue_array import Priority_Queue
from utilities import array_to_pq, pq_to_array, priority_queue_test
pq = Priority_Queue()
array_to_pq(pq, [10, 5, 20])
print(pq._values)
target = []
pq_to_array(pq, target)
print(target)
priority_queue_test([10, 5, 20])