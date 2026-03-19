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
    # Function to return the length of loop using hashing
    def lengthOfLoop(self, head):
        # Dictionary to store visited nodes and their timer values
        visitedNodes = {}

        # Pointer to traverse the linked list
        temp = head

        # Timer to track visited nodes
        timer = 0

        # Traverse the linked list till temp reaches None
        while temp is not None:
            # If revisiting a node, return the difference of timer values
            if temp in visitedNodes:
                # Calculate the length of the loop
                loopLength = timer - visitedNodes[temp]

                # Return the length of the loop
                return loopLength

            # Store the current node and its timer value
            visitedNodes[temp] = timer

            # Move to the next node
            temp = temp.next

            # Increment the timer
            timer += 1

        # If traversal is completed and we reach the end of the list
        # means there is no loop
        return 0


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
