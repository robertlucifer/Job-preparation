class Node:
    def __init__(self, data, next =None):
        self.data = data
        self.next = next


class Linked_list:
    def __init__(self):
        self.head = None

    def insertion_at_beginning(self, data):
        node = Node(data, self.head)
        self.head = node

    def insertion_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None)
            return
        itr = self.head
        while itr.next:
            itr = itr.next

        itr.next = Node(data, None)

    def print(self):
        if self.head is None:
            print("The Linked list is empty")
            return

        itr = self.head
        llstr = ''
        while itr:
            llstr += str(itr.data)
            if itr.next:
                llstr += "-->"
            itr = itr.next

        print(llstr)

    def length_of_ll(self):
        itr = self.head
        counter = 0
        while itr:
            counter += 1
            itr = itr.next

        return counter

    def creating_ll_using_array(self, array):
        self.head = None
        for x in array:
            self.insertion_at_end(x)

    def remove_at(self, index):
        if index<0 or index > self.length_of_ll():
            print("The entered index is invalid ")
            return
        if index == 0:
            self.head = self.head.next
            return

        counter = 0
        itr = self.head
        while itr:
            if counter == index -1:
                itr.next = itr.next.next
            counter +=1
            itr = itr.next
    def insert_at(self, index, value):
        if index <0 or index > self.length_of_ll():
            print("The entered index is invalid")
            return
        if index == 0 :
            self.head = Node(value)
            return

        counter = 0
        itr = self.head
        while itr:
            counter +=1
            itr= itr.next
            if counter == index - 1:
                itr.next=Node(value, itr.next )
                return

ll = Linked_list()
ll.creating_ll_using_array([1, 2, 3, 4, 5, 6, 7])
ll.print()
ll.remove_at(6)
ll.print()
ll.insert_at(4,86)
ll.print()
print(ll.length_of_ll())
