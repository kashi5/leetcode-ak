class MyStack:

    def __init__(self):
        self.my_queue_1 = []
        self.my_queue_2 = []

    def push(self, x: int) -> None:
        self.my_queue_1.append(x)

    def pop(self) -> int:
        element = self.my_queue_1.pop()
        for i in range(len(self.my_queue_1)-1):
            self.my_queue_2.append(self.my_queue_1.pop())
        for j in range(len(self.my_queue_2)):
            self.my_queue_1.append(self.my_queue_2.pop())
        return element
        
    def top(self) -> int:
        return self.my_queue_1[len(self.my_queue_1) - 1]
        
    def empty(self) -> bool:
        if not len(self.my_queue_1):
            return True
        return False
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()