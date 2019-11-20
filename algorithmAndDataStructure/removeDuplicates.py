class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        """"删除排序数组中的重复项,对应leetecode地址:https://leetcode-cn.com/problems/remove-duplicates-from-sorted-array/solution/"""
        start_len = len(nums);
        if not nums or start_len < 2:
            return start_len;
        start = 0;
        now   = 1;
        while now < start_len:
            if nums[start] == nums[now]:
                now      += 1;
                continue;
            start += 1;
            nums[start] = nums[now];
            now   += 1;
        return start + 1;