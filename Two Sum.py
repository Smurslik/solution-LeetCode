```
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.
```
class Solution(object):
    def twoSum(self, nums, target):
        b = []
        for i in range(0, len(nums)):
            for n in range(i+1, len(nums)):
                if nums[i] + nums[n] == target:
                    b.append(i)
                    b.append(n)
                    break
        return b
                    
