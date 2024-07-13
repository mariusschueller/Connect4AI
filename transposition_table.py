from typing import List, Optional


class TranspositionTable:
    class Entry:
        def __init__(self, key: int = 0, val: int = 0):
            self.key = key & ((1 << 56) - 1)  # use 56-bit keys
            self.val = val  # use 8-bit values

    def __init__(self, size: int):
        assert size > 0
        self.T: List[TranspositionTable.Entry] = [self.Entry() for _ in range(size)]

    def index(self, key: int) -> int:
        return key % len(self.T)

    def reset(self):
        # fill everything with 0, because 0 value means missing data
        for entry in self.T:
            entry.key = 0
            entry.val = 0

    def put(self, key: int, val: int):
        assert 0 <= key < (1 << 56)
        assert 0 < val < (1 << 8)
        i = self.index(key)  # compute the index position
        self.T[i].key = key  # and override any existing value.
        self.T[i].val = val

    def get(self, key: int) -> int:
        assert 0 <= key < (1 << 56)
        i = self.index(key)  # compute the index position
        if self.T[i].key == key:
            return self.T[i].val  # and return value if key matches
        else:
            return 0  # or 0 if missing entry
