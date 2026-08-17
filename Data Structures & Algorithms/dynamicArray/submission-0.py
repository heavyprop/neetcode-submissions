class DynamicArray:
    
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.elements = [0] * capacity

    def get(self, i: int) -> int:
        return self.elements[i]

    def set(self, i: int, n: int) -> None:
        self.elements[i] = n

    def pushback(self, n: int) -> None:
        if self.size == self.capacity:
            self.resize()
        self.elements[self.size] = n
        self.size += 1
                
    def popback(self) -> int:
        n = self.elements[self.size - 1]
        self.elements[self.size - 1] = 0
        self.size -= 1
        return n
        
    def resize(self) -> None:
        self.capacity = self.capacity * 2
        new_arr = [0] * self.capacity
        for x in range(self.size):
            new_arr[x] = self.elements[x]
        self.elements = new_arr

    def getSize(self) -> int:
        return self.size
    
    def getCapacity(self) -> int:
        return self.capacity


#["Array", 1, "getSize", "getCapacity"]
#["Array", 1, "pushback", 1, "getCapacity", "pushback", 2, "getCapacity"]
