class Solution:
    def frequencySort(self, s: str) -> str:
        mpp = Counter(s)
        res = ""
        for i,j in mpp.most_common():
            res += i*j
        return res
        