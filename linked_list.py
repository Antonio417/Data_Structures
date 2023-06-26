# Chain like structure where each node points to another node
# Big O
# append to linked list is O(1)
# Pop Linked List is O(n)
# Prepend Linked List is O(1)
# Pop first Linked List is O(1)
# Insert, remove, lookup by index and lookup by value is O(n)
class LinkedList:
    def __init__(self,value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next
    
    def append(self,value):
        new_node = Node(value)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
            self.length += 1
        return True
    
    def pop(self):
        if self.length == 0:
            return None
        
        temp = self.head
        pre = self.head
        while(temp.next):
            pre = temp
            temp = temp.next
        self.tail = pre
        self.tail.next = None
        self.length -= 1
        if self.length == 0:
            self.head = None
            self.tail = None
        return temp


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

temp_linked_list = LinkedList(20)
# temp_linked_list.print_list()

# Appending Linked List
temp_linked_list.append(13)
temp_linked_list.print_list()

# Pop Linked List
temp_linked_list.pop()
print("---------------POP--------------------")
temp_linked_list.print_list()
temp_linked_list.pop()
print("---------------POP--------------------")
print(temp_linked_list.pop())

