"""
------------------------------------------------------------------------
Data Structures, utilities
------------------------------------------------------------------------
Author: Robert Pevec
ID:     169081145
Email:  peve1145@mylaurier.ca
__updated__ = '2024-05-17'
------------------------------------------------------------------------
"""
from Stack_array import Stack
from Queue_array import Queue
from Priority_Queue_array import Priority_Queue
from List_array import List


def array_to_stack(stack, source):
    """
    -------------------------------------------------------
    Pushes contents of source onto stack. At finish, source is empty.
    Last value in source is at bottom of stack,
    first value in source is on top of stack.
    Use: array_to_stack(stack, source)
    -------------------------------------------------------
    Parameters:
        stack - a Stack object (Stack)
        source - a Python list (list)
    Returns:
        None
    -------------------------------------------------------
    """
    for _ in range(len(source)):
        value = source[-1]
        stack.push(value)
        source.pop()
    return None


def stack_to_array(stack, target):
    """
    -------------------------------------------------------
    Pops contents of stack into target. At finish, stack is empty.
    Top value of stack is at end of target,
    bottom value of stack is at beginning of target.
    Use: stack_to_array(stack, target)
    -------------------------------------------------------
    Parameters:
        stack - a Stack object (Stack)
        target - a Python list (list)
    Returns:
        None
    -------------------------------------------------------
    """
    while len(stack) > 0:
        target.push(0, stack.pop())
    return None


def stack_test(source):
    """
    -------------------------------------------------------
    Tests the methods of Stack for empty and
    non-empty stacks using the data in source:
    is_empty, push, pop, peek
    (Testing pop and peek while empty throws exceptions)
    Use: stack_test(source)
    -------------------------------------------------------
    Parameters:
        source - list of data (list of ?)
    Returns:
        None
    -------------------------------------------------------
    """
    stack = Stack()
    stack.is_empty()
    for item in source:
        stack.push(item)
    stack.peek()
    stack.pop()
    _values = []
    target = []
    stack_to_array(_values, target)


def array_to_queue(queue, source):
    """
    -------------------------------------------------------
    Inserts contents of source into queue. At finish, source is empty.
    Last value in source is at rear of queue,
    first value in source is at front of queue.
    Use: array_to_queue(queue, source)
    -------------------------------------------------------
    Parameters:
        queue - a Queue object (Queue)
        source - a Python list (list)
    Returns:
        None
    -------------------------------------------------------
    """
    while source:
        value = source.pop(0)
        queue.insert(value)
    return


def queue_to_array(queue, target):
    """
    -------------------------------------------------------
    Removes contents of queue into target. At finish, queue is empty.
    Front value of queue is at front of target,
    rear value of queue is at end of target.
    Use: queue_to_array(queue, target)
    -------------------------------------------------------
    Parameters:
        queue - a Queue object (Queue)
        target - a Python list (list)
    Returns:
        None
    -------------------------------------------------------
    """
    while not queue.is_empty():
        value = queue.remove()
        target.append(value)
    return


def queue_test(a):
    """
    -------------------------------------------------------
    Tests queue implementation.
  Tests the methods of Queue are tested for both empty and
  non-empty queues using the data in a:
        is_empty, insert, remove, peek, len
    Use: queue_test(a)
    -------------------------------------------------------
    Parameters:
        a - list of data (list of ?)
    Returns:
        None
    -------------------------------------------------------
    """
    q = Queue()
    print(q.is_empty())
    for item in a:
        q.insert(item)
    print(q)
    print(len(q))
    if not q.is_empty():
        print(q.peek())
    while not q.is_empty():
        print(q.remove())
    return


def array_to_pq(pq, source):
    """
    -------------------------------------------------------
    Inserts contents of source into pq. At finish, source is empty.
    Last value in source is at rear of pq,
    first value in source is at front of pq.
    Use: array_to_pq(pq, source)
    -------------------------------------------------------
    Parameters:
        pq - a Priority_Queue object (Priority_Queue)
        source - a Python list (list)
    Returns:
        None
    -------------------------------------------------------
    """
    while len(source) > 0:
        value = source.pop(0)
        pq.insert(value)
    return None


