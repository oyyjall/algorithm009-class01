class BinaryHeap:
    def __init__(self):
        self.d = 2
        self.heap = []
        self.heapSize = 0

    def binaryHeap(self, capacity):
        self.heap = [-1] * (capacity + 1)

    def isEmpty(self):
        return self.heapSize == 0

    def isFull(self):
        return self.heapSize == len(self.heap)

    def parent(self, i):
        return (i-1) // self.d

    def kthChild(self, i, k):
        return self.d * i + k

    def insert(self, x):
        """往堆里插入新元素，时间复杂度是：O(logN)，最坏的情况需要遍历到根节点"""
        if self.isFull():
            raise('Heap is full, No space to insert new element')
        self.heap[self.heapSize] = x
        self.heapSize += 1
        self.heapifyUp(self.heapSize - 1)

    def delete(self, idx):
        """删除下标为idx的值，时间复杂度是：O(logN)"""
        if self.isEmpty():
            raise('Heap is empty, No element to delete')
        maxElement = self.heap[idx]
        self.heap[idx] = self.heap[-1]
        self.heapifyDown(idx)
        self.heapSize -= 1

    def heapifyUp(self, index):
        insertValue = self.heap[index]
        while index > 0 and insertValue > self.heap[self.parent(index)]:
            self.heap[index] = self.heap[self.parent(index)]  # 把父节点移下来
            index = self.parent(index)  # 把父节点的下标赋给当前下标，也就是说将这个值往上移
        """退出循环时，说明已经找到了合适的位置，将需要插入的值放在当前位置即可"""
        self.heap[index] = insertValue

    def heapifyDown(self, index):
        """当删除一个元素时，维护堆（此处是最大堆）的属性"""
        temp = self.heap[index]
        while self.kthChild(index, 1) < self.heapSize:   # 若当前位置不是叶子节点时
            child = self.maxChild(index)
            if temp >= self.heap[child]:
                break
            self.heap[index] = self.heap[child]
            index = child
            # print(self.heap)
        self.heap[index] = temp

    def maxChild(self, index):
        leftchild = self.kthChild(index, 1)
        rightchild = self.kthChild(index, 2)
        return leftchild if self.heap[leftchild] > self.heap[rightchild] else rightchild

    def findMax(self):
        if self.isEmpty():
            raise('Heap is empty')
        return self.heap[0]

    def printHeap(self):
        for i in range(0, len(self.heap)):
            print(self.heap[i], end = ' ')
        print(' ')

    def printY(self):
        print(self.heap)

if __name__ == "__main__":
    maxHeap = BinaryHeap()
    maxHeap.binaryHeap(10)
    maxHeap.insert(10)
    maxHeap.printY()
    maxHeap.insert(4)
    maxHeap.printY()
    maxHeap.insert(9)
    maxHeap.printY()
    maxHeap.insert(1)
    maxHeap.printY()
    maxHeap.insert(7)
    maxHeap.printY()
    maxHeap.insert(5)
    maxHeap.printY()
    maxHeap.insert(3)
    maxHeap.printY()
    # maxHeap.printHeap()
    maxHeap.delete(5)
    maxHeap.printY()
    # maxHeap.printHeap()
    maxHeap.delete(2)
    maxHeap.printY()
    # maxHeap.printHeap()


