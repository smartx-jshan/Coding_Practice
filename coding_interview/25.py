class MyCircularQueue:

    def __init__(self, k: int):
        self.q = [None] * k
        self.maxlen = k
        self.front = 0
        self.rear = 0

    def enQueue(self, value: int) -> bool:
        
        if self.q[self.rear] is None:
            self.q[self.rear] = value
            self.rear = (self.rear + 1 ) % self.maxlen
            return True
        return False

    def deQueue(self) -> bool:
        if self.front == self.rear and self.q[self.front] is None:
            return False
        self.q[self.front] = None
        self.front = (self.front +1) % self.maxlen
        return True

    def Front(self) -> int:
        if self.q[self.front] is None:
            return -1
        return self.q[self.front]

    def Rear(self) -> int:
        if self.q[self.rear -1] is None:
            return -1
        return self.q[self.rear-1]

    def isEmpty(self) -> bool:
        if self.front == self.rear and self.q[self.rear] is None:
            return True
        return False

    def isFull(self) -> bool:
        if self.front == self.rear and self.q[self.rear] is not None:
            return True
        return False
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()
