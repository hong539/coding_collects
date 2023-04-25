class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        
class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
        self.size = 0
        
    def is_empty(self):
        return self.size == 0
    
    def enqueue(self, value):
        new_node = Node(value)
        
        if self.is_empty():
            self.front = new_node
            self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node
            
        self.size += 1
        
    def dequeue(self):
        if self.is_empty():
            return None
        
        removed_node = self.front
        self.front = self.front.next
        self.size -= 1
        
        if self.is_empty():
            self.rear = None
        
        return removed_node.value

if __name__ == "__main__":
    q = Queue()

    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)

    print(q.dequeue())  # 1
    print(q.dequeue())  # 2

    q.enqueue(4)

    print(q.dequeue())  # 3
    print(q.dequeue())  # 4
    print(q.dequeue())  # None