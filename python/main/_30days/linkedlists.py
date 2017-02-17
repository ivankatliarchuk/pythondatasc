class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Solution:
    def display(self, head):
        current = head
        while current:
            print(current.data, end = ' ')
            current = current.next

    def insert(self, head, data):
        if (head == None):
            self.head = Node(data)
        else:
            temp  = head
            while(self.__isTrue(temp)):
                temp = temp.next
            temp.next = Node(data)
        return self.head
    # private method, mfn
    def __isTrue(self, head):
        if (head.next == None):
            return False
        return True



mylist = Solution()
T = int(input())
head = None
for i in range(T):
    data = int(input())
    head = mylist.insert(head, data)

mylist.display(head)
