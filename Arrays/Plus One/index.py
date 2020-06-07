class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        digits[-1] += 1
        i = -1
        while True:
            if digits[i] > 9:
                if len(digits) < abs(i-1):
                    digits.insert(0, 0)
                digits[i-1] = digits[i-1] + int(digits[i] // 10)
                digits[i] = digits[i] % 10
                i -= 1
            else:
                break
        return digits
