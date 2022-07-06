#Approach 1  ==> O(n) space and time
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prev = {}
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in prev:
                return [i, prev[diff]]
            prev[nums[i]] = i

# Approach 2 ==> O(n) space and time
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        arr = {}
        for i in range(len(nums)):
            arr[nums[i]] = i
            
        for i in range(len(nums)):
            if target - nums[i] in arr and i != arr[target-nums[i]]:
                return [arr[target-nums[i]], i]


#Approach 3  ==> O(1) space and 0(n2) time
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        for i in range(len(nums)-1):
            for j in range(i+1,len(nums),1):
                if nums[i]+nums[j] == target:
                    return[i,j]
