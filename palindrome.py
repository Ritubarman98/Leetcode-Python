class Solution:
    def isPalindrome(self, x):
        string = str(x)
        string2 = string[::-1]
        if string == string2:
            return True
        else:
            return False

x = int(input())
s = Solution()
print(s.isPalindrome(x))