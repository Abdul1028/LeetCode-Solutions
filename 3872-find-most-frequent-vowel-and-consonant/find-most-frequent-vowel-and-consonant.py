class Solution:
    def maxFreqSum(self, s: str) -> int:
        c = Counter(s)
        vowelsSet = ["a","e","i","o","u"] 
        vowels = [ val for key, val in c.items() if key in vowelsSet] 
        cons = [ val for key, val in c.items() if key not in vowelsSet]      

        # for key, val in c.items():
        #     if key in vowelsSet:
        #         vowels.append(val)
        #     else:
        #         cons.append(val)

        if not vowels:
            return max(cons)
        elif not cons:
            return max(vowels)
        else:
            return max(cons) + max(vowels)

        
        # if vowels:
        #     a = max(vowels)
        # else:
        #     a = 0
        # if cons:
        #     b = max(cons)
        # else:
        #     b = 0
        # return a + b
         