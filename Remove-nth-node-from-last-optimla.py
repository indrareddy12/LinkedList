# Class representing a node in the linked list
class Node:
    def __init__(self, data1, next1=None):
        self.data = data1
        self.next = next1

# Class to hold the solution logic
class Solution:
    # Function to print the linked list
    def printLL(self, head):
        while head is not None:
            print(head.data, end=" ")
            head = head.next

    # Function to delete the Nth node from the end 
    # using the optimized two-pointer method
    def deleteNthNodeFromEnd(self, head, N):
        # Create a dummy node before head to handle edge cases
        dummy = Node(0, head)

        # Initialize slow and fast pointers at dummy
        slow = dummy
        fast = dummy

        # Move fast pointer N+1 steps ahead to create a gap
        for _ in range(N + 1):
            fast = fast.next

        # Move both pointers until fast reaches the end
        while fast is not None:
            slow = slow.next
            fast = fast.next

        # Slow is now at node before target → delete target node
        slow.next = slow.next.next

        # Return updated head
        return dummy.next

# Main driver code
if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5]
    N = 3

    # Create linked list manually
    head = Node(arr[0])
    head.next = Node(arr[1])
    head.next.next = Node(arr[2])
    head.next.next.next = Node(arr[3])
    head.next.next.next.next = Node(arr[4])

    # Create Solution object
    sol = Solution()

    # Delete the Nth node from the end
    head = sol.deleteNthNodeFromEnd(head, N)

    # Print the modified linked list
    sol.printLL(head)
