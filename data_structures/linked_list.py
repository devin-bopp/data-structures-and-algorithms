class Node:
    def __init__(self, value):
        self.value = value
        self.next_node = None
    
    def get_value(self):
        return self.value

    def get_next_node(self):
        return self.next_node.value

    def set_next_node(self, next_node):
        self.next_node = next_node

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def add_node_to_end(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        if self.length > 0:
            current_tail = self.tail
            current_tail.set_next_node(new_node)
            self.tail = new_node
        self.length += 1

    def __iter__(self):
        current = self.head
        while current:
            yield current
            current = current.next_node
        


my_list = LinkedList()

my_list.add_node_to_end(1)
my_list.add_node_to_end(2)
my_list.add_node_to_end(3)


for i in my_list:
    print(i.get_value())