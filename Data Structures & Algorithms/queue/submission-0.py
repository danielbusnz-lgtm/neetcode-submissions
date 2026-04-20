class Deque:
    
    def __init__(self):
        self.queue = []

    def isEmpty(self) -> bool:
        if self.queue == []:
            return True
        else:
            return False

    def append(self, value: int) -> None:
        self.value = value
        return self.queue.append(self.value)

    def appendleft(self, value: int) -> None:
        self.value = value
        return self.queue.insert(0,self.value)

    def pop(self) -> int:
        if self.isEmpty():
            return -1
        else:
            return self.queue.pop(-1)

    def popleft(self) -> int:
        if self.isEmpty():
            return -1
        else:
            return self.queue.pop(0)

