class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i, j in enumerate(nums):
            other = target - j
            if other not in hashmap:
                hashmap[j] = i
            else:
                return [i, hashmap[other]]
