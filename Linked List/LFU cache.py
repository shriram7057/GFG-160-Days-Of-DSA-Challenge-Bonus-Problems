from collections import  defaultdict , OrderedDict
class LFUCache:
    def __init__(self, cap: int):
        self.cap = cap
        self.minFreq=0
        self.keyMap= {}
        self.freqMap = defaultdict(OrderedDict)
    
    def _update(self,key):
        value, freq = self.keyMap[key]
        del self.freqMap[freq][key]
        
        if not self.freqMap[freq]:
            if self.minFreq == freq:
                self.minFreq += 1
            del self.freqMap[freq]
        self.keyMap[key][1] = freq + 1
        self.freqMap[freq+1][key] = value
    
    def get(self, key: int) -> int:
        #code here
        if key not in self.keyMap:
            return -1
        self._update(key)
        return self.keyMap[key][0]
        
    
    def put(self, key: int, value: int) -> None:
        #code here
        if self.cap == 0:
            return 
        if key in self.keyMap:
            self.keyMap[key][0] = value
            self._update(key)
            return 
        if len(self.keyMap) == self.cap:
            lf = self.minFreq
            k, _ = self.freqMap[lf].popitem(last=False)
            del self.keyMap[k]
            if not self.freqMap[lf]:
                del self.freqMap[lf]
        
        self.keyMap[key] = [value,1]
        self.freqMap[1][key] = value
        self.minFreq = 1

