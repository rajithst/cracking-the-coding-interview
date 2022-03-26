from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:

        # time - O(nlog(n)), Space - O(1)
        sorted_nums = sorted(nums)
        for i in range(1, len(nums)):
            if sorted_nums[i] == sorted_nums[i - 1]:
                return True
        return False


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:

        # time - O(n), Space - O(n)
        mem = set()
        for num in nums:
            if num in mem:
                return True
            else:
                mem.add(num)
        return False
