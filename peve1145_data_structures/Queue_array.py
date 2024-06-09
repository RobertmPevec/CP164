"""
-------------------------------------------------------
Array version of the Queue ADT.
-------------------------------------------------------
Author:  Robert Pevec
ID:      169081145
Email:   peve1145@mylaurier.ca
Section: CP164 C
__updated__ = "2024-05-24"
-------------------------------------------------------
"""
from copy import deepcopy


class Queue:

    def __init__(self):
        """
        -------------------------------------------------------
        Initializes an empty qu
        eue. Data is stored in a Python list.
        Use: queue = Queue()
        -------------------------------------------------------
        Returns:
            a new Queue object (Queue)
        -------------------------------------------------------
        """
        self._values = []

    def is_empty(self):
        """
        -------------------------------------------------------
        Determines if the queue is empty.
        Use: b = queue.is_empty()
        -------------------------------------------------------
        Returns:
            True if queue is empty, False otherwise.
        -------------------------------------------------------
        """
        return len(self._values) == 0

    def is_full(self):
        """
        -------------------------------------------------------
        Determines if the queue is full. (Given the expandable nature
        of the Python list _values, the queue is never full.)
        Use: b = queue.is_full()
        -------------------------------------------------------
        Returns:
            True if queue is full, False otherwise.
        -------------------------------------------------------
        """
        return False

    def __len__(self):
        """
        -------------------------------------------------------
        Returns the length of the queue.
        Use: n = len(queue)
        -------------------------------------------------------
        Returns:
            the number of values in queue.
        -------------------------------------------------------
        """
        return len(self._values)

    def insert(self, value):
        """
        -------------------------------------------------------
        Adds a copy of value to the rear of the queue.
        Use: queue.insert(value)
        -------------------------------------------------------
        Parameters:
            value - a data element (?)
        Returns:
            None
        -------------------------------------------------------
        """
        deep_copy_value = deepcopy(value)
        self._values.append(deep_copy_value)
        return

    def remove(self):
        """
        -------------------------------------------------------
        Removes and returns value from the queue.
        Use: value = queue.remove()
        -------------------------------------------------------
        Returns:
            value - the value at the front of the queue - the value is
            removed from queue (?)
        -------------------------------------------------------
        """
        assert len(self._values) > 0, "Cannot remove from an empty queue"
        value = self._values[0]
        self._values.pop(0)
        return value

    def peek(self):
        """
        -------------------------------------------------------
        Peeks at the front of queue.
        Use: value = queue.peek()
        -------------------------------------------------------
        Returns:
            value - a copy of the value at the front of queue -
            the value is not removed from queue (?)
        -------------------------------------------------------
        """
        assert len(self._values) > 0, "Cannot peek at an empty queue"
        value = deepcopy(self._values[0])
        return value

    def __iter__(self):
        """
        FOR TESTING ONLY
        -------------------------------------------------------
        Generates a Python iterator. Iterates through the queue
        from front to rear.
        Use: for value in queue:
        -------------------------------------------------------
        Returns:
            value - the next value in the queue (?)
        -------------------------------------------------------
        """
        for value in self._values:
            yield value

    def __eq__(self, target):
        """
        ----------------
        Determines whether two Queues are equal.
        Values in self and target are compared and if all values are equal
        and in the same order, returns True, otherwise returns False.
        Use: equals = source == target
        ---------------
        Parameters:
            target - a queue (Queue)
        Returns:
            equals - True if source contains the same values
                as target in the same order, otherwise False. (boolean)
        ---------------
        """
        equals = (self._count == target._count)

        i = 0
        while equals and i < self._count:
            self_index = (self._front + i) % self._capacity
            target_index = (target._front + i) % target._capacity
            if self._values[self_index] != target._values[target_index]:
                equals = False
            i += 1

        return equals

    def combine(self, source1, source2):
        """
        -------------------------------------------------------
        Combines two source queues into the current target queue.
        When finished, the contents of source1 and source2 are interlaced
        into target and source1 and source2 are empty.
        Order of source values is preserved.
        (iterative algorithm)
        Use: target.combine(source1, source2)
        -------------------------------------------------------
        Parameters:
            source1 - an array-based queue (Queue)
            source2 - an array-based queue (Queue)
        Returns:
            None
        -------------------------------------------------------
        """
        self._values = [None] * (source1._count + source2._count)
        self._count = 0
        self._front = 0
        self._rear = 0

        while source1._count > 0 or source2._count > 0:
            if source1._count > 0:
                self._values[self._rear] = source1._values[source1._front]
                self._rear = (self._rear + 1) % len(self._values)
                source1._front = (source1._front + 1) % source1._capacity
                source1._count -= 1
                self._count += 1
            if source2._count > 0:
                self._values[self._rear] = source2._values[source2._front]
                self._rear = (self._rear + 1) % len(self._values)
                source2._front = (source2._front + 1) % source2._capacity
                source2._count -= 1
                self._count += 1

        # Clear source1 and source2
        source1._values = [None] * source1._capacity
        source1._front = None
        source1._rear = 0
        source1._count = 0

        source2._values = [None] * source2._capacity
        source2._front = None
        source2._rear = 0
        source2._count = 0
