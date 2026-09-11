from typing import List

class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        first = float('-inf')
        second = float('-inf')
        third = float('-inf')
        
        for num in nums: 
            if num == first or num == second or num == third:
                continue
            elif num > first: 
                third = second
                second = first
                first = num
            elif num < first and num > second:
                third = second
                second = num
            elif num < second and num > third: 
                third = num
            else: 
                continue
        if (third != float('-inf')) : return third
        else: return first
