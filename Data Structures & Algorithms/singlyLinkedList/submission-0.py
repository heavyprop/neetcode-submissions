class LinkedList:
    # index = 0, 1, 2
    # size = 3 for e.g.
    
    def __init__(self):
        self.size = 0
        self.head = None
    
    def get(self, index: int) -> int:
        # just in case out of bounds
        if 0 <= index < self.size:
            
            node = self.head
            for x in range(index):
                node = node.get_next()

            return node.get_value()
        
        else:
            return -1

    def insertHead(self, val: int) -> None:
        new_node = Node(val)
        new_node.set_next(self.head)
        
        # updating
        self.head = new_node
        self.size += 1

    def insertTail(self, val: int) -> None:

        new_node = Node(val)
        new_node.set_next(None)

        node = self.head

        if self.head != None:

            for x in range(self.size - 1):
                node = node.get_next()

            node.set_next(new_node)

        else: 
            self.head = new_node

        self.size += 1

    def remove(self, index: int) -> bool:
        if index != 0 and index < self.size:
            node = self.head

            for x in range(index - 1):
                node = node.get_next()

            node_1 = node

            the_node = node_1.get_next()

            node_2 = the_node.get_next()

            node_1.set_next(node_2)
            the_node.set_next(None)

            self.size -= 1
            return True
        
        elif index == 0 and index < self.size:
            node = self.head.get_next()
            self.head.set_next(None)
            self.head = node

            self.size -= 1
            return True

        else:
            return False


    def getValues(self) -> List[int]:
        arr = []
        node = self.head
        for x in range(self.size):
            arr.append(node.get_value())
            node = node.get_next()
        return arr

class Node:

    def __init__(self, value):
        self.value = value
        self.next = None

    def get_value(self):
        return self.value
    
    def set_next(self, Node):
        self.next = Node

    def get_next(self):
        return self.next