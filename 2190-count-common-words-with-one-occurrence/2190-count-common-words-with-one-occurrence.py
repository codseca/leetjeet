from collections import Counter
class Solution(object):
    def countWords(self, words1, words2):
        """
        :type words1: List[str]
        :type words2: List[str]
        :rtype: int
        """
        cnt1=Counter(words1)
        cnt2=Counter(words2)
        return sum(1 for word in cnt1 if cnt1[word] == 1 and cnt2[word] == 1)
