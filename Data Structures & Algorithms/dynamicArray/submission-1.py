class DynamicArray:
    
    def __init__(self, capacity: int):
        # initialising the array
        # storing the CAPACITY
        # storing the SIZE which is the num. of elements
        # making the elements which is the size of the capacity
        self.capacity = capacity
        self.size = 0
        self.elements = [0] * capacity

    def get(self, i: int) -> int:
        # getting an element at a specific idx
        return self.elements[i]

    def set(self, i: int, n: int) -> None:
        # setting the array normally
        self.elements[i] = n

    def pushback(self, n: int) -> None:
        # appending an elements and if it goes out of bounds we assign more capacity
        if self.size == self.capacity:
            self.resize()
        self.elements[self.size] = n
        self.size += 1
                
    def popback(self) -> int:
        # popping an element off
        n = self.elements[self.size - 1]
        self.elements[self.size - 1] = 0
        self.size -= 1
        return n
        
    def resize(self) -> None:
        # making the capcity twice as big and then moving each element back into the twice as big array
        self.capacity = self.capacity * 2
        new_arr = [0] * self.capacity
        for x in range(self.size):
            new_arr[x] = self.elements[x]
        self.elements = new_arr

    def getSize(self) -> int:
        # getting the size of the array
        return self.size
    
    def getCapacity(self) -> int:
        # getting the capacity of the array
        return self.capacity


#["Array", 1, "getSize", "getCapacity"]
#["Array", 1, "pushback", 1, "getCapacity", "pushback", 2, "getCapacity"]
