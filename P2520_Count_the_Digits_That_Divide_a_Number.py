class Solution:
    def countDigits(self, num: int) -> int:
        temp = num
        count = 0
        while num > 0:
            last = num%10
            if temp % last == 0: count+=1
            num//=10
        return count