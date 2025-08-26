class Solution(object):
    def plusOne(self, digits):
        return [int(x) for x in str(int(''.join(map(str, digits))) + 1)]
