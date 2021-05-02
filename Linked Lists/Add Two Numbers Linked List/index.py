# Definition for singly-linked list.
class ListNode:
    def __init__(self, value):
        self.value = value
        self.next = None


# O(N) time | O(N) space
def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
    # init condition
    tot = l1.value + l2.value
    carry = int(tot / 10)
    l3 = ListNode(tot % 10)
    p1 = l1.next
    p2 = l2.next
    p3 = l3
    while p1 is not None or p2 is not None:
        tot = carry + (p1.value if p1 else 0) + (p2.value if p2 else 0)
        carry = int(tot/10)
        p3.next = ListNode(tot % 10)
        p3 = p3.next
        p1 = p1.next if p1 else None
        p2 = p2.next if p2 else None

    if(carry > 0):
        p3.next = ListNode(carry)

    return l3


# O(N) space | O(N) time
def sumOfLinkedLists(linkedListOne, linkedListTwo):
    pointer = ListNode(0)
    currentNode = pointer
    carry = 0

    nodeOne = linkedListOne
    nodeTwo = linkedListTwo

    while nodeOne is not None or nodeTwo is not None or carry != 0:
        valueOne = nodeOne.value if nodeOne is not None else 0
        valueTwo = nodeTwo.value if nodeTwo is not None else 0
        sumofValues = valueOne + valueTwo + carry

        newValue = sumofValues % 10
        newNode = ListNode(newValue)
        currentNode.next = newNode
        currentNode = newNode

        carry = sumofValues // 10
        nodeOne = nodeOne.next if nodeOne is not None else None
        nodeTwo = nodeTwo.next if nodeTwo is not None else None

    return pointer.next
