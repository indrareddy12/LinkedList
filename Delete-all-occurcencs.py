class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

def deleteAllOccurrences(head, k):
    temp = head

    while temp is not None:
        if temp.data == k:
            # If the node to delete is the head, update head
            if temp == head:
                head = temp.next

            nextNode = temp.next
            prevNode = temp.prev

            if nextNode is not None:
                nextNode.prev = prevNode
            if prevNode is not None:
                prevNode.next = nextNode

            temp = nextNode  # move to next node
        else:
            temp = temp.next

    return head
