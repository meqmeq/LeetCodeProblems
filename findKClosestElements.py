"""
Given a sorted integer array arr, two integers k and x, return the k closest integers to x in the array. The result should also be sorted in ascending order.

An integer a is closer to x than an integer b if:

|a - x| < |b - x|, or
|a - x| == |b - x| and a < b
"""


def findClosestElements(arr, k, x):
    """
        :type arr: List[int]
        :type k: int
        :type x: int
        :rtype: List[int]
        """

#         answer = []
#         howFarAns= 100000000000
#         for i in range(0,len(arr) - k + 1):
#             howFar = 0
#             for num in arr[i:i+k]:
#                 if num >= x:
#                     howFar += num - x
#                 elif num < x:
#                     howFar += x - num
#             if howFar < howFarAns:
#                 howFarAns = howFar
#                 answer = arr[i:i+k]

#         return answer

    L = 0
    R = len(arr)
    if len(arr) <= 1 or k >= len(arr):
        return arr
    while (R-L) >= 2:
        mid = int((R+L)/2)
        if arr[mid] < x:
            L = mid
        elif arr[mid] > x:
            R = mid
        else:
            R = mid

    if k == 1:
        if abs(x - arr[L]) <= abs(arr[R] - x):
            return [arr[L]]
        else:
            return [arr[R]]

    while R-L < k:
        if R >= len(arr):
            L -= 1
        elif ((abs(x - arr[L-1]) <= abs(arr[R] - x) and L > 0)):
            L -= 1
        else:
            R += 1

    return arr[L:R]


# print(findClosestElements([0, 1, 2, 2, 2, 3, 6, 8, 8, 9], 5, 9))
print(findClosestElements([1, 2, 3, 4, 5], 4, -1))
# print(findClosestElements([0, 0, 1, 2, 3, 3, 4, 7, 7, 8], 3,
#                           5))
# print(findClosestElements([0, 2, 2, 3, 4, 6, 7, 8, 9, 9], 4, 5))
