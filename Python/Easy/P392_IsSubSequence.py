class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        
        lenS = len(s)
        lenT = len(t)

        if s == '': return True
        if lenS > lenT: return False

        j = 0
        for i in range(lenT):
            if t[i] == s[j]:
                if j == lenS - 1:
                    return True
                j+=1
        return False
    
# Time: O(T)
# Space: O(1)
            
s = Solution()
print(s.isSubsequence("axc", "ahbgdc"))