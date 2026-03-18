class Node:
    def __init__(self, data):
        self.data = data   # store element
        self.next = None   # reference to next node


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0
        print("Created new LinkedList")
        print("Current size:", self.count)
        print("Head:", self.head)

    def size(self):
        return self.count

    def append(self, element):
        new_node = Node(element)

        if self.head is None:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

        self.count += 1
        print(f"Appended {element} to the list")

    def prepend(self, element):
        new_node = Node(element)

        if self.head is None:
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node

        self.count += 1
        print(f"Prepend {element} to the list")

    def get(self, index):
        if index < 0 or index >= self.count:
            return "Index out of range"

        current = self.head
        for _ in range(index):
            current = current.next

        return current.data

    def set(self, index, element):
        if index < 0 or index >= self.count:
            return "Index out of range"

        current = self.head
        for _ in range(index):
            current = current.next

        current.data = element
        print(f"Set element at index {index} to {element}")

    def print_list(self):
        current = self.head
        result = []
        while current:
            result.append(str(current.data))
            current = current.next
        print("Print Linked list :[" + " ".join(result) + "]")

ll = LinkedList()

ll.append(5)
print("Element at index 0:", ll.get(0))

ll.set(0, 10)
print("Element at index 0:", ll.get(0))

print("Current size:", ll.size())

ll.prepend(10)

ll.print_list()