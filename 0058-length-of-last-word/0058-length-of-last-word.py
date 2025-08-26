class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        n=s.strip()
        j=n.split(" ")
        return (len(j[-1]))