class Solution(object):
    def decompressRLElist(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ans = []
        for i in range(0,len(nums)):
            if i % 2 ==0:
                for j in range(0,nums[i]):
                    ans.append(nums[i+1])
        
        return ans

