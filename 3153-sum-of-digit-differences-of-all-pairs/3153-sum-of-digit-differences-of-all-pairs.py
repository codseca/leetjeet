class Solution(object):
    def sumDigitDifferences(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        ans = 0
        
        while nums[0] > 0:
            freq = [0] * 10
            
            for i in range(n):
                digit = nums[i] % 10
                freq[digit] += 1
                nums[i] //= 10
            
            for f in freq:
                ans += f * (n - f)

        return ans//2
        