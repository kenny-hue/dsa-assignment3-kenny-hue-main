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
        # Initialize head and tail pointers
        head = self.head
        tail = self.head

        # Move head pointer forward to skip leading spaces
        while head is not None and head.val == ' ':
            head = head.next

        # If the list is empty or contains only spaces, set head and tail to None
        if head is None:
            self.head = None
            self.tail = None
            return

        # Move tail pointer backward to skip trailing spaces
        while tail.next is not None:
            if tail.next.val != ' ':
                tail = tail.next
            else:
                tail = tail.next
                break

        while tail.next is not None:
            if tail.next.val != ' ':
                tail = tail.next
            else:
                tail.next = None
                break

        # Update head and tail of the linked list
        self.head = head
        self.tail = tail




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
result = ll_string.find_nth(4, 'a')

# Print the result
print("Index of the 2nd occurrence of 'a':", result)
