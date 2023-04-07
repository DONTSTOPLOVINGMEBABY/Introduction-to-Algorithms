class dll_NODE:
    def __init__(self, data):
        self.data = data 
        self.next = None
        self.prev = None 


class doubly_linked_list:
    def __init__(self):
        self.head = None
        self.tail = None
        self.num_elements = 0 

    
    ## appends item to the end of the list
    def append(self, data):
        node = dll_NODE(data)
        self.num_elements += 1 
        if self.tail == None:
            self.head = node 
            self.tail = node
            return 
        node.prev = self.tail  
        self.tail.next = node 
        self.tail = node 

    ## prepends item to the end of the list 
    def prepend(self, data):
        node = dll_NODE(data) 
        self.num_elements += 1 
        if self.head == None :
            self.tail = node 
            self.head = node 
            return 
        node.next = self.head 
        self.head.prev = node 
        self.head = node 


    ## Checks if node is in list
    ## returns node if found, false if not
    def isInList(self, data):
        if self.head == None : return False 
        if self.head.data == data : return self.head 
        temp = self.head 
        while (temp != None):
            if (temp.data == data):
                return temp 
            temp = temp.next
        return False 

    ## deletes a node from the list
    ## returns false if node dne true if it does & if delete was successful 
    def delete(self, data):
        if self.head == None : return False 
        if self.head.data == data:
            if self.head.next != None:
                self.head.next.prev = None 
                self.head = self.head.next 
                return True 
            else :
                self.head = None 
                self.tail = None
                return True 
        temp = self.head 
        while (temp.next != None and temp.next.data != data):
            temp = temp.next 
        if temp.next.data == data :
            if temp.next == self.tail :
                temp.next = None 
                self.tail = temp 
            else : 
                temp.next.next.prev = temp 
                temp.next = temp.next.next 
            return True 
        return False 
    
    def print_forward(self):
        if self.head == None: return "None" 
        string = ""
        temp = self.head 
        while temp != None :
            string += f"{temp.data} --> "
            temp = temp.next 
        return string + "None" 

    def print_backward(self):
        if (self.tail == None) : return "None" 
        string = ""
        temp = self.tail
        while temp != None:
            string += f" <-- {temp.data}"
            temp = temp.prev 
        return "None"  + string 


    def __len__(self):
        return self.num_elements 
    


class EfficientQueue(doubly_linked_list):

    def enqueue(self, item): 
        self.append(item) 
    
    def dequeue(self): 
        if self.head == None : return None 
        elif self.head == self.tail :
            item = self.head 
            self.head = None 
            self.tail = None 
            return item 
        else :
            item = self.head 
            self.head.next.prev = None 
            self.head = self.head.next 
            return item 

    def __str__(self):
        if self.head == None : return "[]"
        string = "[ "
        temp = self.head 
        while (temp != None):
            string += f"{temp.data}, "
            temp = temp.next
        string += f"]"
        return string




class EfficientStack(doubly_linked_list):
    
    def push(self, data):
        self.prepend(data)


    def pop(self):
        if self.head == None : return None 
        elif self.head == self.tail :
            item = self.head 
            self.head = None
            self.tail = None 
            return item 
        else :
            item = self.head 
            self.head.next.prev = None 
            self.head = self.head.next 
            return item 

    def __str__(self):
        if self.head == None : return "[]"
        string = "[ "
        temp = self.head 
        while (temp != None):
            string += f"{temp.data}, "
            temp = temp.next
        string += f"]"
        return string