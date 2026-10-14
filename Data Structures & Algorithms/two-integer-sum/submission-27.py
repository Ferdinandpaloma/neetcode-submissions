class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # set a pointer to the first index
        # have a for loop going through the 0+1 index asking if 
        # it adds up to the targe if so you can return it
        new_set = {}
        for i, num in enumerate(nums):
            sol = target - num
            if sol in new_set:
                return [new_set[sol], i]  # indices of the pair
            new_set[num] = i
                
                