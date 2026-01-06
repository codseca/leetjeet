class Solution(object):
    def maxArea(self, height):
        l=0
        n=len(height)
        r=n-1
        max_water=0
        while(l<r):
            width=r-l
            current_height=min(height[l],height[r])
            current_amount_of_water=width*current_height
            max_water=max(max_water,current_amount_of_water)

            if height[l]<height[r]:
                l=l+1
            else:
                r=r-1
        return max_water

            

