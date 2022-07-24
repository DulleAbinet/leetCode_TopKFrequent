class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        coun = Counter(nums)
        nw = []
        res =[]
        kw = list(coun.values())
        kw.sort(reverse = True)
        for i in range(k):
            nw.append(kw[i])
        for n in coun:
            if coun[n] in nw:
                res.append(n)
        return res
