class Solution:
    def maximumWealth(self, accounts: list[list[int]]) -> int:
        m = sum(accounts[0])
        for i in range(1,len(accounts)):
            if sum(accounts[i]) > m:
                m = sum(accounts[i])
        return m        