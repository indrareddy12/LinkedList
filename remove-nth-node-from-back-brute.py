# Class representing a node in the linked list
class Node:
    def __init__(self, data1, next1=None):
        self.data = data1
        self.next = next1

# Class to hold the solution logic
class Solution:
    # Function to print the linked list
    def printLL(self, head):
        while head:
            print(head.data, end=" ")
            head = head.next

    # Function to delete the Nth node from the end
    def deleteNthNodeFromEnd(self, head, N):
        # If list is empty
        if head is None:
            return None

        cnt = 0
        temp = head

        # Count total number of nodes
        while temp:
            cnt += 1
            temp = temp.next

        # If N equals total nodes → delete head
        if cnt == N:
            return head.next

        # Calculate position from start
        res = cnt - N
        temp = head

        # Traverse to the node before target
        while temp:
            res -= 1
            if res == 0:
                break
            temp = temp.next

        # Delete the node
        temp.next = temp.next.next

        return head


if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5]
    N = 3

    # Create linked list manually
    head = Node(arr[0])
    head.next = Node(arr[1])
    head.next.next = Node(arr[2])
    head.next.next.next = Node(arr[3])
    head.next.next.next.next = Node(arr[4])

    sol = Solution()
    head = sol.deleteNthNodeFromEnd(head, N)
    sol.printLL(head)
