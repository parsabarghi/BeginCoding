# Linked List
## node class
class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


## linked list class
class LinkedList:
    def __init__(self):
        self.head = None

    def insert_begining(self, data):
        node = Node(data, self.head)
        self.head = node

    def print(self):
        if self.head is None:
            print("Linked List is empty!")
            return

        itr = self.head
        llstr = ''

        while itr:
            llstr += str(itr.data) + " --> "
            itr = itr.next

        print(llstr)

    def insert_end(self, data):
        if self.head is None:
            self.head = Node(data, None)
            return

        itr = self.head
        while itr.next:
            itr = itr.next

        itr.next = Node(data, None)

    def insert_value(self, data_lists):
        self.head = None
        for data in data_lists:
            self.insert_end(data)

    def get_len(self):
        count = 0
        itr = self.head
        while itr:
            count += 1
            itr = itr.next

        return count

    def remove(self, index):
        if index<0 or index>self.get_len():
            raise Exception("Invalid index")

        if index == 0:
            self.head = self.head.next
            return

        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                itr.next = itr.next.next
                break
            itr = itr.next
            count += 1

    def insert(self, index, data):
        if index<0 or index>self.get_len():
            raise Exception("Invalid index")

        if index == 0:
            self.insert_begining(data)
            return

        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                node = Node(data, itr.next)
                itr.next = node
                break
            itr = itr.next
            count += 1

    def insert_after_value(self, value, data):
        if self.head is None:
            print("we dont have new value!!")

        itr = self.head
        while itr:
            if value == itr.data:
                node = Node(data, itr.next)
                itr.next = node
                break
            itr = itr.next

    def removing_by_value(self, value):
        itr = self.head
        count = 0
        while itr:
            if value == itr.data:
                self.remove(count)
                break
            itr = itr.next
            count += 1



if __name__ == '__main__':
    ## insert at beggining test
    print("Insert at begining test: ")
    ib = LinkedList()
    ib.insert_begining(5)
    ib.insert_begining(55)
    ib.print()
    print("lenght: ", ib.get_len())
    print("___________________________________")
    ## insert at end test
    print("Insert at end test: ")
    ie = LinkedList()
    ie.insert_end(25)
    ie.insert_end(65)
    ie.print()
    print("lenght: ", ie.get_len())
    print("___________________________________")
    ## insert values test
    print("insert values test: ")
    iv = LinkedList()
    iv.insert_value(["Parsa", "Barghi", "Salam", "Khobi"])
    ## remove test
    iv.remove(2)
    ## insert index test
    iv.insert(2,"parsa")
    iv.print()
    print("lenght: ", iv.get_len())
    print("___________________________________")
    ## insert after value test
    print("insert after special value test: ")
    iv.insert_after_value("parsa", "Chara")
    iv.insert_after_value("Barghi", "mmd")
    iv.print()
    print("lenght: ", iv.get_len())
    print("___________________________________")
    print("removing by value test: ")
    iv.removing_by_value("mmd")
    print("lenght: ", iv.get_len())
    iv.print()




