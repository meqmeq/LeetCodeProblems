
def triangleNumber(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
#         count = 0

#         for i in range(0,len(nums)-2):
#             a = nums[i]
#             if a == 0:
#                 continue
#             for j in range(i+1,len(nums) -1):
#                 b = nums[j]
#                 if b == 0:
#                     continue
#                 for k in range(j+1,len(nums)):
#                     c = nums[k]
#                     if  c== 0:
#                         continue
#                     if ((a+b) > c and a+c > b and b+c > a) or (a==b and b==c and a==c):
#                         count +=1

#         return count

    count = 0

    nums = sorted(nums)

    for i in range(2, len(nums)):
        val = nums[i]
        start, end = 0, i - 1
        while (start < end):
            if nums[start] + nums[end] > val:
                count += end - start
                end -= 1
            else:
                start += 1

    return count


print(triangleNumber([2, 2, 3, 4]))
