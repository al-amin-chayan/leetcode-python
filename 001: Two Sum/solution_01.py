class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        length = len(nums)

        enumerate_nums = enumerate(nums)

        for i, num in enumerate_nums:

            j = i + 1

            while j < length:

                if num + nums[j] == target:
                    return [i, j]
                j += 1