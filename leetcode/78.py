class Solution:
    
    def fillset(self, index, path, nums, sList):
        
        sList.append(path)
        
        for i in range(index, len(nums)):
            
            self.fillset(i+1, path + [nums[i]], nums, sList)
                   
       
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        sList = []
        self.fillset(0, [], nums, sList)
        return sList


def main():

    n = "123456789"

    s = Solution()
    s.sumStreamNumbers(n,0)

    for i in s.solutions:
        print(i)

if __name__ == '__main__':
    main()
