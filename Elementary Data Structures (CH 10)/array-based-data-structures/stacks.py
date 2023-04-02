'''
Psuedo-Code

STACK-EMPTY(S)
    if S.top == 0 
        return TRUE
    else return FALSE

PUSH(S, x)
    if S.top == S.size
        error "overflow"
    else 
        S.top = S.top + 1
        S[S.top] = x 

POP(S)
    if STACK-EMPTY(S)
        error "underflow"   
    else 
        S.top = S.top - 1 
        return S[S.top + 1]
'''

class Stack () :
    def __init__(self, initial_size=100):
        self.stack = [None] * initial_size
        self.top = -1 
        self.MAXSIZE = initial_size - 1

    def stack_empty (self) :
        if (self.top == -1):
            return True
        else : return False

    def push(self, element):
        if (self.top == self.MAXSIZE):
            print("MAXSIZE REACHED")
            return False
        else :
            self.top += 1 
            self.stack[self.top] = element

    def pop(self):
        if (self.stack_empty()):
            print("No elements on stack")
            return False
        else :
            self.top -= 1 
            return self.stack[self.top + 1] 
        
    def __str__(self): 
        string = "Empty Stack " if self.stack_empty() else ""
        ctr = 0 
        while (ctr <= self.top):
            string += f'{self.stack[ctr]} '
            ctr += 1
        return string + f'\nTop: {self.top}'


class ResizeableStack ():
    def __init__(self, initial_size=100):
        self.stack = [None] * initial_size
        self.top = -1 
        self.MAXSIZE = initial_size 

    def stack_empty (self) :
        if (self.top == -1):
            return True
        else : return False

    def push(self, element):
        if (self.top == self.MAXSIZE - 1):
            self.resize() 
            self.top += 1 
            self.stack[self.top] = element
        else :
            self.top += 1 
            self.stack[self.top] = element

    def pop(self):
        if (self.stack_empty()):
            print("No elements on stack")
            return False
        else :
            self.top -= 1 
            return self.stack[self.top + 1] 
        
    def resize(self): 
        if (self.MAXSIZE == 1) : self.MAXSIZE += 1 
        new_size = self.MAXSIZE * 2
        new_stack = [None] * new_size
        for i in range(len(self.stack)):
            new_stack[i] = self.stack[i] 
        self.stack = new_stack
        self.MAXSIZE = new_size
        
    def __str__(self): 
        string = "Empty Stack " if self.stack_empty() else ""
        ctr = 0 
        while (ctr <= self.top):
            string += f'{self.stack[ctr]} '
            ctr += 1
        return string + f'\nTop: {self.top} position\nStack Size: {self.MAXSIZE}'

