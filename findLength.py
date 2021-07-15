def findLength(nums1, nums2):
    """
    :type nums1: List[int]
    :type nums2: List[int]
    :rtype: int
    """
    """
    Brute Force
    """
#         ans = 0
#         for i in range(len(nums1)):
#             for j in range(len(nums2)):
#                 n = 0
#                 if nums1[i] == nums2[j]:
#                     if i+n >= len(nums1) or   j+n >= len(nums2):
#                         break;
#                     while nums1[i+n] == nums2[j+n]:

#                         n+=1
#                         if n >= ans:
#                             ans = n
#                         if i+n >= len(nums1) or   j+n >= len(nums2): break
#         if ans == 0: return 0
#         return ans

    dp = [[0] * (len(nums2)+1)
          for _ in range(len(nums1)+1)]  # Initialize zero up to 5

    for i in range(1, len(nums1)+1):

        for j in range(1, len(nums2)+1):
            if nums1[i - 1] == nums2[j - 1]:
                dp[i][j] = 1 + dp[i-1][j-1]

    return max(map(max, dp))


# print(findLength([1, 2, 3, 2, 1],
#                  [3, 2, 1, 4, 7]))

print(findLength([1, 2, 3, 2, 1],
                 [3, 2, 1, 4]))
