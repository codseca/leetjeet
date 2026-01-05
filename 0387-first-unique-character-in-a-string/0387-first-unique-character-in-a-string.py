class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        f={}
        for i in s:
            f[i]=f.get(i,0)+1
        for j in range(len(s)):
            if f[s[j]]==1:
                return j
        return -1