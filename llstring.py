class LLString:
    class Node:
        def __init__(self, val, next):
            self.val = val
            self.next = next

    def __init__(self, s):
        self.head = None
        self.tail = None

        for char in s:
            self.append(char)

    def append(self, new_val):
        new_node = LLString.Node(new_val, None)

        if self.tail is not None:
            self.tail.next = new_node
        self.tail = new_node

        if self.head is None:
            self.head = new_node

    # recursive helper method for printing
    def __print(self, node):
        if node is None:
            print()
        else:
            print(node.val, end='')
            self.__print(node.next)

    def print(self):
        # just invoke the recursive helper method
        self.__print(self.head)

    def to_string(self):
        s = ''
        trav = self.head
        while trav is not None:
            s += trav.val
            trav = trav.next
        return s

    def find(self, c):
        no_index = 0

        for letter in self.split:
            if c == letter:
                return no_index
            no_index += 1
        return -1


    def to_upper_case(self):
        pass

    def replace(self, old, new):
        pass

    def copy(self):
        pass

    def trim(self):
        pass

    def find_nth(self, n, c):
        pass
