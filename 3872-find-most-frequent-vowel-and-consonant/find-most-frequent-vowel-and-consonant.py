class Solution:
    def maxFreqSum(self, s: str) -> int:
        c = Counter(s)
        vowelsSet = ["a","e","i","o","u"] 
        vowels = [ val for key, val in c.items() if key in vowelsSet] 
        cons = [ val for key, val in c.items() if key not in vowelsSet]      
        
        if not vowels:
            return max(cons)
        elif not cons:
            return max(vowels)
        else:
            return max(cons) + max(vowels)
