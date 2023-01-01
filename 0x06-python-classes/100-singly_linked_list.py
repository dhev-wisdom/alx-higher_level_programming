#!/usr/bin/python3
"""Implementing Singly Linked List with Python3"""

class Node:
    """Node class; Model for the Linked List"""
    def __init__(self, data,next_node=None):
        self.__data = data
        self.__next_node = None

    @property
    def data(self):
        """Getter method to retrieve the data value"""
        return self.__data

    @data.setter
    def data(self, value):
        """Setter method to set data to value"""
        try:
            if isinstance(value, int):
                self.__data = value
            else:
                raise TypeError("data must be an integer")
        except TypeError as er:
            print(er)

    @property
    def next_node(self):
        """Getter method: Returns the value of next_node"""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """Setter method to set next_node to value"""
        try:
            if value is Node() or None:
                self.__next_node = value
            else:
                raise TypeError("next_node must be a Node object")
        except TypeError as err:
            print(err)

class SinglyLinkedList:
    """SinglyLinkedList"""
    def __init__(self):
        self.__head = None

    def __str__(self):
        """Print function"""
        ptr_str = ""
        node = self.__head

        while node is not None:
            ptr_str += str(node.data)
            node = node.__next_node

        return ptr_str

    def sorted_insert(self, value):
        """sorted insert"""
        node = self.__head
        if isinstance(value, int):
            if node is None or self.__head.__data >= value:
                self.__head = Node(value, self.__head)
            else:
                while node.__next_node is not None and node.__next_node.__data < value:
                    node = node.__next_node
                node.__next_node = Node(value, node.__next_node)


sll = SinglyLinkedList()
sll.sorted_insert(2)
sll.sorted_insert(5)
sll.sorted_insert(3)
sll.sorted_insert(10)
sll.sorted_insert(1)
sll.sorted_insert(-4)
sll.sorted_insert(-3)
sll.sorted_insert(4)
sll.sorted_insert(5)
sll.sorted_insert(12)
sll.sorted_insert(3)
print(sll)
