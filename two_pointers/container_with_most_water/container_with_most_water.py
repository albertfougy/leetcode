# Since we know area = length * min (height_a, height_b), to maximize the area 
# we want to maximize both height and length.

# Width: We set two pointers, which are initialized as 0 and len(height) - 1 to 
# get the max width.

# Height: We move the left pointer and right pointer respectively to search for 
# the next higher height.

def maxArea(self, height):
    max_area = area = 0
    left, right = 0, len(height) - 1
    while left < right:
        l, r = height[left], height[right]
        if l < r:
            area = (right - left) * l
            while height[left] <= l:
                left += 1
        else:
            area = (right - left) * r
            while height[right] <= r and right:
                right -= 1
        if area > max_area:
            max_area = area
    return max_area