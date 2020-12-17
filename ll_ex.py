class Node:
    def __init__(self, value, next):
        self.value = value
        self.next = next


class LinkedList:
    def __init__(self, value):
        self.head = Node(value, None)

    def append_end(self, value):
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = Node(value, None)

    def __str__(self):
        holder = ''
        curr = self.head
        while curr:
            holder += str(curr.value) + ' - '
            curr = curr.next
        return holder

    def __len__(self):
        holder = 0
        curr = self.head
        while curr:
            holder += 1
            curr = curr.next
        return holder

    def does_exist(self, value):
        curr = self.head
        while curr:
            if curr.value == value:
                return True
            curr = curr.next
        return False

    def __getitem__(self, value):
        index = 0
        curr = self.head
        while curr:
            if index == value:
                return curr.value
            curr = curr.next
            index += 1
        raise Exception("Invalid index")

    def insert_at(self, index, value):
        tracker = 0
        curr = self.head
        while curr:
            if tracker == index - 1:
                curr.next = Node(value, curr.next)
                return
            curr = curr.next
            tracker += 1
        raise Exception("Invalid index")

    def delete_first(self):
        self.head = self.head.next

    def delete_last(self):
        curr = self.head
        while curr.next.next:
            curr = curr.next
        curr.next = None


ll = LinkedList(0)
ll.append_end(1)
ll.append_end(1)
ll.append_end(2)
ll.append_end(2)
print(ll)

ll.delete_last()
print(ll)
