# Data Structures - Doubly Linked List

class Node:
    def __init__(self, value, previous=None, next=None):
        # None is a valid value in Python
        self.value = value
        self.previous = previous
        self.next = next

# Class for doubly Linked List
class doublyLinkedList:
    
    def __init__(self):
        self.first_node = None
    
    # Insert Element 
    def insert(self, data):
        if self.first_node is None:
            # If the list is empty, add the node and return
            self.first_node = Node(data)
            return
        
        temp_node = self.first_node
        # Iterate till the next reaches NULL, because we want to insert the new node at end
        while temp_node.next is not None:
            temp_node = temp_node.next
        
        new_node = Node(data)
        temp_node.next = new_node
        new_node.previous = temp_node

    # Delete the elements
    def delete_dll(self):
        if self.first_node is None:
            print("The Linked list is empty, no element to delete")
            return
        while self.first_node is not None:    
            self.first_node = self.first_node.next
            self.start_prev = None

    # Traversing and Displaying each element of the list
    def display_dll(self):
        if self.first_node is None:
            print("list is empty")
            return
        else:
            temp_node = self.first_node
            while temp_node is not None:
                print("Element is: ", temp_node.value)
                temp_node = temp_node.next
        print("\n")

# Create a new Doubly Linked List
dll = doublyLinkedList()

# Insert the element
dll.insert("a")
dll.insert("b")
dll.insert("c")
dll.insert('d') # Both single and double quotes can be used to define string.

# Display Data
dll.display_dll()

# Delete elements
dll.delete_dll()

# Display Data
dll.display_dll()

# To do: 
# 1) Update the program so you can specify an element to delete
# 2) Try to create the same structure and similar functions for Singly Linked List