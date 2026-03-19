# Node class represents a node in the linked list
class Node:
    # Constructor with data and next pointer
    def __init__(self, data1, next1=None):
        self.data = data1
        self.next = next1

# Solution class contains method to delete middle node
class Solution:
    # Function to delete the middle node
    def deleteMiddle(self, head):
        # If list has only one node, delete it
        if head is None or head.next is None:
            return None

        # Initialize slow pointer to head
        slow = head

        # Initialize fast pointer two steps ahead
        fast = head.next.next

        # Traverse until fast reaches end
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next

        # Bypass the middle node
        slow.next = slow.next.next

        # Return head of updated list
        return head

# Function to print linked list
def printLL(head):
    temp = head
    while temp is not None:
        print(temp.data, end=" ")
        temp = temp.next
    print()

# Driver function
if __name__ == "__main__":
    # Creating linked list 1->2->3->4->5
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)

    # Printing original list
    print("Original Linked List:", end=" ")
    printLL(head)

    # Deleting middle node
    obj = Solution()
    head = obj.deleteMiddle(head)

    # Printing updated list
    print("Updated Linked List:", end=" ")
    printLL(head)
