"""
------------------------------------------------------------------------
Lab 3, Task 3
------------------------------------------------------------------------
Author: Robert Pevec
ID:     169081145
Email:  peve1145@mylaurier.ca
__updated__ = '2024-05-24'
------------------------------------------------------------------------
"""
from Queue_array import Queue
from utilities import array_to_queue, queue_to_array, queue_test
queue = Queue()
array_to_queue(queue, [1, 2, 3])
print(queue._values)
target = []
queue_to_array(queue, target)
print(target)
queue_test([1, 2, 3])