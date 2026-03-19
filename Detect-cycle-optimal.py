# Node class represents a node in a linked list
class Node:
    def __init__(self, data1, next1=None):
        self.data = data1
        self.next = next1

# Solution class with detectLoop function
class Solution:
    def detectLoop(self, head):
        # Initialize slow and fast pointers at head
        slow = head
        fast = head

        # Traverse the linked list
        while fast is not None and fast.next is not None:
            slow = slow.next          # moves 1 step
            fast = fast.next.next     # moves 2 steps

            # If slow and fast meet, loop exists
            if slow == fast:
                return True

        # If fast reaches None, no loop exists
        return False

# Driver code
if __name__ == "__main__":
    # Create a sample linked list with a loop for testing
    head = Node(1)
    second = Node(2)
    third = Node(3)
    fourth = Node(4)
    fifth = Node(5)

    head.next = second
    second.next = third
    third.next = fourth
    fourth.next = fifth

    # Create a loop (fifth -> third)
    fifth.next = third

    sol = Solution()

    if sol.detectLoop(head):
        print("Loop detected in the linked list.")
    else:
        print("No loop detected in the linked list.")
```

**Output:**
```
Loop detected in the linked list.
