class Solution(object):
    def maxPoints(self, points):
        n = len(points)
        if n <= 2:
            return n

        ans = 0

        for i in range(n):
            x1, y1 = points[i]
            slopes = {}
            same = 1
            vertical = 0

            for j in range(i + 1, n):
                x2, y2 = points[j]

                if x1 == x2 and y1 == y2:
                    same += 1
                elif x1 == x2:
                    vertical += 1
                else:
                    dy = y2 - y1
                    dx = x2 - x1

                    g = self.gcd(dy, dx)
                    dy //= g
                    dx //= g

                    slopes[(dy, dx)] = slopes.get((dy, dx), 0) + 1

            curr = vertical
            for v in slopes.values():
                curr = max(curr, v)

            ans = max(ans, curr + same)

        return ans

    def gcd(self, a, b):
        while b:
            a, b = b, a % b
        return a
