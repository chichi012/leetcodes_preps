class Node:
    def __init__(self,key,value):
        self.pair = (key,value)
        self.next = None

class MyHashMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.capacity = 10000
        self.arr = [None]*self.capacity


    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative. 0 <= key
        """
        index = key % self.capacity
        if self.arr[index] is None:
            self.arr[index] = Node(key,value)
        else:
            cur = self.arr[index]
            while cur is not None:
                if cur.pair[0] == key:
                    cur.pair = (key,value)
                    return 
                prev = cur
                cur = cur.next
            prev.next = Node(key,value)   #add keys with colliding indexes 

    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is
        mapped, or -1 if this map contains no mapping for
        the key
        """
        index = key%self.capacity
        cur = self.arr[index]
        while cur is not None:
            if cur.pair[0] == key:
                return cur.pair[1]
            else:
                cur = cur.next
        return -1

        

    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if
        this map contains a mapping for the key
        """
        index = key % self.capacity
        cur = prev = self.arr[index]
        if not cur:
            return -1
        if cur.pair[0] == key:
            self.arr[index] = cur.next
        else:
            cur = cur.next
            while cur is not None:
                if cur.pair[0] == key:
                    prev.next = cur.next
                    break
                else:
                    cur = cur.next
                    prev=prev.next



# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
