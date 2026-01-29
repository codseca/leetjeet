class Solution(object):
    def averageValue(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # n=len(nums)
        # c=0
        # a=0
        # for i in range(n):
        #     if nums[i]%2==0 and nums[i]%3==0:
        #         c+=1
        #         a+=nums[i]

            
        # return a//c if c!=0 else 0

        a=[x for x in nums if x%6==0]
        return sum(a)//len(a) if a else 0

        