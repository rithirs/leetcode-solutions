# Time Complexity: O(log10(n))
# Space Complexity: O(1)

class Solution:
    def reverse(self, x: int) -> int:
        is_negative = False
        if x < 0:
            x = abs(x)
            is_negative = True
        temp = x
        rev = 0
        while temp > 0:
            last = temp % 10
            rev = rev * 10 + last
            temp //= 10
        if (is_negative == True): rev*=-1

        # 32-bit signed integer boundary check
        if rev < -2**31 or rev > 2**31 - 1: return 0
        else : return rev