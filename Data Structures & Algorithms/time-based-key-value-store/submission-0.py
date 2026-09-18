class TimeMap:

    def __init__(self):
        self.times_stamp_dict = collections.defaultdict(list)
        self.values_dict = collections.defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.times_stamp_dict[key].append(timestamp)
        self.values_dict[key].append(value)

    def get(self, key: str, timestamp: int) -> str:
        l,r = 0, len(self.times_stamp_dict[key]) - 1
        res = ""
        while l <= r:
            m = (l+r) // 2
            if self.times_stamp_dict[key][m] <= timestamp:
                res = self.values_dict[key][m]
                l = m + 1
            else:
                r = m - 1
        return res
