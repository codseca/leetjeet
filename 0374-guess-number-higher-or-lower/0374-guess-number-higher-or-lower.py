class Solution(object):
    def guessNumber(self, n):
        s, e = 1, n

        while s <= e:
            mid = s + (e - s) // 2
            res = guess(mid)

            if res == 0:
                return mid
            elif res == -1:
                e = mid - 1
            else:
                s = mid + 1
