class Solution:
    def maxFreqSum(self, s: str) -> int:
        c = Counter(s)
        vowelsSet = ["a","e","i","o","u"] 
        vowels = [ ] 
        cons = []      

        for key, val in c.items():
            if key in vowelsSet:
                vowels.append(val)
            else:
                cons.append(val)

        
        if vowels:
            a = max(vowels)
        else:
            a = 0
        if cons:
            b = max(cons)
        else:
            b = 0
        return a + b
         