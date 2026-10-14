class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashset = set()
        for i in nums:
            if i in hashset:
                return True
            hashset.add(i)
        return False

        # for i in range(len(nums)):
        #     if nums[i] == range(len(nums), i + 1):
        #         return False
        # return True
        