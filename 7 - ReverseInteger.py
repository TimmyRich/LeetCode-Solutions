class Solution:
    def reverse(self, x: int) -> int:
        neg = 0
        if x < 0:
            neg = 1
            x = x * -1
            print(x)
        num = str(x)
        num = num[::-1]
        if int(num) > (2**31) - 1:
            return 0
        if neg:
            return int(num) * -1
        return int(num)
    
sol = Solution()
print(sol.reverse(-123))