# Write a function that reverses a string. The input string is given as an array of characters char[].

# Do not allocate extra space for another array, 
# you must do this by modifying the input array in-place with O(1) extra memory



def reverseString(s):

    left = 0
    right = len(s)-1

    while(left < right):

        tempC = s[left]
        s[left] = s[right]
        s[right] = tempC
        
        left += 1
        right -= 1

    return s


s = list("hello")
print(reverseString(s))