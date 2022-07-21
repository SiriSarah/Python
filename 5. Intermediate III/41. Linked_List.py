# Data Structures - Singly Linked List

class Node:
    def __init__(self, value, next=None):
        # None is a valid value in Python
        self.value = value
        self.next = next

# Constructing a List by giving the nodes
linked_list = Node("a", Node("b", Node("c", Node("d"))))

print(linked_list.value)
print(linked_list.next.value)
print(linked_list.next.next.value)
print(linked_list.next.next.next.value)
# To do: 
# 1) Replace the above print statements with the iter()
# 2) Try to print the next value after this and check what happens