class Solution(object):
    def restoreString(self, s, indices):
        """
        :type s: str
        :type indices: List[int]
        :rtype: str
        """
        ans = ['']*len(s)
        
        for i in range(0,len(indices)):
            ans[indices[i]] =s[i] 
        

        return ''.join(i for i in ans)
        