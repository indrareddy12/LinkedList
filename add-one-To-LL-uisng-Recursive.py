# Node class representing a single digit in the linked list
class Node:
    def __init__(self, value):
        self.data = value
        self.next = None

# LinkedList class having only append and print logic
class LinkedList:
    # Function to insert digit at the end
    def append(self, head, value):
        new_node = Node(value)
        if not head:
            return new_node
        current = head
        while current.next:
            current = current.next
        current.next = new_node
        return head

    # Function to print the list
    def printList(self, head):
        current = head
        while current:
            print(current.data, end='')
            current = current.next
        print()

# Solution class having the addOne logic
class Solution:
    # Recursive function to add one from least significant digit (rightmost node)
    def addOneUtil(self, node):
        # Base case: when reaching beyond last node, return carry = 1
        if not node:
            return 1
        # Recurse to the end
        carry = self.addOneUtil(node.next)  
        total = node.data + carry
        node.data = total % 10
        # Return new carry
        return total // 10  

    # Function to add one to the number represented by the linked list
    def addOne(self, head):
        # Perform recursive addition
        carry = self.addOneUtil(head)

        # If carry remains after processing the head, create a new head node
        if carry:
            new_head = Node(carry)
            new_head.next = head
            head = new_head
        return head

# Main function
if __name__ == "__main__":
    head = None
    ll = LinkedList()
    sol = Solution()

    # Example: Number 129 (1 -> 2 -> 9)
    head = ll.append(head, 1)
    head = ll.append(head, 2)
    head = ll.append(head, 9)

    print("Original Number: ", end='')
    ll.printList(head)

    head = sol.addOne(head)

    print("After Adding One: ", end='')
    ll.printList(head)
