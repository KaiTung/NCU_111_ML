class Solution(object):
    def maximumWealth(self, accounts):
        """
        :type accounts: List[List[int]]
        :rtype: int
        """
        
        ans = 0
        
        for sub_list in accounts:
            temp = 0
            for i in sub_list:
                temp += i
                if temp >= ans:
                    ans = temp

        return ans