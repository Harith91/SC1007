class Node():
        def __init__(self,data):
            self.data = data
            self.next = None
            return

class stack():
        def __init__(self):
            self.top = None
            self.size = 0
        
        def pop(self):
            if self.top == None:
                return ("Cannot remove from empty stack")
            popped = self.top
            self.top = self.top.next
            self.size -= 1
            return popped.data 
                

        def push(self,item):
            new = Node(item)
            if self.top == None:
                self.top = new
                self.size += 1
                return
                
            new.next = self.top
            self.top = new
            self.size +=1
            return
            
       
                
        def display(self):
            cur = self.top
            while cur != None:
                print(cur.data, end = " ")
                cur = cur.next
            print()
            return
                
def reverseStack(a):
    new = queue()
    for i in range(a.size):
        item = a.pop()
        new.push(item)

    for i in range(new.size):
        item = new.pop() 
        a.push(item)
    return a	
      			

s= stack()
s.push(1)
s.push(2)
s.push(3)
s.push(4)
print("Original") 
s.display() 
s = reverseStack(s)
print("Original")
s.display()


    
        
        
