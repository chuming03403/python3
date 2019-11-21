class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        https://leetcode-cn.com/problems/rotate-array
        """
        leng = len(nums);
        k %= leng;
        loop_time = current = start = 0;
        while True:
            if loop_time >= leng:
                break;  
            num = nums[current];
            while True:
                current = (current + k) % leng;
                temp = num;
                num = nums[current];
                nums[current] = temp;
                loop_time += 1;
                if current == start:
                    break;
            start += 1;
            current = start;
        return True;