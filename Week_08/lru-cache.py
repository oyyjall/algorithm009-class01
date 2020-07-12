from collections import OrderedDict
class LRUCache:
    def __init__(self, capacity: int):
        self.size = capacity
        self.dic = OrderedDict()

    def get(self, key: int) -> int:
        if key not in self.dic:
            return -1
        val = self.dic.pop(key)
        self.dic[key] = val
        return val

    def put(self, key: int, value: int) -> None:
        if key in self.dic:
            self.dic.pop(key)
        else:
            if self.size > 0:
                self.size -= 1
            else:
                self.dic.popitem(last = False)
        self.dic[key] = value