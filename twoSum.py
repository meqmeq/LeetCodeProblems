
def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
# Brute force
#         it1 = 0
#         for num1 in nums:

#             it2=1

#             for num2 in nums[1:(len(nums))]:


#                 if (num1 + num2) == target and it1 != it2:
#                     ans = [it1,it2]
#                     return ans
#                 it2+=1
#             it1 += 1

# 2 Pointers
#         numsDict = {}
#         for i in range(len(nums)):
#             if nums[i] in numsDict.keys():
#                 numsDict[nums[i]] += [i]
#             else:
#                 numsDict[nums[i]] = [i]
#         L = 0
#         R = len(nums) - 1
#         numsSorted = sorted(nums)
#         while L < R:
#             if numsSorted[L] + numsSorted[R] > target:
#                 R -= 1
#             elif numsSorted[L] + numsSorted[R] < target:
#                 L += 1
#             else:
#                 if numsSorted[L] == numsSorted[R]:
#                     return numsDict[numsSorted[L]]

#                 return numsDict[numsSorted[L]] + numsDict[numsSorted[R]]

# Complement
    complementDict = {}
    for i in range(len(nums)):
        if nums[i] in complementDict:
            return [complementDict[nums[i]], i]
        complement = target - nums[i]

        complementDict[complement] = i


print(twoSum([3, 2, 3], 6))
