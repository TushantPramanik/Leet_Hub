class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        up=0
        low=0
        for i in range(len(word)-1,-1,-1):
            if word[i]>="A" and word[i]<="Z":
                up+=1
            elif word[i]>="a" and word[i]<="z":
                low+=1
        if up==len(word) or low==len(word):
            return True
        elif up==1 and low==len(word)-1 and word[0]>="A" and word[0]<="Z":   
            return True
        else:
            return False    