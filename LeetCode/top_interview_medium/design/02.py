import random

class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.data = collections.defaultdict(int)
        self.result = []
        

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val in self.data: #데이터가 있다면(삭제되었을 수도 있음)
            if self.data[val] == 1: #데이터가 있는데 삭제되었다면
                return False
            else: #데이터가 있는데 삭제되었다면
                self.data[val] =1
                self.result.append(val)
                return True
        else:
            self.data[val] = 1
            self.result.append(val)
            return True
        

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val in self.data:
            if self.data[val] == 1: #있는 경우
                self.data[val] = 0

