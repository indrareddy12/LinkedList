# Definition for singly-linked list
class ListNode:
    def __init__(self, val=0):
        self.val = val
        self.next = None

class Solution:
    # Recursive function to reverse the linked list
    def reverseList(self, head):
        # Base case: empty list or single node
        if head is None or head.next is None:
            return head

        # Recursively reverse the rest of the list
        newHead = self.reverseList(head.next)

        # Store next node
        front = head.next

        # Make next node point back to current
        front.next = head

        # Break current forward link
        head.next = None

        # Return new head
        return newHead

# Driver code
if __name__ == "__main__":
    # Create linked list: 1 -> 2 -> 3 -> 4 -> 5
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)

    sol = Solution()
    reversed_head = sol.reverseList(head)

    # Print reversed list
    while reversed_head:
        print(reversed_head.val, end=" ")
        reversed_head = reversed_head.next
