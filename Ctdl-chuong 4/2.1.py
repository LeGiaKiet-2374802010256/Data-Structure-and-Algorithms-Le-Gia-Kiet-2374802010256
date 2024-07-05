class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
    def printList(self):
        temp = self.head
        while (temp):
            print(temp.data)    
            temp = temp.next
if __name__=='__main__':
    llist = LinkedList()
    llist.head = Node(10)
    second = Node(11)
    third = Node(12)
    
    llist.head.next = second;
    second.next = third;
    llist.printList()