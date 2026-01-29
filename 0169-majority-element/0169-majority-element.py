class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        can=None
        c=0

        for num in nums:
            if c==0:
                can=num
                c=1
            elif num==can:
                c+=1
            else:
                c-=1

        return can 


        