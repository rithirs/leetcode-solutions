class Solution:
    def secondHighest(self, s: str) -> int:
        largest = -1
        second_largest = -1
        
        for ch in s: 
            if ch.isdigit(): 
                val = int(ch)
                if val > largest:
                    second_largest = largest
                    largest = val
                elif val < largest and val > second_largest: 
                    second_largest = val
                else: continue
        return second_largest