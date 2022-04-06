from typing import List
import unittest
from unittest import TestCase
import sys
import threading

class BinarySearch(object):

    def __init__(self):
        pass

    @classmethod
    def firstNotSmaller(self, nums: List[int], target: int) -> int:

        start = 0
        end = len(nums)-1
        res = -1

        while start <= end:
            middle = (start + end) // 2
            if (nums[middle] >= target):
                res = middle
                end = middle - 1
            else:
                start = middle + 1

        return res

    @classmethod
    def firstOccurrence(self, nums: List[int], target: int) -> int:

        start = 0
        end = len(nums) - 1
        res = -1

        while start <= end:
            middle = (start + end) // 2
            
            if (target <= nums[middle]):
                if (target == nums[middle]):
                    res = middle
                end = middle - 1
            else:
                start = middle + 1
        return res

    @classmethod
    def squareRoot(self, target: int) -> int:

        if (target <= 1):
            return target

        res = None
        start = 0
        end = target

        while (start <= end):
            middle = (start + end) // 2
            if (middle * middle > target):
                end = middle - 1
            else:
                res = middle
                start  = middle + 1

        return res

    @classmethod
    def minSortedRotatedArray(self, nums: List[int]) -> int:

        start = 0
        end = len(nums) - 1
        res = -1 * sys.maxsize

        while start <= end:

            middle = (start + end) // 2
            res = middle
            if (nums[start] <= nums[middle]):
                start = middle + 1
            else:
                end = middle - 1

        return res

    @classmethod
    def mountainPeak(self, nums: List[int]) -> int:

        res = -1 * sys.maxsize

        start = 0
        end = len(nums) - 1

        while (start <= end):

            middle = (start + end) // 2

            if (nums[middle] >= nums[middle + 1]):
                res = middle
                end = middle - 1
            else:
                start = middle + 1

        return res


class TestBinarySearch(TestCase):

    def setUp(self):

        self.search = BinarySearch()

    def testFirstNotSmaller(self):

        testSetFirstNotSmaller = [
            ([], 1, -1),
            ([1,2,3], 2, 1),
            ([1,2,2,4], 3, 3),
            ([1,2,3], 4, -1)
        ]

        for testInputs in testSetFirstNotSmaller:
            nums = testInputs[0]
            target = testInputs[1]
            expectedResult = testInputs[2]
            self.assertEqual(self.search.firstNotSmaller(nums, target), expectedResult, "testFirstNotSmaller | {}".format(testInputs))

    def testFirstOccurrence(self):

        testSetFirstOccurrence = [
            ([], 5, -1),
            ([1,2,2,3,4,5,6,7], 2, 1),
            ([1,2,3,4,5,6,7,8],8,7),
            ([0,1,2,3], 5, -1),
            ([0,1,2,3], -1, -1)
        ]

        for testInputs in testSetFirstOccurrence:
            nums = testInputs[0]
            target = testInputs[1]
            expectedResult = testInputs[2]
            self.assertEqual(self.search.firstOccurrence(nums, target), expectedResult, "testFirstOccurrence | {}".format(testInputs))

    def testSquareRoot(self):

        testSetSquareRoot = [
            (0,0),
            (8,2),
            (10,3),
            (1,1)
        ]

        for inputs in testSetSquareRoot:
            target = inputs[0]
            expected = inputs[1]
            self.assertEqual(self.search.squareRoot(target),expected,"testSquareRoot | {}".format(inputs))

    def testMinSortedRotatedArray(self):

        testSetMinSortedRotatedArray = [
            ([], -1 * sys.maxsize),
            ([2,1], 1),
            ([10,20,30,2], 3),
            ([-10, 0, 10, -20], 3)
        ]

        for inputs in testSetMinSortedRotatedArray:
            nums = inputs[0]
            expected = inputs[1]
            self.assertEqual(self.search.minSortedRotatedArray(nums), expected, "testMinSortedRotatedArray | {}".format(inputs))

    def testMountainPeak(self):

        print(threading.current_thread().getName())

        testSetMountainPeak = [
            ([0,1,2,3,1],3),
            ([0,1,0],1),
            ([1,10,2,1],1),
            ([0, 1, 2, 3, 2, 1, 0], 3),
            ([0, 10, 3, 2, 1, 0],1),
            ([0, 10, 0],1)
        ]

        for inputs in testSetMountainPeak:
            nums = inputs[0]
            expected = inputs[1]
            self.assertEqual(self.search.mountainPeak(nums), expected, "testMountainPeak | {}".format(inputs))


    def tearDown(self):

        del self.search
        print("ALL TEST CASES PASSED")

    
if __name__ == "__main__":
    unittest.main()