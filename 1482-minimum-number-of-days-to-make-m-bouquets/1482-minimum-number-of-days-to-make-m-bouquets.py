class Solution(object):
    def minDays(self, bloomDay, m, k):
        """
        :type bloomDay: List[int]
        :type m: int
        :type k: int
        :rtype: int
        """
        start = 1
        end = max(bloomDay)
        ans = -1

        while start <= end:
            mid = start + (end - start) / 2
            bouquets = 0
            consecutive = 0

            for h in bloomDay:
                if h <= mid:
                    consecutive += 1
                    if consecutive == k:
                        bouquets += 1
                        consecutive = 0
                else:
                    consecutive = 0

            if bouquets >= m:
                ans = mid
                end = mid - 1  
            else:
                start = mid + 1

        return ans

