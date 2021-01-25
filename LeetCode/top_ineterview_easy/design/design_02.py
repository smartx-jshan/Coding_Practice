class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.arr = []
        

    def push(self, x: int) -> None:
        self.arr.append(x)

    def pop(self) -> None:
        del self.arr[-1]
        

    def top(self) -> int:
        return self.arr[-1]

    def getMin(self) -> int:
        return min(self.arr)
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
