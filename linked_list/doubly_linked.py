class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = Node(None)
        self.tail = Node(None)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.length = 0

    # ---------------helper functions--------------
    def is_empty(self):
        return self.length == 0
    
    def check_is_empty(self):
        if self.is_empty():
            raise IndexError("List is empty")

    def is_index(self, index):
        # check if index is already in the list
        return 0 <= index < self.length

    def is_insert_index(self, index):
        # check if index is an valid insert position
        return 0 <= index <= self.length

    def check_is_index(self, index):
        if not self.is_index(index):
            raise IndexError(f"Index {index} out of range: length = {self.length}")
    
    def check_insert_index(self, index):
        if not self.is_insert_index(index):
            raise IndexError(f"Invalid insert position {index}: length = {self.length}")
        
    def print_list(self):
        print(f"length = {self.length}")
        p = self.head.next
        while p != self.tail:
            print(f"{p.value} <-> ", end=" ")
            p = p.next
        print("end")
    # --------------getter and setter--------------
    # def get_first_value(self):
    #     if self.is_empty():
    #         raise IndexError("List is empty")
    #     return self.head.next.value
    
    # def get_last_value(self):
    #     if self.is_empty():
    #         raise IndexError("List is empty")
    #     return self.tail.prev.value
    
    def get_node(self, index):
        self.check_is_index(index)
        p = self.head
        for _ in range(index+1):
            p = p.next
        return p
            
    def get_node_value(self, index):
        p = self.get_node(index)
        return p.value
    
    def set_value(self, index, value):
        self.check_is_index(index)
        p = self.get_node(index)
        p.value = value   
            

    # ---------------insertion----------------
    def insert_at_beginning(self, value):
        new_node = Node(value)
        temp = self.head.next
        new_node.next = temp
        temp.prev = new_node
        self.head.next = new_node
        new_node.prev = self.head
        self.length += 1

    def insert_at_end(self, value):
        new_node = Node(value)
        temp = self.tail.prev
        new_node.prev = temp
        temp.next = new_node
        new_node.next = self.tail
        self.tail.prev = new_node
        self.length += 1

    def insert(self, index, value):
        self.check_insert_index(index)
        if index == 0:
            self.insert_at_beginning(value)
            return
        if index == self.length:
            self.insert_at_end(value)
            return
        p = self.get_node(index)
        p_prev_old = p.prev
        new_node = Node(value)
        new_node.next = p
        p.prev = new_node
        p_prev_old.next = new_node
        new_node.prev = p_prev_old
        self.length += 1
        
    # ---------------deletion----------------
    def delete_at_beginning(self):
        self.check_is_empty()
        temp = self.head.next
        temp.next.prev = self.head
        self.head.next = temp.next
        self.length -= 1
        return temp.value
    
    def delete_at_end(self):
        self.check_is_empty()
        temp = self.tail.prev
        temp.prev.next = self.tail
        self.tail.prev = temp.prev
        self.length -= 1
        return temp.value
        
    def delete(self, index):
        self.check_is_index(index)
        p = self.get_node(index)
        p.prev.next = p.next
        p.next.prev = p.prev
        self.length -= 1
        return p.value
            
if __name__ == "__main__":
    list = DoublyLinkedList()
    list.insert_at_beginning(1)
    list.insert_at_end(2)
    list.insert_at_end(3)
    list.insert_at_beginning(0)
    list.insert(2, 100)  
    print("List after inserting values:")
    list.print_list()         
