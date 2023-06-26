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

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

my_linked_list = LinkedList(20)
print(my_linked_list)
