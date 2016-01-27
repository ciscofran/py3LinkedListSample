class Node:
    def __init__ (self, d = None, nn = None):
        self.data= d
        self.next_node = nn
    
    def set_data(self, d):
        self.data = d
    
    def get_data(self):
        return self.data
    
    def get_next(self):
        return self.next_node
    
    def set_next(self, new_next):
        self.next_node = new_next
               
class LinkedList:
    def __init__(self, head = None):
        self.head = head
        self.size = 0
        
    def get_size (self):
        return self.size    
        
    def insert(self,data):
        new_node = Node(data)
        new_node.set_next(self.head)
        self.head = new_node
        self.size += 1
    
    def find(self, data):
        this_node = self.head
        while this_node:
            if this_node.get_data() == data:
                return data
            else:
                this_node = this_node.get_next()
        return None
    
    def show(self):
        print("showing linked list data")
        current_node = self.head
        while current_node is not None:
            print (current_node.data)
            current_node = current_node.next_node
            
    
         
l_list = LinkedList()
l_list.insert("Victor")
l_list.insert("Sam")
l_list.insert("Jas")

print(l_list.find("Sam"))
l_list.show()


     

        
