from solution_01 import Solution


def test_example1():
    nums = [2, 7, 11, 15]
    target = 9

    solution = Solution()

    assert solution.twoSum(nums, target) == [0, 1], "Should be [0, 1]"


def test_example2():
    nums = [3, 2, 4]
    target = 6

    solution = Solution()

    assert solution.twoSum(nums, target) == [1, 2], "Should be [1, 2]"


def test_example3():
    nums = [3, 3]
    target = 6

    solution = Solution()

    assert solution.twoSum(nums, target) == [0, 1], "Should be [0, 1]"


if __name__ == "__main__":
    test_example1()
    test_example2()
    test_example3()
    print("Everything passed")
