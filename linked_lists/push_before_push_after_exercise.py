# Python Script to Implement and Manipulate Linked List in Python

# Node class
class Node:
    # Constructor to initialize the node object
    def __init__(self, data):
        self.data = data  # Assign the data
        self.next = None  # Initialize the next node as null

# LinkedList class
class LinkedList:

    # Initialize the linked list with a head
    def __init__(self):
        self.head = None
    
    # Function to add a node to the beginning of the linked list
    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    # TODO: Add a method to insert a node after a specified node in the linked list.
    def push_after(self, new_data):
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = Node(new_data)
  
    # Function to print the linked list
    def print_list(self):
        current_node = self.head
        while(current_node):
            print(current_node.data, end="->")
            current_node = current_node.next

llist = LinkedList()

# Add nodes to the alien communication network
llist.push("Zog")
# TODO: Insert a new node "Zak" after "Zog" in the alien communication network.
llist.push_after("Zak")
# Print the Alien Communication Network
llist.print_list() 
