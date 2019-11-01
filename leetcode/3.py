
# Given a string, find the length of the longest substring without repeating characters.

# Input: "abcabcbb"
# Output: 3 

# 1 2 3 4 5 6
# p w w k e w
# 1 2 1 2 3 3

def findLongestSubstring(s):
    maxV = 0
    tempV = 0
    dic = {}
        
    for i in range(len(s)):
            
        if s[i] in dic:
            tempV = max(tempV, dic[s[i]])
            
        maxV = max(maxV, i+1 - tempV)
        dic.update({s[i]: i+1})
            
    return maxV

    

s = "abcabcbb"

print(findLongestSubstring(s))