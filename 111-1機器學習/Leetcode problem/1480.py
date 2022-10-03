class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ans = []
        j = len(nums)
        
        while True:
            temp = 0
            
            if j ==1:
                for i in nums:
                    temp += i
                ans.append(temp)
                break
            else:
                for i in nums[:-(j-1)]:
                    temp += i
                j -= 1
                ans.append(temp)
        
        return ans