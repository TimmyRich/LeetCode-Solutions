from Testing import test

"""
1. Two Sum

Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.
"""
def twoSum(nums, target):
  """
  :type nums: List[int]
  :type target: int
  :rtype: List[int]
  """
  diffMap = {}
  for index, num in enumerate(nums):
    if num in diffMap:
      return [diffMap[num], index]
    diffMap[target - num] = index
  
  

input = ([2,7,11,15], 9)
expectedOutput = [0, 1]
test(twoSum, input, expectedOutput)



