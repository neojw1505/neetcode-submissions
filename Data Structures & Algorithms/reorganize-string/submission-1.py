class Solution:
    def reorganizeString(self, s: str) -> str:
        freqMap = Counter(s)
        maxHeap = []
        for char, cnt in freqMap.items():
            maxHeap.append((-cnt, char))
        heapq.heapify(maxHeap)

        res = []

        while len(maxHeap) >= 2:
            first_cnt, first_char = heapq.heappop(maxHeap) 
            second_cnt, second_char = heapq.heappop(maxHeap) 

            res.append(first_char)
            res.append(second_char)

            first_cnt += 1
            second_cnt += 1

            if first_cnt < 0:
                heapq.heappush(maxHeap, (first_cnt,first_char))
            if second_cnt < 0:
                heapq.heappush(maxHeap, (second_cnt,second_char))
            
        if maxHeap:
            cnt, char = heapq.heappop(maxHeap)
            if cnt < -1 or (res and char == res[-1]):
                return ""
            else:
                res.append(char)
        
        return ''.join(res)