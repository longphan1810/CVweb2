from collections import defaultdict
from queue import PriorityQueue

class node:
    def __init__(self,name,g=0, par=None):
        self.name = name
        self.g = g
        self.par = par

    def __lt__(self, other):
        if other == None:
            return False
        return self.g < other.g
    
    def display(self):
        print(self.name, self.g)
    
    def __eq__(self, other):
        if other == None:
            return False
        return self.name == other.name

def equal(O, G):
    return O == G

def checkInQ(O, c):
    if O == None:
        return False
    return (O in c.queue)

def path(O):
    print(O.name)
    if O.par != None:
        path(O.par)
    else:
        return

data = defaultdict(list)
data['A'] = ['B', 3, 'C', 1, 'D', 5]
data['B'] = ['E', 3, 'F', 2]
data['C'] = ['G', 1, 'H', 5]
data['D'] = ['I', 2]

def search(S, G):
    Open = PriorityQueue()
    Close = PriorityQueue()

    Open.put(S)

    while True:
        if Open.empty():
            print('k tim thay')
            return
        
        O = Open.get()
        Close.put(O)
        print('dang duyet', O.name, O.g)
        if equal(O, G):
            print('tim thay', O.name)
            path(O)
            print('distamce',O.g)
            return
        i = 0
        while i < len(data[O.name]):
            name = data[O.name][i]
            g = O.g + data[O.name][i+1]
            
            tmp = node(name = name, g = g)
            tmp.par = O
            ok1 = checkInQ (tmp, Open)
            ok2 = checkInQ (tmp, Close)
            if not ok1 and not ok2:
                Open.put(tmp)
            i += 2
    

search(node('A'), node('I2'))

        
        



