class DynamicArray:
    
    def __init__(self, capacity: int):

        self.capacity = capacity

        self.list = [] * capacity



    def get(self, i: int) -> int:
        return self.list[i]


    def set(self, i: int, n: int) -> None:
        self.list[i] = n
        


 
    def pushback(self, n: int) -> None:
        if self.getSize() == self.capacity:
            self.resize()
        self.list.append(n)

    def popback(self) -> int:
        return self.list.pop(-1)
        

    def resize(self) -> None:
        self.capacity *= 2


    def getSize(self) -> int:
        return len(self.list)
    
    def getCapacity(self) -> int:
        
        return self.capacity