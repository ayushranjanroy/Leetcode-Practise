class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        mpp = Counter(nums).most_common()
        mpp.sort(key = lambda x:x[0], reverse = True)
        mpp.sort(key = lambda x:x[1])
        
        res = []
        for i in mpp:
            a,b=i
            res.extend([a]*b)
        return res