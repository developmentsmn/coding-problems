#s = "loveleetcode"
# first non-repeating char and return its index

import collections

def firstUniqChar(s: str) -> int:
    
    counters = collections.Counter(s)
    
    for i in range(0, len(s)):
        
        if 1 == counters[s[i]]:
            return i
        
    return -1

print(firstUniqChar("loveleetcode"))