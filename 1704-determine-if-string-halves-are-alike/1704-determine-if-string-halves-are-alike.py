class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        a=""
        b=""
        c1=0
        c2=0
        for ch in range(len(s)):
            if ch<len(s)//2:
                a+=s[ch]
            else:
                b+=s[ch]

        for el in "aeiouAEIOU":
            if el in a:
                c1+=a.count(el)             
            if el in b:
                c2+=b.count(el)      

        return c1==c2

