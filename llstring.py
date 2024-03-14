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
        trav = self.head

        while trav is not None:
            if c == trav.val:
                return no_index
            trav = trav.next
            no_index += 1
        return -1


    def to_upper_case(self):
        def recursive_to_upper(node):
            if node is None:
                return
            node.val = node.val.upper()
            recursive_to_upper(node.next)

        recursive_to_upper(self.head)

    def replace(self, old, new):
        def recursive_replace(node):
            if node is None:
                return
            if node.val == old:
                node.val = new
            recursive_replace(node.next)

        recursive_replace(self.head)

    def copy(self):
        new_list = LLString("")
        trav = self.head

        while trav is not None:
            new_list.append(trav.val)
            trav = trav.next

        return new_list

    def trim(self):
        # Trim leading spaces
        while self.head is not None and self.head.val == ' ':
            self.head = self.head.next

        # Trim trailing spaces
        if self.head is None:
            return
        
        prev = self.head
        trav = self.head.next
        while trav is not None:
            if trav.val == ' ' and trav.next is not None and trav.next.val == ' ':
                prev.next = trav.next
                trav = trav.next
            else:
                prev = trav
                trav = trav.next
                
        # Trim trailing spaces after removing internal spaces
        while prev is not None and prev.val == ' ':
            prev = prev.next
        if prev is not None:
            prev.next = None


    def find_nth(self, n, c):
        def recursive_find_nth(node, count):
            if node is None:
                return -1
            if node.val == c:
                if count == 0:
                    return 0
                return 1 + recursive_find_nth(node.next, count - 1)
            return recursive_find_nth(node.next, count)

        if n < 0:
            return -1
        return recursive_find_nth(self.head, n)
