class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            new_node.prev = None
            self.head = new_node
        else:
            current_node = self.head
            while current_node.next:
                current_node = current_node.next
            current_node.next = new_node
            new_node.prev = current_node
            new_node.next = None

    def insert_at_begining(self, data):
        new_node = Node(data)
        if not self.head:
            new_node.prev = None
            self.head = new_node
        else:
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node
            new_node.prev = None

    def add_after_node(self, key, data):
        current_node = self.head
        while current_node:
            if current_node.next is None and current_node.data == key:
                self.append(data)
                return
            elif current_node.data == key:
                new_node = Node(data)
                next_node = current_node.next
                current_node.next = new_node
                new_node.next = next_node
                new_node.prev = current_node
                next_node.prev = new_node
            current_node = current_node.next

    def add_before_node(self, key, data):
        current_node = self.head
        while current_node:
            if current_node.prev is None and current_node.data == key:
                self.insert_at_begining(data)
                return
            elif current_node.data == key:
                new_node = Node(data)
                previous_node = current_node.prev
                previous_node.next = new_node
                current_node.prev = new_node
                new_node.next = current_node
                new_node.prev = previous_node
            current_node = current_node.next

    def delete_node(self, key):
        current_node = self.head
        while current_node:
            if current_node.data == key and current_node == self.head:
                if not current_node.next:
                    current_node = None
                    self.head = None
                    return
                else:
                    next_node = current_node.next
                    current_node.next = None
                    next_node.prev = None
                    current_node = None
                    self.head = next_node
                    return
            elif current_node.data == key:
                if current_node.next:
                    next_node = current_node.next
                    prev_node = current_node.prev
                    prev_node.next = next_node
                    next_node.prev = prev_node
                    current_node.next = None
                    current_node.prev = None
                    current_node = None
                    return
                else:
                    prev_node = current_node.prev
                    prev_node.next = None
                    current_node.prev = None
                    current_node = None
                    return
            current_node = current_node.next


    def print_list(self):
        if not self.head:
            print("List have no values")
            return
        current_node = self.head
        while current_node:
            print(current_node.data)
            current_node = current_node.next


if __name__ == '__main__':
    doubly_linked_list = DoublyLinkedList()
    doubly_linked_list.append(1)
    doubly_linked_list.append(2)
    doubly_linked_list.append(3)
    doubly_linked_list.append(4)
    doubly_linked_list.add_before_node(1, 10)
    doubly_linked_list.delete_node(5)
    doubly_linked_list.print_list()
