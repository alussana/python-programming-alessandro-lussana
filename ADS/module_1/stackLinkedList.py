class Node:  
    def __init__(self, data): 
        self.data = data 
        self.next = None
  
class LinkedList: 
    def __init__(self):  
        self.head = None

    def push(self, new_data): 
        new_node = Node(new_data) 
        new_node.next = self.head  
        self.head = new_node
    
    def topoPrint(self):
        top = self.head
        a = []
        while top != None:
            a.append(top.data)
            top = top.next
        print(a)

if __name__ == '__main__':
    L = LinkedList()
    
    for i in range(6):
        L.push(i)
        L.topoPrint()