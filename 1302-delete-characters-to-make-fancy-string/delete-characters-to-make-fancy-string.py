class Solution:
    def makeFancyString(self, s: str) -> str:
        res = []
        for char in s:
            if len(res) >= 2 and res[-1] == res[-2] == char:
                pass
            else:
                res.append(char)
        return "".join(res)        