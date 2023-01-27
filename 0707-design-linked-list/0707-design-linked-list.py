class Node:
    def __init__(self, val = None):
        self.val = val
        self.next = None

class MyLinkedList:

    def __init__(self):
        self.head = None

    def get(self, index: int) -> int:                
        current = self.head
        
        start = 0
        
        while current:
            if start == index:
                return current.val
        
            current = current.next
            start += 1
            
        return -1

    def addAtHead(self, val: int) -> None:      
        if not self.head:
            self.head = Node(val)
        else:
            newNode = Node(val)
            newNode.next = self.head
            self.head = newNode

    def addAtTail(self, val: int) -> None:        
        if not self.head:
            self.head = Node(val)
        else:
            current = self.head
            
            while current.next:
                current = current.next

            current.next = Node(val)
    
    def addAtIndex(self, index: int, val: int) -> None:
        if index == 0:
            self.addAtHead(val)
            return
        
        current = self.head
        start = 0

        while current:
            if start == index - 1:
                break

            current = current.next
            start += 1

        if current:
            newNode = Node(val)
            newNode.next = current.next
            current.next = newNode

    def deleteAtIndex(self, index: int) -> None:
        if index == 0:
            self.head = self.head.next
        else:
            current = self.head
            start = 0
            while current:
                if start == index - 1:
                    break
                
                current = current.next
                start += 1
            
            if current and current.next:
                current.next = current.next.next
#     def printLinkedList(self) -> None:
#         current = self.head
        
#         while current:
#             print(current.val, end=" ")
#             current = current.next
        
        
        
        

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)