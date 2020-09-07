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
        
        
s1 = LinkList()
s1.append_first(12)
s1.append_first(23)
s1.append_first(34)
s1.append_last(45)
s1.append_last(56)
s1.append_anywhere(67,s1.head.next.next)
s1.print_list()