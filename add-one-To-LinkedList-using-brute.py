# Node class representing a single digit in the linked list
class Node:
    def __init__(self, value):
        self.data = value
        self.next = None

# LinkedList class to manage node-level operations
class LinkedList:
    # function to insert digit at the end
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
    # function to reverse the linked list
    def reverseList(self, node):
        prev = None
        current = node

        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        return prev

    # Function to add one to the number represented by the linked list
    def addOne(self, head):
        # Reverse the list to make least significant digit accessible
        head = self.reverseList(head)

        current = head
        carry = 1  

        # Traverse the list and add carry
        while current and carry:
            sum_ = current.data + carry
            current.data = sum_ % 10
            carry = sum_ // 10

            # If there's no next node and we still have a carry, append a new node
            if not current.next and carry:
                current.next = Node(carry)
                carry = 0  

            current = current.next

        # Reverse the list back to restore original order
        head = self.reverseList(head)
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
