#making a queue data structure using linked list

import Node

class Queue:

    def _init_(self,f,r):
        self.front = f
        self.rear = r
        self.size = 0

    def _enqueue(self,r):
        self.count += 1
        if self.size == 1:
            self.front = r
            self.rear = r
        else:
            Node(r)._set_next(self.rear)
            self.rear = r  
    
    def _dequeue(self):
        self.size -= 1
        if self.size < 0:
            Node(self.front)._set_next(None)


    def _get_size(self):
        return self.size