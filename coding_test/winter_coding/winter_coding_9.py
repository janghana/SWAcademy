N = int(input())

class CircleQueue:
    rear = 0
    front = 0
    MAX_SIZE = N
    queue = list()

    def __init__(self):
        self.rear = 0
        self.front = 0
        self.queue = [-1 for i in range(self.MAXSIZE)]

    def is_empty(self):
        if self.rear == self.front:
            return "true"
        return "false"

    def is_full(self):
        if (self.rear + 1) % self.MAX_SIZE == self.front:
            return "true"
        return "false"

    def enqueue(self, x):
        self.rear = (self.rear + 1) % (self.MAX_SIZE)
        self.queue[self.rear] = x

    def dequeue(self):
        self.front = (self.front + 1) % self.MAX_SIZE
        return self.queue[self.front]

while True:
    try:
        S = input().split()
        if S[0] == 'enQueue':
            CircleQueue.enqueue(int(S[1]))
            print(CircleQueue.front)
        elif S[0] == 'Front':
            print(CircleQueue.front)
        elif S[0] == 'Rear':
            print(CircleQueue.rear)
        elif S[0] == 'isFull':
            print(CircleQueue.is_full())
        elif S[0] == 'deQueue':
            CircleQueue.dequeue()
        elif S[0] == 'isEmpty':
            print(CircleQueue.is_empty())
    except:
        break
