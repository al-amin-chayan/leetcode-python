class Solution:

    def twoSum(self, nums: list, target: int) -> list:

        previous = {}

        for i, x in enumerate(nums):

            y = target - x
            
            if y in previous:
                return [i, previous[y]]

            previous[x] = i
