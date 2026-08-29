from collections import Counter
class Solution:
    def reorganizeString(self, s: str) -> str:
        # setup for maxHeap
        freqMap = Counter(s)
        maxHeap = []
        for char,count in freqMap.items():
            maxHeap.append((-count,char))
        heapq.heapify(maxHeap)

        res = [] # string builder to store chars
        while len(maxHeap) >= 2:
            # pop 2 at once
            first_count,first_char = heapq.heappop(maxHeap)
            second_count,second_char = heapq.heappop(maxHeap)

            res.append(first_char)
            res.append(second_char)

            # update counter - maxHeap should increase count
            first_count += 1
            second_count += 1

            # push back to heap, don't push back if count already 0
            if first_count < 0: 
                heapq.heappush(maxHeap, (first_count, first_char))
            
            if second_count < 0:
                heapq.heappush(maxHeap,(second_count, second_char))
        
        # check if maxHeap still got 1 item
        if maxHeap:
            # still got char(s)
                # 1. need to check if more than 1 char, cnt more than 1 sure fail
                # 2. need to check if char is same as last pushed
            count, char = heapq.heappop(maxHeap)
            if count < -1 or char == res[-1]:
                return ""
            else:
                res.append(char)
        return "".join(res)




