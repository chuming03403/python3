class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        从一个数组中，找到两数之和为target，并返回这两个数的下标
        https://leetcode-cn.com/problems/two-sum
        """
        hashmap = {};
        for index, num in enumerate(nums):
            if hashmap.get(target - num) is not None:
                return [hashmap.get(target - num), index];
            hashmap[num] = index;
