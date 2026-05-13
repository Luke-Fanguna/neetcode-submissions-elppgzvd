class TimeMap:
    def __init__(self):
        self.mapped = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.mapped:
            self.mapped[key] = []
        self.mapped[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        res, vals = "", self.mapped.get(key, [])
        l, r = 0, len(vals) - 1
        while l <= r:
            mid = (l + r) // 2
            if vals[mid][0] <= timestamp:
                res = vals[mid][1]
                l = mid + 1
            else:
                r = mid - 1
        return res
