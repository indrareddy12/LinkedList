# Node class represents a
# node in a linked list
class Node:
    # Constructor with both data and next node as parameters
    def __init__(self, data1, next1=None):
        # Data stored in the node
        self.data = data1
        # Pointer to the next node in the list
        self.next = next1

# Solution class with detectLoop function
class Solution:
    # function to detect loop in linked list
    def detectLoop(self, head):
        # Initialize a pointer 'temp'
        # at the head of the linked list
        temp = head

        # Create a set to keep track of
        # encountered nodes
        nodeMap = {}

        # Step 2: Traverse the linked list
        while temp is not None:
            # If the node is already in the
            # map, there is a loop
            if temp in nodeMap:
                return True
            # Store the current node
            # in the map
            nodeMap[temp] = 1

            # Move to the next node
            temp = temp.next

        # Step 3: If the list is successfully traversed 
        # without a loop, return false
        return False

# Driver code
if __name__ == "__main__":
    # Create a sample linked list
    # with a loop for testing
    head = Node(1)
    second = Node(2)
    third = Node(3)
    fourth = Node(4)
    fifth = Node(5)

    head.next = second
    second.next = third
    third.next = fourth
    fourth.next = fifth
    # Create a loop
    fifth.next = third

    sol = Solution()

    # Check if there is a loop 
    # in the linked list
    if sol.detectLoop(head):
        print("Loop detected in the linked list.")
    else:
        print("No loop detected in the linked list.")
