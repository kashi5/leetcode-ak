class MyQueue:

    def __init__(self):
        self.my_stack_1 =[]
        self.my_stack_2 =[]
        

    def push(self, x: int) -> None:
        self.my_stack_1.append(x)
        
    def pop(self) -> int:
        for i in range(len(self.my_stack_1) - 1):
            self.my_stack_2.append(self.my_stack_1.pop())
        element = self.my_stack_1.pop()
        for j in range(len(self.my_stack_2)):
            self.my_stack_1.append(self.my_stack_2.pop())
        return element

    def peek(self) -> int:
        if self.my_stack_1[0]:
            return self.my_stack_1[0]
        
    def empty(self) -> bool:
        if not len(self.my_stack_1):
            return True
        return False


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()