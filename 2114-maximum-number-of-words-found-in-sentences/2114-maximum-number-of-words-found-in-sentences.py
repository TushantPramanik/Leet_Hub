class Solution:
    def mostWordsFound(self, sentences: list[str]) -> int:
        long=sentences[0].split()
        for i in range(1,len(sentences)):
            cur=sentences[i].split()
            if len(cur)>len(long):
                long=cur
        return len(long)        