class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class SingleLinkedList:
    def __init__(self):
        self.head = None

    def print_list(self):
        if not self.head:
            print("List have no values")
            return
        current_node = self.head
        while current_node:
            print(current_node.data)
            current_node = current_node.next

    def insert_at_begining(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def insert_after_node_holding_data(self, node_data, data):
        current_node = self.head
        while current_node:
            if current_node.data == node_data:
                break
            current_node = current_node.next
        if not current_node:
            print("Data is not in the list")
        else:
            new_node = Node(data)
            new_node.next = current_node.next
            current_node.next = new_node

    def insert_before_node_holding_data(self, node_data, data):
        if self.head is None:
            print("List is empty")
            return
        if self.head.data == node_data:
            new_node = Node(data)
            new_node.next = self.head
            self.head = new_node
            return
        current_node = self.head
        while current_node.next:
            if current_node.next.data == node_data:
                break
            current_node = current_node.next
        if not current_node:
            print("Data is not in the list")
        else:
            new_node = Node(data)
            new_node.next = current_node.next
            current_node.next = new_node

    def delete_element_by_value(self, key):
        current_node = self.head
        if current_node and current_node.data == key:
            self.head = current_node.next
            current_node = None
            return
        prev_node = None
        while current_node and current_node.data != key:
            prev_node = current_node
            current_node = current_node.next
        if current_node is None:
            return
        prev_node.next = current_node.next
        current_node = None

    def delete_node_at_position(self, position):
        current_node = self.head
        if position == 0:
            self.head = current_node.next
            current_node = None
            return
        prev_node = None
        count = 1
        while current_node and count != position:
            prev_node = current_node
            current_node = current_node.next
            count += 1
        if current_node is None:
            return
        prev_node.next = current_node.next
        current_node = None

    def insert_at_index(self, index, data):
        if index == 0:
            new_node = Node(data)
            new_node.next = self.head
            self.head = new_node
        i = 0
        current_node = self.head
        while i < index-1 and current_node:
            current_node = current_node.next
            i += 1
        if not current_node:
            print("Index out of bounds")
        else:
            new_node = Node(data)
            new_node.next = current_node.next
            current_node.next = new_node

    def get_count(self):
        if self.head is None:
            return 0
        current_node = self.head
        count = 0
        while current_node is not None:
            count += 1
            current_node = current_node.next
        return count

    def create_linked_list(self):
        num_of_nodes = int(input("No of nodes that you want to create : "))
        if num_of_nodes == 0:
            return
        for num in range(num_of_nodes):
            data = int(input("Enter the value of the node : "))
            self.append(data)

    def reverse_linked_list(self):
        previous_node = None
        current_node = self.head
        while current_node:
            next_node = current_node.next
            current_node.next = previous_node
            previous_node = current_node
            current_node = next_node
        self.head = previous_node

if __name__ == '__main__':
    single_linked_list = SingleLinkedList()
    single_linked_list.create_linked_list()
    single_linked_list.print_list()
