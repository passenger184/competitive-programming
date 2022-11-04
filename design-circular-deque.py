class MyCircularDeque:

    def __init__(self, k: int):
        self.size = k
        self.f = self.r = -1
        self.deque = [None for i in range(k)]
        
    def insertFront(self, value: int) -> bool:
        if (self.f == 0 and self.r == self.size - 1) or self.f == self.r + 1:
            return False
        
        else:
            if self.f == -1 and self.r == -1:
                self.f = self.r = 0
                self.deque[self.f] = value
                return True
            
            else:
                self.f = (self.f + self.size - 1) % self.size
                self.deque[self.f] = value
                return True

    def insertLast(self, value: int) -> bool:
        if (self.f == 0 and self.r == self.size - 1) or self.f == self.r + 1:
            return False
        
        else:
            if self.f == -1 and self.r == -1:
                self.f = self.r = 0
                self.deque[self.r] = value
                return True
            
            else:
                self.r = (self.r + 1) % self.size
                self.deque[self.r] = value
                return True
        

    def deleteFront(self) -> bool:
        if self.f == -1 and self.r == -1:
            return False
        else:
            if self.f == self.r:
                self.f = self.r = -1
                return True
            else:
                self.f = (self.f + 1) % self.size
                return True
        

    def deleteLast(self) -> bool:
        if self.f == -1 and self.r == -1:
            return False
        else:
            if self.f == self.r:
                self.f = self.r = -1
                return True
            else:
                self.r = (self.r + self.size - 1) % self.size
                return True
            

    def getFront(self) -> int:
        if self.f == -1 and self.r == -1:
            return -1
        else:
            return self.deque[self.f]

    def getRear(self) -> int:
        if self.f == -1 and self.r == -1:
            return -1
        else:
            return self.deque[self.r]

    def isEmpty(self) -> bool:
        if self.f == -1 and self.r == -1:
            return True
        else:
            return False

    def isFull(self) -> bool:
        if ((self.f == 0 and self.r == self.size - 1) or self.f == self.r + 1):
            return True
        else:
            return False


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()
