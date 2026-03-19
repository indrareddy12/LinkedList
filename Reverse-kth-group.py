# Definition for singly-linked list node
class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

class Solution:
    # Function to reverse nodes in k-sized groups
    def reverseKGroup(self, head, k):
        # Creating a dummy node
        dummy = ListNode(0)
        dummy.next = head

        # Pointer to the tail of the last reversed group
        groupPrev = dummy

        while True:
            # Get the k-th node in the group
            kth = self.getKthNode(groupPrev, k)
            if not kth:
                break

            # Store the next group’s start
            groupNext = kth.next

            # Reverse the current k nodes
            prev = groupNext
            curr = groupPrev.next

            for _ in range(k):
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp

            # Connect the reversed group to the previous part
            temp = groupPrev.next
            groupPrev.next = kth
            groupPrev = temp

        # Return new head
        return dummy.next

    # Helper function to find the k-th node from current
    def getKthNode(self, curr, k):
        while curr and k > 0:
            curr = curr.next
            k -= 1
        return curr

# Driver code
def printList(node):
    while node:
        print(node.val, end=" ")
        node = node.next

# Creating linked list: 1->2->3->4->5
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)

k = 2
sol = Solution()
result = sol.reverseKGroup(head, k)
printList(result)
