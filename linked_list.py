class Node:
    def __init__(self, data=None, next=None):
        # houd data bij & reference naar volgende node
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        node = Node(data, self.head)
        self.head = node

    def print(self):
        # als de LinkedList leeg is, print error.
        if self.head is None:
            raise Exception("List is empty")
            return

        itr = self.head
        llstring = ''
        # blijf loopen zolang de volgende node NIET null is
        while itr:
            llstring += str(itr.data) + ' ---> '
            itr = itr.next
        print(llstring)

    def insert_at_end(self, data):
        # als de list leeg is, maak de eerste Node met een next van None
        if self.head is None:
            self.head = Node(data, None)
            return

        # loop zolang er een volende node is.
        itr = self.head
        while itr.next:
            itr = itr.next

        # wanneer er geen volgende node is (eind), maak een link naar einde
        itr.next = Node(data, None)

    def insert_values(self, values):
        self.head = None
        for value in values:
            self.insert_at_end(value)

    def __len__(self):
        count = 0
        itr = self.head
        # loop door nodes zolang de current NIET none is
        while itr:
            count += 1
            itr = itr.next
        return count

    def remove(self, idx):
        if idx < 0 or idx >= self.__len__():
            raise Exception("Invalid index!")
        # als index 0 is, zet head naar head + 1
        if idx == 0:
            self.head = self.head.next
            return
        count = 0
        itr = self.head
        while itr:
            if count == idx - 1:
                itr.next = itr.next.next
                break
            itr = itr.next
            count += 1

    def insert_at(self, idx, value):
        if idx < 0 or idx >= self.__len__():
            raise Exception("Invalid index!")
        if idx == 0:
            self.insert_at_beginning(value)
            return
        count = 0
        itr = self.head
        while itr:
            if count == idx - 1:
                node = Node(value, itr.next)
                itr.next = node
                break
            itr = itr.next
            count += 1

    def insert_after_value(self, data_after, data_to_insert):
        itr = self.head
        count = 0
        while itr:
            if itr.data == data_after:
                itr.next = Node(data_to_insert, itr.next)
                break
            itr = itr.next
            count += 1

    def remove_by_value(self, data):
        itr = self.head
        count = 0
        while itr:
            if itr.data == data:
                self.remove(count)
                break
            itr = itr.next
            count += 1


ll = LinkedList()
ll.insert_values([1, 2, 3, 4, 5])
ll.insert_after_value(5, 'e')
ll.print()
print(len(ll))
