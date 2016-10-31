class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class Solution:
    def insert(self, head, data):
        p = Node(data)
        if head == None:
            head = p
        elif head.next == None:
            head.next = p
        else:
            start = head
            while start.next != None:
                start = start.next
            start.next = p
        return head

    def display(self, head):
        current = head
        while current:
            print(current.data, end = ' ')
            current = current.next
    def removeDuplicates(self, head):
        unique = []
        prev = None
        temp = head
        while temp:
            if unique.__contains__(temp.data) == False:
                unique.append(temp.data)
                if prev == None:
                    prev = Node(temp.data)
                elif prev.next == None:
                    prev.next = Node(temp.data)
                else:
                    start = prev
                    while start.next != None:
                        start = start.next
                    start.next = Node(temp.data)
            else:
                pass
            temp = temp.next
        return prev
    def removeDuplicates2(self,head):
        '''
        not removing when out of order
        :param head:
        :return:
        '''
        node = head
        while node:
            if node.next:
                # if data is equal, reset the next pointer
                if node.data == node.next.data:
                    node.next = node.next.next
                else:
                    # if data is not equal, go
                    # to the next element
                    node = node.next
            else:
                node = node.next
        return head

mylist= Solution()
T=int(input())
head=None
for i in range(T):
    data=int(input())
    head=mylist.insert(head,data)

head=mylist.removeDuplicates(head)

mylist.display(head)
