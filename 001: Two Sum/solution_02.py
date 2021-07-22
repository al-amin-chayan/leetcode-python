from itertools import combinations


class Solution:

    def twoSum(self, nums: list, target: int) -> list:

        pairs = list(combinations(range(0, len(nums)), 2))

        pair_sum = lambda a, b: nums[a] + nums[b]

        for pair in pairs:

            if pair_sum(*pair) == target:
                return list(pair)
