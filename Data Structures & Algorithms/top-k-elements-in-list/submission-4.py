class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cnt = {}
        for num in nums:
            cnt[num]=1+cnt.get(num,0)
        
        hp = []
        for i in cnt.keys():
            heapq.heappush(hp,(cnt[i],i))
            if len(hp)>k:
                heapq.heappop(hp)
        
        res = []
        for i in range(k):
            res.append(heapq.heappop(hp)[1])
        return res