class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        
        x, y = len(nums1), len(nums2)
        low, high = 0, x
        
        while low <= high:
            i = (low + high) // 2
            j = (x + y + 1) // 2 - i
            
            max_left_x = float('-inf') if i == 0 else nums1[i - 1]
            min_right_x = float('inf') if i == x else nums1[i]
            
            max_left_y = float('-inf') if j == 0 else nums2[j - 1]
            min_right_y = float('inf') if j == y else nums2[j]
            
            if max_left_x <= min_right_y and max_left_y <= min_right_x:
                # حالة صحيحة
                if (x + y) % 2 == 0:
                    return (max(max_left_x, max_left_y) + min(min_right_x, min_right_y)) / 2.0
                else:
                    return max(max_left_x, max_left_y)
            elif max_left_x > min_right_y:
                high = i - 1
            else:
                low = i + 1
                
                
                
# this my version code

x = [1, 2]
y = [3, 4]

total_length = len(x) + len(y)

# نحسب الموضعين في النص
mid1 = (total_length // 2) - 1
mid2 = total_length // 2

FirstNumber = None
SecondNumber = None

# ندمج بعقل بدون sort فعلي
i = j = 0
count = 0

while i < len(x) or j < len(y):
    val = None

    if j >= len(y) or (i < len(x) and x[i] <= y[j]):
        val = x[i]
        i += 1
    else:
        val = y[j]
        j += 1

    if count == mid1:
        FirstNumber = val
    if count == mid2:
        SecondNumber = val
        break

    count += 1

print((FirstNumber + SecondNumber) / 2.0)

