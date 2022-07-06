from ast import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:

        testSet = set(nums)

        if len(testSet) != len(nums):
            return True
        else:
            return False