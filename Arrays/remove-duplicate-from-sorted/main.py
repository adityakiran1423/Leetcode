class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        temp = list(set(nums))
        nums.clear()
        for i in range(len(temp)):
            nums.append(temp[i])
        return len(nums)