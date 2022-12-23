class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def set_next(self, next_node):
        self.next = next_node

    def get_next(self):
        return self.next

    def __str__(self):
        return self.data


class MyLinkedList:
    def __init__(self):
        self.head = None

    def set_head(self, new_node):
        self.head = new_node

    def prepend(self, new_node):
        new_node.next = self.head
        self.head = new_node

    def append(self, new_node):
        x: Node = self.head
        while x.next is not None:
            x = x.next
        x.next = new_node

    def get(self, index):
        x: Node = self.head
        i = 0
        while i < index:
            x = x.next
            i += 1
        return x

    def insert(self, index, new_node):
        if index == 0:
            self.prepend(new_node)

        x: Node = self.head
        i = 1
        while i < index:
            x = x.next
            i += 1
        temp_node = x.next
        x.next = new_node
        new_node.next = temp_node

    def size(self):
        linked_list = []
        if self.head is None:
            return 0

        x: Node = self.head
        while x is not None:
            linked_list.append(x)
            x = x.next

        return len(linked_list)

    def delete(self, index):
        if index == 0:
            self.head.next = None

        x: Node = self.head
        prev_node: Node
        i = 0
        while i < index:
            prev_node = x
            if x.next is None:
                break
            x = x.next
            i += 1
        if x.next is None:
            prev_node.next = None
        prev_node.next = x.next

    def __str__(self):
        linked_list = []
        if self.head is None:
            return [].__str__()

        x: Node = self.head
        while x is not None:
            linked_list.append(x.__str__())
            x = x.next

        return linked_list.__str__()


new_list = MyLinkedList()
print(new_list)
day1 = Node("Mon")
day2 = Node("Tue")
day3 = Node("Wed")
day4 = Node("Fri")
day5 = Node("Thur")
day6 = Node("Sat")
day7 = Node("Sun")

new_list.head = day1
day1.next = day2
day2.next = day3
day3.next = day4

print(new_list)

new_list.insert(3, day5)
print(new_list)
print(new_list.size())

new_list.prepend(day7)
print(new_list)
print(new_list.size())

new_list.append(day6)
print(new_list)
print(new_list.size())

new_list.delete(7)

for i in range(new_list.size()):
    print(new_list.get(i))