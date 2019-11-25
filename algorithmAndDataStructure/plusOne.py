class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        """
        一个数组组成一个大整数，实现加一功能。
        https://leetcode-cn.com/problems/plus-one
        """
        leng = n = len(digits) - 1;
        while leng >= 0:
            if digits[leng] < 9:
                digits[leng] = digits[leng] + 1;
                return digits;
            else:
                digits[leng] = 0;
                leng -= 1;
        #此时，所有数据都为0，要进一位
        digits.insert(0, 1);
        return digits;