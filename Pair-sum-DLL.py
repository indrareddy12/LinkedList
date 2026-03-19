class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

def findTail(head):
    temp = head
    while temp.next is not None:
        temp = temp.next
    return temp

def findPairsWithSum(head, target):
    result = []

    left = head
    right = findTail(head)

    while left.data < right.data:  # two pointers haven't crossed
        s = left.data + right.data

        if s == target:
            result.append((left.data, right.data))
            left = left.next
            right = right.prev
        elif s < target:
            left = left.next   # need bigger sum → move left forward
        else:
            right = right.prev  # need smaller sum → move right backward

    return result


# ---- Test ----
def buildDLL(values):
    head = Node(values[0])
    curr = head
    for v in values[1:]:
        new = Node(v)
        new.prev = curr
        curr.next = new
        curr = new
    return head

head = buildDLL([1, 2, 3, 4, 9])
print(findPairsWithSum(head, 5))  # [(1, 4), (2, 3)]
```

---

### How it works (Two Pointer):
```
DLL: 1 ↔ 2 ↔ 3 ↔ 4 ↔ 9   target = 5

left=1, right=9 → 1+9=10 > 5 → move right ←
left=1, right=4 → 1+4=5  ✅ → pair found, move both
left=2, right=3 → 2+3=5  ✅ → pair found, move both
left=3, right=2 → left >= right → STOP
