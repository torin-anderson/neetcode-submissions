class TimeMap:

    def __init__(self):
        self.keys = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.keys:
            self.keys[key] = []
        self.keys[key].append([value, timestamp])
        

    def get(self, key: str, timestamp: int) -> str:
        values = self.keys.get(key, [])
        l, r = 0, len(values) -1
        output = ""
        while l <= r:
            m = (r + l)//2
            if values[m][1] <= timestamp:
                l = m + 1
                output = values[m][0]
            elif values[m][1]:
                r = m - 1
        return output
             
