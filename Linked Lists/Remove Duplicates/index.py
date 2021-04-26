class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


# O(n) time | O(1) space
def removeDuplicatesFromLinkedList(linkedList):
    currentNode = linkedList
    while currentNode is not None:
        nextDistinctNode = currentNode.next
        while nextDistinctNode is not None and nextDistinctNode.value == currentNode.value:
            nextDistinctNode = nextDistinctNode.next

        currentNode.next = nextDistinctNode
        currentNode = nextDistinctNode

    return linkedList


# O(n) time | O(1) space
def removeDuplicatesFromLinkedListAlt(linkedList):
    nextNode = linkedList.next
    currentNode = linkedList
    while nextNode is not None:
        if currentNode.value != nextNode.value:
            currentNode.next = nextNode
            currentNode = currentNode.next
        else:
            nextNode = nextNode.next
    currentNode.next = None
    return linkedList
