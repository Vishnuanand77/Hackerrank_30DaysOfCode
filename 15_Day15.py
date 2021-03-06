# Day 15 : Linked List

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None 
class Solution: 
    def display(self,head):
        current = head
        while current:
            print(current.data,end=' ')
            current = current.next

    def insert(self,head,data): 
        #Complete this method
        node = Node(data)
        #Check if head is pointing to a node. If not make current node the head
        if head == None:
            head = node
        else:
            current = head
            while(current.next is not None):
                current = current.next #Parse through the linked list to the end
            current.next = node
        return head

mylist= Solution()
T=int(input())
head=None
for i in range(T):
    data=int(input())
    head=mylist.insert(head,data)    
mylist.display(head); 	  