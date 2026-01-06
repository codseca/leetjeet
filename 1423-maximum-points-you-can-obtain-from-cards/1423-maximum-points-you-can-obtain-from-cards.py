class Solution(object):
    def maxScore(self, cardPoints, k):
        """
        :type cardPoints: List[int]
        :type k: int
        :rtype: int
        """
        sum1=sum(cardPoints[:k])
        l,r=k-1,len(cardPoints)-1
        max_sum=sum1
        curr_sum=sum1
        for i in range(0,k):
            curr_sum=curr_sum-cardPoints[l]
            curr_sum+=cardPoints[r]
            l-=1
            r-=1
            max_sum=max(max_sum,curr_sum)

        return max_sum


        # n = len(cardPoints)
        
        # if k == n:
        #     return sum(cardPoints)
        
        # window_size = n - k
        # total_sum = sum(cardPoints)
        
        # window_sum = sum(cardPoints[:window_size])
        # min_window_sum = window_sum
        
        # for i in range(window_size, n):
        #     window_sum += cardPoints[i]      
        #     window_sum -= cardPoints[i - window_size]  
        #     min_window_sum = min(min_window_sum, window_sum)
        
        # return total_sum - min_window_sum
        
