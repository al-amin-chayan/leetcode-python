from importlib import import_module
import unittest

module = import_module('001_two_sum.solution_01')


class TestTwoSum(unittest.TestCase):
    def test_example1(self):
        """
        Test that it can sum two list element to match target value and return the indexes
        """
        nums = [2, 7, 11, 15]
        target = 9

        solution = module.Solution()
        result = solution.twoSum(nums, target)

        self.assertTrue(set(result) == set([0, 1]))

    def test_example2(self):
        """
        Test that it can sum two list element to match target value and return the indexes
        """
        nums = [3, 2, 4]
        target = 6

        solution = module.Solution()
        result = solution.twoSum(nums, target)

        self.assertTrue(set(result) == set([1, 2]))

    def test_example3(self):
        """
        Test that it can sum two list element to match target value and return the indexes
        """
        nums = [3, 3]
        target = 6

        solution = module.Solution()
        result = solution.twoSum(nums, target)

        self.assertTrue(set(result) == set([0, 1]))


if __name__ == '__main__':
    unittest.main()
