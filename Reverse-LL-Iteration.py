# Definition for singly-linked list node
class ListNode:
    def __init__(self, val=0):
        self.val = val
        self.next = None

class Solution:
    # Function to reverse a linked list iteratively
    def reverseList(self, head):
        # Initialize previous pointer to None
        prev = None

        # Start from the head of the list
        temp = head

        # Traverse the list
        while temp:
            # Save the next node
            front = temp.next

            # Reverse the current node's pointer
            temp.next = prev

            # Move prev to current node
            prev = temp

            # Move to the next node
            temp = front

        # Return new head (last node becomes first)
        return prev

# Driver code
def printList(head):
    while head:
        print(head.val, end=" ")
        head = head.next
    print()

# Creating a linked list: 1 -> 2 -> 3 -> 4 -> 5
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)

sol = Solution()
# Reversing the list
newHead = sol.reverseList(head)

# Printing the reversed list
printList(newHead)
