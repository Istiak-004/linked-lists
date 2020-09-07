class Node(object):
    def __init__(self,data = None,next = None):
        self.data = data
        self.next = next
class LinkList:
    def __init__(self):
        self.head = None
    def append_first(self,data):
        node = Node(data,next = None)
        node.next = self.head
        self.head = node
    def append_last(self,data):
        node = Node(data,next = None)
        if self.head is None:
            self.head = node
            return
        last_node = self.head
        while last_node.next :
            last_node = last_node.next
        last_node.next = node
    def append_anywhere(self,data,previous_node):
        node = Node(data,next = None)
        if previous_node is None:
            print("there is no previous node")
            return
        node.next = previous_node.next
        previous_node.next = node
    def print_list(self):
        current_node = self.head
        while current_node:
            print(current_node.data)
            current_node = current_node.next
    def delete_list(self,key):
        cur_node = self.head
        if cur_node and cur_node.data == key:
            self.head = cur_node.next
            cur_node = None
            return
        previous_node = None
        while cur_node and cur_node.data != key:
            previous_node = cur_node
            cur_node = cur_node.next
        if cur_node is None:
            return
        else:    
            previous_node.next = cur_node.next
            cur_node = None
            return
    def list_index(self,key):
        current_node = self.head
        index = 0
        while current_node and current_node.data != key:
            #print(current_node.data)
            current_node = current_node.next
            index = index+1
        print(index)               

    def delete_on_position(self,pos):
        current_node = self.head
        if pos == 0:
            self.head = current_node.next
            current_node = None
            return
        previous_node = None
        count = 1
        while current_node and count != pos:
            previous_node = current_node
            current_node = current_node.next
            count += 1
        if current_node is None:
            return
        else:
            previous_node.next = current_node.next
            current_node = None    
        
        
s1 = LinkList()
s1.append_last('A')
s1.append_last('B')
s1.append_last('C')
s1.append_last('D')
s1.append_last('E')
#s1.append_anywhere(67,s1.head.next.next)
#s1.print_list()
# s1.delete_list('A')
# s1.delete_list('B')
# s1.delete_list('C')
#s1.list_index('P')
#s1.current_position(2)
s1.delete_on_position(1)
s1.print_list()