# Binary Heap by Elijah Owusu Boahen
# 13th April, 2022

# O(1) T, O(N) S
class BH:
    def __init__(self, size) -> None:
        self.List = (size + 1) * [None]  # fix size list
        self.heapSize = 0
        self.maxSize = size + 1


# Traversal
# O(N)T, O(1)S
def levelorder(rootNode):
    try:
        for i in range(1, rootNode.heapSize + 1):
            print(rootNode.List[i])

    except (ValueError, RuntimeError, TypeError, NameError, SyntaxError) as err:
        print(f"Oops!... traversing failed. List is empty")


# O(log N)T, S
def heapifyInsert(rootNode, index, heapType):
    parentIndex = int(index / 2)
    if index <= 1:
        return
    if heapType == "Min":
        if rootNode.List[index] < rootNode.List[parentIndex]:
            temp = rootNode.List[index]
            rootNode.List[index] = rootNode.List[parentIndex]
            rootNode.List[parentIndex] = temp
        heapifyInsert(rootNode, parentIndex, heapType)

    elif heapType == "Max":
        if rootNode.List[index] > rootNode.List[parentIndex]:
            temp = rootNode.List[index]
            rootNode.List[index] = rootNode.List[parentIndex]
            rootNode.List[parentIndex] = temp
        heapifyInsert(rootNode, parentIndex, heapType)


# O(log N)T, S
def insert(rootNode, nodeValue, heapType):
    if rootNode.heapSize + 1 == rootNode.maxSize:
        return "Binary Heap is full"
    rootNode.List[rootNode.heapSize + 1] = nodeValue
    rootNode.heapSize += 1
    heapifyInsert(rootNode, rootNode.heapSize, heapType)
    return "Inserted Successfully"


def _siftdown_max(heap, startpos, pos):
    'Maxheap variant of _siftdown'
    newitem = heap[pos]
    # Follow the path to the root, moving parents down until finding a place
    # newitem fits.
    while pos > startpos:
        parentpos = (pos - 1) >> 1
        parent = heap[parentpos]
        if parent < newitem:
            heap[pos] = parent
            pos = parentpos
            continue
        break
    heap[pos] = newitem


def _siftup_max(heap, pos):
    'Maxheap variant of _siftup'
    endpos = len(heap)
    startpos = pos
    newitem = heap[pos]
    # Bubble up the larger child until hitting a leaf.
    childpos = 2*pos + 1    # leftmost child position
    while childpos < endpos:
        # Set childpos to index of larger child.
        rightpos = childpos + 1
        if rightpos < endpos and not heap[rightpos] < heap[childpos]:
            childpos = rightpos
        # Move the larger child up.
        heap[pos] = heap[childpos]
        pos = childpos
        childpos = 2*pos + 1
    # The leaf at pos is empty now.  Put newitem there, and bubble it up
    # to its final resting place (by sifting its parents down).
    heap[pos] = newitem
    _siftdown_max(heap, startpos, pos)


def pop_max(heap):
    """Maxheap version of a heappop."""
    lastelt = heap.pop()    # raises appropriate IndexError if heap is empty
    if heap:
        returnitem = heap[0]
        heap[0] = lastelt
        _siftup_max(heap, 0)
        return returnitem
    return lastelt




