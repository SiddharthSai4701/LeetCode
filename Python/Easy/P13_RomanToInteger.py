class Solution:
   def romanToInt(self, s: str) -> int:  
    romanNumerals = {
        "M": 1000,
        "D": 500,
        "C": 100,
        "L": 50,
        "X": 10,
        "V": 5,
        "I": 1
    }

    integer = 0
    i = 0
    n = len(s)
    while(i <= n - 1):
        if i == n - 1:
            integer+= romanNumerals[s[i]]
            i+=1
        else:
            if romanNumerals[s[i]] >= romanNumerals[s[i+1]]:
                integer+= romanNumerals[s[i]]
                i+=1
            else:
                integer = integer + romanNumerals[s[i+1]] - romanNumerals[s[i]]
                i+=2
    
    return integer
 
