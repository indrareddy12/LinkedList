# Definition for singly-linked list node
class ListNode:
    def __init__(self, val=0, next=None):
        # Value stored in the node
        self.val = val    
        # Pointer to the next node
        self.next = next  

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        # Create a dummy node to simplify handling the result list
        dummy = ListNode()
        # Pointer to the current node in the result list
        temp = dummy  
        # Carry from the previous digit addition
        carry = 0     

        # Loop until both lists are fully traversed and no carry remains
        while (l1 is not None or l2 is not None) or carry:
            sum_val = 0  # Holds the sum of current digits and carry

            # Add l1's value to sum if l1 exists
            if l1 is not None:
                sum_val += l1.val
                l1 = l1.next

            # Add l2's value to sum if l2 exists
            if l2 is not None:
                sum_val += l2.val
                l2 = l2.next

            # Add any carry from the previous step
            sum_val += carry

            # Update carry for the next addition
            carry = sum_val // 10

            # Create a new node with the digit value (sum % 10)
            node = ListNode(sum_val % 10)
            # Append the new node to the result list
            temp.next = node  
            # Move temp forward
            temp = temp.next  

        # Return the result list, skipping the dummy node
        return dummy.next
def create_list(arr):
    head = ListNode(arr[0])
    temp = head
    for i in arr[1:]:
        temp.next = ListNode(i)
        temp = temp.next
    return head

def print_list(head):
    while head:
        print(head.val, end=" -> " if head.next else "\n")
        head = head.next

if __name__ == "__main__":
    num1 = [2, 4, 3]  # represents 342
    num2 = [5, 6, 4]  # represents 465
    l1 = create_list(num1)
    l2 = create_list(num2)

    sol = Solution()
    result = sol.addTwoNumbers(l1, l2)
    print_list(result)  # Output: 7 -> 0 -> 8
