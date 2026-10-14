class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        ''' 
        we have an array of ones and zeros
        we are looking for the most sequential amount of ones in a row
        solution 1:
        We would have a max that holds the max amount of count
        We would have the current count that holds we are counting
        have a for loop that goes through the array and if 1 count += 1
        if 0 and if current count is greater than max count then max = current

        '''
        maxCount = 0
        currentCount = 0
        for i in nums:
            if i == 1:
                currentCount += 1
                maxCount = max(maxCount, currentCount)
            else:
                currentCount = 0
        return maxCount