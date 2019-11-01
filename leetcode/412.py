# But for multiples of three it should output "Fizz" instead of the number 
# and for the multiples of five output "Buzz". 
# For numbers which are multiples of both three and five output "FizzBuzz".

# n = 15,

# Return:
# [
#     "1",
#     "2",
#     "Fizz",
#     "4",
#     "Buzz",
#     "Fizz",
#     "7",
#     "8",
#     "Fizz",
#     "Buzz",
#     "11",
#     "Fizz",
#     "13",
#     "14",
#     "FizzBuzz"
# ]


class Solution:
    
    def fizzBuzz(self, n):

        result = []

        for i in range(1, n+1):

            Fizz = True if i%3 == 0 else False
            Buzz = True if i%5 == 0 else False

            if Fizz & Buzz:
                result.append("FizzBuzz")
            elif Fizz:
                result.append("Fizz")
            elif Buzz:
                result.append("Buzz")
            else:
                result.append(str(i))

        return result

def main():

    result = Solution()

    print (result.fizzBuzz(15))

if __name__ == '__main__':
    main()