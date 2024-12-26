class Solution:
    def reverseVowels(self, s: str) -> str:
        
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        v_list = [i for i in s if i in vowels]
        pointer = -1
        reversed_vowels = ""
        for i in range(len(s)):
            if s[i] in vowels:
                reversed_vowels+=v_list[pointer]
                pointer-=1 
            else:
                reversed_vowels+= s[i]

        return reversed_vowels    
sol = Solution()
print(sol.reverseVowels("hello"))