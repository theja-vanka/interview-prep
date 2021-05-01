class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return f"Value : {self.value}, Next: {self.next}"


# O(n) time | O(1) space
def removeKthNodeFromEnd(head, k):
    current = head
    counter = 0
    while counter < k+1 and current is not None:
        counter += 1
        current = current.next
    if counter <= k:
        head.value = head.next.value
    while current is not None:
        head = head.next
        current = current.next
    head.next = head.next.next
