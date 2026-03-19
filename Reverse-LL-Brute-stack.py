# Definition for singly-linked list node
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    # Function to reverse a linked list using stack
    def reverseList(self, head):
        # Stack to store values of nodes
        stack = []

        # Temporary pointer to traverse the list
        temp = head

        # Traverse and push all node values to stack
        while temp:
            stack.append(temp.val)
            temp = temp.next

        # Reset temp back to head
        temp = head

        # Reassign values from stack in reverse order
        while temp:
            temp.val = stack.pop()
            temp = temp.next

        # Return the modified head
        return head

# Driver code
def printList(head):
    while head:
        print(head.val, end=" ")
        head = head.next

# Creating linked list 1 -> 2 -> 3 -> None
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)

sol = Solution()
head = sol.reverseList(head)
printList(head)
