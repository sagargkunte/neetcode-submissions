class MyHashMap:

    def __init__(self):
        self.map_ = dict()

    def put(self, key: int, value: int) -> None:
        self.map_[key] = value
        

    def get(self, key: int) -> int:
        if key in self.map_:
            return self.map_[key]
        else:
            return -1

    def remove(self, key: int) -> None:
        if key in self.map_:
            self.map_.pop(key)