def pq_to_array(pq, target):
    """
    -------------------------------------------------------
    Removes contents of pq into target. At finish, pq is empty.
    Highest priority value in pq is at front of target,
    lowest priority value in pq is at end of target.
    Use: pq_to_array(pq, target)
    -------------------------------------------------------
    Parameters:
        pq - a Priority_Queue object (Priority_Queue)
        target - a Python list (list)
    Returns:
        None
    -------------------------------------------------------
    """
    while not pq.is_empty():
        value = pq.remove()
        target.append(value)
    return None


def priority_queue_test(a):
    """
    -------------------------------------------------------
    Tests priority queue implementation.
    Test the methods of Priority_Queue are tested for both empty and
    non-empty priority queues using the data in a:
        is_empty, insert, remove, peek
    Use: priority_queue_test(a)
    -------------------------------------------------------
    Parameters:
        a - list of data (list of ?)
    Returns:
        None
    -------------------------------------------------------
    """
    pq = Priority_Queue()
    print(pq.is_empty())
    for value in a:
        pq.insert(value)
        print(list(pq))
    print(pq.is_empty())
    print(pq.peek())
    while not pq.is_empty():
        print(pq.remove())
        print(list(pq))
    print(pq.is_empty())
    return None


def array_to_list(llist, source):
    """
    -------------------------------------------------------
    Appends contests of source to llist. At finish, source is empty.
    Last element in source is at rear of llist,
    first element in source is at front of llist.
    Use: array_to_list(llist, source)
    -------------------------------------------------------
    Parameters:
        llist - a List object (List)
        source - a Python list (list)
    Returns:
        None
    -------------------------------------------------------
    """
    while source:
        value = source.pop(0)
        llist.append(value)
    return None


def list_to_array(llist, target):
    """
    -------------------------------------------------------
    Removes contents of llist into target. At finish, llist is empty.
    Front element of llist is at front of target,
    rear element of llist is at rear of target.
    Use: list_to_array(llist, target)
    -------------------------------------------------------
    Parameters:
        llist - a List object (List)
        target - a Python list (list)
    Returns:
        None
    -------------------------------------------------------
    """
    while llist:
        value = llist.pop(0)
        target.append(value)
    return None

def list_test(source):
    """
    -------------------------------------------------------
    Tests List implementation.
    The methods of List are tested for both empty and
    non-empty lists using the data in source
    Use: list_test(source)
    -------------------------------------------------------
    Parameters:
        source - list of data (list of ?)
    Returns:
        None
    -------------------------------------------------------
    """
    lst = List()
    print("Testing on empty list:")
    print("Is empty:", lst.is_empty())
    print("Length:", len(lst))
    for item in source:
        lst.append(item)
    print("\nTesting on populated list:")
    print("List contents:", lst._values)
    print("Is empty:", lst.is_empty())
    print("Length:", len(lst))
    if len(lst) > 0:
        print(f"Element at index 0 (before): {lst[0]}")
        lst[0] = "TestItem"
        print(f"Element at index 0 (after setting to 'TestItem'): {lst[0]}")
    print("List contains 'TestItem':", "TestItem" in lst)  # Expected: True
    print("List contains 'NonExistent':", "NonExistent" in lst)  # Expected: False
    lst.insert(1, "InsertedItem")
    print("List after inserting 'InsertedItem' at index 1:", lst._values)
    removed_value = lst.remove("TestItem")
    print(f"Removed value: {removed_value}")
    print("List after removing 'TestItem':", lst._values)
    print(f"Find 'InsertedItem' in list:", lst.find("InsertedItem"))  # Expected: 'InsertedItem'
    print("Find 'NonExistent' in list:", lst.find("NonExistent"))  # Expected: None
    count_value = lst.count("InsertedItem")
    print(f"Count of 'InsertedItem' in list: {count_value}")
    index_value = lst.index("InsertedItem")
    print(f"Index of 'InsertedItem' in list: {index_value}")
    if len(lst) > 0:
        print("Minimum value in the list:", lst.min())
        print("Maximum value in the list:", lst.max())

    return None
