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

        # If the list is empty after trimming leading spaces, return
        if self.head is None:
            return

        # Traverse to the end of the list
        trav = self.head
        while trav.next is not None:
            trav = trav.next

        # Remove trailing spaces
        while trav.val == ' ':
            # Find the node before the trailing space node
            prev = self.head
            while prev.next != trav:
                prev = prev.next
            prev.next = None
            trav = prev

        # Remove internal spaces
        trav = self.head
        while trav is not None and trav.next is not None:
            if trav.next.val == ' ':
                trav.next = trav.next.next
            else:
                trav = trav.next



    def find_nth(self, n, c):
        if n < 1:
            return -1

        count = 0
        index = 0
        trav = self.head

        while trav is not None:
            if trav.val == c:
                count += 1
                if count == n:
                    return index
            index += 1
            trav = trav.next

        return -1






# Given LLString
ll_string = LLString('banana')

# Call find_nth() method for the 2nd occurrence of 'e'
result = ll_string.find_nth(2, 'a')

# Print the result
print("Index of the 2nd occurrence of 'a':", result)
