class queue(object):
    def __init__(self, a, h, t, s):
        self.head = h
        self.tail = t
        self.size = s
        self.list = a

    def isfull(self):
        return((self.size - self.tail + self.head) % self.size == 1)

    def enqueue(self, x):
        if self.isfull() == False:
            self.list[self.tail] = x
            self.tail = (self.tail + 1) % self.size
        else:
            print("Queue is full!")

# TODO def a constructor for queue object
if __name__ == '__main__':
    A = [1,2,3,0,0,0,0,0,0,0]
    h = 0
    t = 3
    s = 10
    myqueue = queue(A, h, t, s)
    print(myqueue.list)
    print(myqueue.head)
    print(myqueue.tail)
    print(myqueue.size)
    print(myqueue.isfull)
    for i in range(4,11):
        myqueue.enqueue(i)
    print(myqueue.isfull)