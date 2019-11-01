# Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

# Note: For the purpose of this problem, we define empty string as valid palindrome.

# example: taco cat , True

import collections 

class Solution:

    def isPalindrome(self, s):

        s = s.replace(" ","")
        if s == "":
            return True
        
        s = s.lower()
        
        left = 0
        right = ( len(s) -1 )
        
        print(s)
        
        while(left <= right):
            
            if s[left].isalnum() and s[right].isalnum():
                
                if(s[left]!= s[right]):
                    return False
                left+= 1
                right-= 1
                continue
            
            # isalpha() is for letters only
            # isalnum() is for numbers and letters

            left = left if s[left].isalnum() else left+1
            right = right if s[right].isalnum() else right-1

        return True

def main():
    
    s = 'bbcbb'

    print(Solution().isPalindrome(s))

if __name__ == "__main__":
    main()

