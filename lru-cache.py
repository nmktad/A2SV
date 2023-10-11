class Node:
    def __init__(self, key: int, val: int, nextnode = None, prevnode = None):
        self.key = key
        self.val = val
        self.next = nextnode
        self.prev = prevnode

class LRUCache:

    def __init__(self, capacity: int):
        self.dict = {}
        
        self.cap = capacity
        
        self.head = Node(-1, -1)
        self.tail = Node(-1, -1)
        
        self.head.next = self.tail
        self.tail.prev = self.head
        
    def get(self, key: int) -> int:
        if key in self.dict:
            node = self.dict[key]
            
            if node != self.head.next:
                self.deleteNode(node)
                self.addNextToHead(node)                
            
            return node.val
        else:
            return -1
        

    def put(self, key: int, value: int) -> None:
        if key in self.dict:
            node = self.dict[key]
            self.deleteNode(node)
            self.addNextToHead(node)
            node.val = value
            
        else:
            if self.cap <= len(self.dict):
                delNode = self.tail.prev
                self.deleteNode(delNode)
                
                del self.dict[delNode.key]
            
            node = Node(key, value)
            self.addNextToHead(node)
            self.dict[key] = node
            
    def addNextToHead(self, node: Node) -> None:
        temp = self.head.next
        
        self.head.next = node
        node.prev = self.head
        
        temp.prev = node
        node.next = temp
        
        temp = None
    
    def deleteNode(self, node: Node) -> None:
        node.prev.next = node.next
        node.next.prev = node.prev
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)