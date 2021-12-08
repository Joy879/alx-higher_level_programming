#!/usr/bin/python3
class Node:
    """Creates class named Node
    """

    def __init__(self, data, next_node=None):
        """initializes instance
        Args:
            data: integer
            next_node: next node address
        """

        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Decorates getter function to access private instance attribute
        Return:
            return self.__data value
        """

        return self.__data

    @data.setter
    def data(self, value):
        """Decorates setter function to set private instance attribute value
        Raises:
            TypeError: data must be an integer
        """

        if not isinstance(value, int):
            raise TypeError('data must be an integer')
        self.__data = value

    @property
    def next_node(self):
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """Sets private instance attribute value
        """

        if value is not None and type(value) != Node:
            raise TypeError('next_node must be a Node object')
        self.__next_node = value


class SinglyLinkedList:
    """Creates class
    """

    def __init__(self):
        self.head = None

    def __str__(self):
        """Return string to print function
        """

        return self.print_list()

    def sorted_insert(self, value):
        """Insert node function
        Arg:
            value: integer
        """

        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            return
        if value <= self.head.data:
            new_node.next_node = self.head
            self.head = new_node
            return

        current = self.head
        while current.next_node is not None and value > current.next_node.data:
            current = current.next_node
        new_node.next_node = current.next_node
        current.next_node = new_node

    """
    def insert_head(self, value):
        new_node = Node(value)
        if self.head is not None:
            new_node.next_node = self.head
        self.head = new_node
    """

    def print_list(self):
        """makes string for print function
        Return:
            return string
        """

        string = ''
        current = self.head
        while current.next_node is not None:
            string += (str(current.data) + '\n')
            current = current.next_node
        string += str(current.data)
        return string
