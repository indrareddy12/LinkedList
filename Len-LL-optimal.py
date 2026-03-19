# Node class represents a node in a linked list
class Node:
    # Constructor with both data and next node
    def __init__(self, data1, next1=None):
        # Data stored in the node
        self.data = data1
        # Pointer to the next node
        self.next = next1


# Solution class containing the loop length function
class Solution:
    # Function to return the length of loop using Floyd's Algorithm
    def lengthOfLoop(self, head):
        # Initialize slow and fast pointers
        slow = head
        fast = head

        # Loop until fast and slow meet
        while fast is not None and fast.next is not None:
            # Move slow by one step
            slow = slow.next

            # Move fast by two steps
            fast = fast.next.next

            # If slow and fast meet, loop detected
            if slow == fast:
                # Count the length of the loop
                return self.countLoopLength(slow)

        # No loop found
        return 0

    # Function to count loop length
    def countLoopLength(self, meetingPoint):
        # Start from meeting point
        temp = meetingPoint
        length = 1

        # Move until we meet again
        while temp.next != meetingPoint:
            temp = temp.next
            length += 1
        return length


# Main driver code
if __name__ == "__main__":
    # Creating a sample linked list with a loop
    head = Node(1)
    second = Node(2)
    third = Node(3)
    fourth = Node(4)
    fifth = Node(5)

    # Linking the nodes
    head.next = second
    second.next = third
    third.next = fourth
    fourth.next = fifth

    # Creating a loop from fifth to second
    fifth.next = second

    # Creating a Solution object
    obj = Solution()

    # Getting the loop length
    loopLength = obj.lengthOfLoop(head)

    # Printing the result
    if loopLength > 0:
        print("Length of the loop:", loopLength)
    else:
        print("No loop found in the linked list.")
