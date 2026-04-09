class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
class LinkedList:
    def __init__(self):
        self.head = None
    def is_empty(self):
        return
        self.head is None
    
    def append(self, data):
        new_node = Node(data)
# If list is empty
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
# Move to the last node
            while current.next is not None:
                current = current.next
# Add new node at the end
            current.next = new_node
            
    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        
    def display(self):
        current = self.head
        while current is not None:
            print(current.data, end=" -> ")
            current = current.next
        print("None")
        
# Test code
linked_list = LinkedList()

linked_list.append(10)
linked_list.append(20)
linked_list.append(30)

linked_list.prepend(5)

linked_list.display()

def insert_at_position(self, data, position):
    new_node = Node(data)

# Insert at beginning
    if position == 0:
        new_node.next = self.head
        self.head = new_node
        return

    current = self.head
    count = 0

# Move to the position before where we insert
    while current is not None and count < position - 1:
        current = current.next
        count += 1

# If position is out of range
    if current is None:
        print("Position out of range")
        return

# Insert node
    new_node.next = current.next
    current.next = new_node
    
 # Test code
linked_list = LinkedList()

linked_list.append(10)
linked_list.append(20)
linked_list.append(30)

insert_at_position(linked_list, 15, 1)
linked_list.display()

def delete_by_value(self, value):
    current = self.head

 # case 1: empty list
    if current is None:
        print("List is empty")
        return

 # case 2: value is at head
    if current.data == value:
        self.head = current.next
        return

# case 3: value is in middle or end
    prev = None

    while current is not None and current.data != value:
        prev = current
        current = current.next

    # value not found
    if current is None:
        print("Value not found")
        return

    # delete node
    prev.next = current.next
 # Test code
linked_list = LinkedList()

linked_list.append(10)
linked_list.append(20)
linked_list.append(30)

linked_list.display

delete_by_value(linked_list, 20)
linked_list.display()
    
    
def search(self, value):
    current = self.head
    index = 0

    while current:
        if current.data == value:
            return index
        current = current.next
        index += 1

    return -1
#Test code
linked_list = LinkedList()

linked_list.append(10)
linked_list.append(20)
linked_list.append(30)

linked_list.display

print(search(linked_list, 40))

def display(self):
    current = self.head

    if current is None:
        print("List is empty")
        return

    while current:
        print(current.data, end=" -> ")
        current = current.next

    print("None")
# Test code
linked_list = LinkedList()

linked_list.append(10)
linked_list.append(20)
linked_list.append(30)

linked_list.display()

def is_empty(self):
    return self.head is None
if linked_list.is_empty():
    print("List is empty")
else:
    print("List is not empty")
    
def size(self):
    current = self.head
    count = 0
    while current:
        count += 1
        current = current.next
    return count

# Test code
if __name__ == "__mainn__":
    linked_list = LinkedList()

    linked_list.append(10)
    linked_list.append(20)
    linked_list.append(30)
    linked_list.prepend(5)
    insert_at_position(linked_list, 15, 1)
    delete_by_value(linked_list, 20)
    print(search(linked_list, 40))
    linked_list.display()

    print("size of linked list:", size(linked_list))
