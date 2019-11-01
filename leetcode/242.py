# Given two strings s and t , write a function to determine if t is an anagram of s.
# Input: s = "anagram", t = "nagaram"
# Output: true
# Input: s = "rat", t = "car"
# Output: false

import collections

class Solution:
    def isanagram(self, s, t):

        if len(t)!=len(s):
            return False
        
        tC = collections.Counter(t)
        sC = collections.Counter(s)

        for c in tC:
            if tC[c] != sC[c]:
                return False

        return True
        

def main():

    s = "anagram"
    t = "nagaram"

    print( Solution().isanagram(s,t) )

if __name__ == "__main__":
    main()

