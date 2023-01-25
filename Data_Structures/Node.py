class Node:

    def __init__(self,d,n):
        self.data = d
        self.next = n
    
    def _set_data(self,d):
        self.data = d
    
    def _get_data(self):
        return self.data

    def _set_next(self, n):
        self.next = n
    
    def _get_next(self):
        return self.next