# Node class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# Linked List class
class LinkedList:
    def __init__(self):
        self.head = None

    # Insert at end
    def append(self, data):
        new_node = Node(data)

        # If list is empty
        if self.head is None:
            self.head = new_node
            return

        # Traverse to last node
        temp = self.head
        while temp.next:
            temp = temp.next

        temp.next = new_node

    # Insert at beginning
    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    # Delete a node
    def delete(self, key):
        temp = self.head

        # If head itself holds the key
        if temp and temp.data == key:
            self.head = temp.next
            temp = None
            return

        prev = None

        # Search for the key
        while temp and temp.data != key:
            prev = temp
            temp = temp.next

        # Key not found
        if temp is None:
            return

        prev.next = temp.next
        temp = None

    # Display linked list
    def display(self):
        temp = self.head

        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next

        print("None")


# Driver code
ll = LinkedList()

ll.append(10)
ll.append(20)
ll.append(30)

ll.prepend(5)

ll.display()

ll.delete(20)

ll.display()
