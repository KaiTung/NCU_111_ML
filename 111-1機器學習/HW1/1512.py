class Solution(object):
    def numIdenticalPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = 0
        for i in range(len(nums)):
            for j in nums[i+1:]:
                if nums[i] == j:
                    ans += 1
                    
        return ans