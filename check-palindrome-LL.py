# Node class represents a node in a linked list
class Node:
    def __init__(self, data, next_node=None):
        self.data = data       # Data stored in the node
        self.next = next_node  # Pointer to the next node in the list

# Function to reverse a linked list using the recursive approach
def reverse_linked_list(head):
    if head is None or head.next is None:
        return head  # No change is needed; return the current head

    # Recursive step: Reverse the remaining part of the list and get the new head
    new_head = reverse_linked_list(head.next)

    # Store the next node in 'front' to reverse the link
    front = head.next

    # Update the 'next' pointer of 'front' to point to the current head
    front.next = head

    # Set the 'next' pointer of the current head to None to break the original link
    head.next = None

    return new_head  # Return the new head obtained from the recursion

# Function to check if the linked list is a palindrome
def is_palindrome(head):
    if head is None or head.next is None:
        return True  # It's a palindrome by definition

    slow = head
    fast = head

    # Traverse the linked list to find the middle using slow and fast pointers
    while fast.next is not None and fast.next.next is not None:
        slow = slow.next      # Move slow pointer one step at a time
        fast = fast.next.next # Move fast pointer two steps at a time

    # Reverse the second half of the linked list starting from the middle
    new_head = reverse_linked_list(slow.next)

    first = head
    second = new_head

    # Compare data values of nodes from both halves
    while second is not None:
        if first.data != second.data:
            reverse_linked_list(new_head)  # Reverse the second half back to its original state
            return False

        first = first.next  # Move the first pointer
        second = second.next  # Move the second pointer

    # Reverse the second half back to its original state
    reverse_linked_list(new_head)

    return True  # The linked list is a palindrome

# Function to print the linked list
def print_linked_list(head):
    temp = head
    while temp:
        print(temp.data, end=" ")  # Print the current node's data
        temp = temp.next           # Move to the next node
    print()

# Driver code
if __name__ == "__main__":
    # Create a linked list with values 1, 5, 2, 5, and 1 (15251, a palindrome)
    head = Node(1)
    head.next = Node(5)
    head.next.next = Node(2)
    head.next.next.next = Node(5)
    head.next.next.next.next = Node(1)

    # Print the original linked list
    print("Original Linked List: ", end="")
    print_linked_list(head)

    # Check if the linked list is a palindrome
    if is_palindrome(head):
        print("The linked list is a palindrome.")
    else:
        print("The linked list is not a palindrome.")
