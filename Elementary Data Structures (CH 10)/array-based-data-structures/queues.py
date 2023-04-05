'''
Psuedo-Code

ENQUEUE(Q, x)
    Q[Q.tail] = x
    if Q.tail == Q.size
        Q.tail = 1 
    else Q.tail = Q.tail + 1 

DEQUEUE(Q)
    x = Q[Q.head]
    if Q.head == Q.size
        Q.head = 1 
    else Q.head = Q.head + 1 
    return x   

'''

class CLRSQueue:
    def __init__(self, initial_size = 100):
        self.queue = [None] * initial_size
        self.head = 0
        self.tail = 0 
        self.size = initial_size 

    def isEmpty(self):
        return self.head == self.tail

    def underflow(self):
        return self.head == self.size

    def overflow(self):
        return self.head == self.tail + 1 or (self.head == 0 and self.tail == self.size)

    def enqueue(self, item):
        if not self.overflow(): 
            self.queue[self.tail] = item
            if self.tail == self.size - 1:
                self.tail = 0 
            else :
                self.tail = self.tail + 1 
    
    def dequeue(self):
        if not self.underflow():
            item = self.queue[self.head]
            if self.head == self.size:
                self.head = 1 
            else :
                self.head = self.head + 1 
            return item
    
    def __str__(self):     
        string = f'{self.queue[self.head:self.size]}'
        return string



class AdjustableCLRSQueue: 
    def __init__(self, initial_size = 100):
        self.queue = [None] * initial_size
        self.head = 0
        self.tail = 0 
        self.size = initial_size 

    def isEmpty(self):
        return self.head == self.tail

    def underflow(self):
        return self.head == self.size

    def overflow(self):
        return self.head == self.tail + 1 or (self.head == 0 and self.tail == self.size)

    def enqueue(self, item):
        if not self.overflow(): 
            self.queue[self.tail] = item
            self.tail = self.tail + 1 
        else : 
            self.resize() 
            self.enqueue(item)

    def resize(self): 
        if (self.size == 1) : self.size += 1 
        new_size = self.size * 2 
        new_queue = [None] * new_size 
        for i in range(len(self.queue)):
            new_queue[i] = self.queue[i]
        self.queue = new_queue
        self.size = new_size

    def dequeue(self):
        if not self.underflow():
            item = self.queue[self.head]
            if self.head == self.size:
                self.head = 1 
            else :
                self.head = self.head + 1 
            return item
    
    def __str__(self):     
        string = f'{self.queue[self.head:self.tail]}'
        none_ctr = 0 
        if (not self.overflow()): 
            for i in self.queue:
                if (i == None): none_ctr += 1 
            string += f' None * {none_ctr}'
        elif (self.isEmpty):
            string += f' None * {self.size}'
        return string
