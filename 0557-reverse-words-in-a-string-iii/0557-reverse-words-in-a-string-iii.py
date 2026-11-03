class Solution:
    def reverseWords(self, s: str) -> str:
        l1 = s.split()
        l2=[]
        for el in l1:
            rev = el[::-1]
            l2.append(rev)
        s = " ".join(l2)    
        return s