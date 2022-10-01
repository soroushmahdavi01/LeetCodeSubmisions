class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # list of numbers
        # two numbers = target
        # only ONE valid answer
        # avoid O(n ^2)
        answer = {}
        for i,n in enumerate(nums):
            difference = target - n
            if difference in answer:
                return [answer[difference], i]
            answer[n] = i
            
        
                           
            
        
            
        
