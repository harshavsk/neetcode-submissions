class Node:
    def __init__(self,key,val):
        self.key,self.val = key, val
        self.prev = self.next = None
class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.maps = {}
        self.left,self.right = Node(0,0), Node(0,0)
        self.left.next, self.right.prev = self.right, self.left
    def insert(self,node):
        prev, nxt = self.right.prev,self.right
        prev.next = nxt.prev = node
        node.next, node.prev = nxt,prev
    def remove(self, node):
        prev, nxt = node.prev, node.next
        prev.next,nxt.prev = nxt,prev
    def get(self, key: int) -> int:
        if key in self.maps:
            self.remove(self.maps[key])
            self.insert(self.maps[key])
            return self.maps[key].val
        return -1
    def put(self, key: int, value: int) -> None:
        if key in self.maps:
            self.remove(self.maps[key])
        self.maps[key] = Node(key,value)
        self.insert(self.maps[key])
        if len(self.maps)>self.cap:
            lru = self.left.next
            self.remove(lru)
            del self.maps[lru.key]
