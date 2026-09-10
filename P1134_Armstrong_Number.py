class Solution:
    def isArmstrong(self, n: int) -> bool:
        power = len(str(n))
        total_sum = 0
        temp = n
        
        while temp != 0: 
            digit = temp % 10
            total_sum += digit ** power
            temp //= 10
            
        return total_sum == n