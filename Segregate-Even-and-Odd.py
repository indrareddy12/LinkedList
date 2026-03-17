# Node definition for singly-linked list
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Solution:

    # Function to segregate even and odd nodes in a linked list
    def segregateEvenOdd(self, head):

        # Edge case: If list is empty or has only one node
        if head is None or head.next is None:
            return head

        # Create pointers for the heads and tails of even and odd lists
        evenHead = evenTail = None
        oddHead = oddTail = None

        # Pointer to traverse the list
        current = head

        # Traverse the linked list
        while current:

            # If the current node has even value
            if current.data % 2 == 0:
                if not evenHead:
                    evenHead = evenTail = current
                else:
                    evenTail.next = current
                    evenTail = current

            else:
                # If the current node has odd value
                if not oddHead:
                    oddHead = oddTail = current
                else:
                    oddTail.next = current
                    oddTail = current

            # Move to next node
            current = current.next

        # If no even nodes found, return odd list
        if not evenHead:
            return oddHead

        # If no odd nodes found, return even list
        if not oddHead:
            return evenHead

        # Combine even and odd lists
        evenTail.next = oddHead

        # Set end of list to null
        oddTail.next = None

        return evenHead

# Driver code
def printList(head):
    while head:
        print(head.data, end=" ")
        head = head.next

head = Node(17)
head.next = Node(15)
head.next.next = Node(8)
head.next.next.next = Node(12)
head.next.next.next.next = Node(10)
head.next.next.next.next.next = Node(5)
head.next.next.next.next.next.next = Node(4)

sol = Solution()
newHead = sol.segregateEvenOdd(head)
printList(newHead)
