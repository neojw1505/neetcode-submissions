class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        n = len(hand)
        if n % groupSize: return False

        count = collections.Counter(hand)
        min_heap = list(count.keys())
        heapq.heapify(min_heap)

        while min_heap:
            # 1. check if the top of min_heap count is 0
            if count[min_heap[0]] == 0:
                heapq.heappop(min_heap)
                continue
            # 2. build the groupSize, i = card_number
            for i in range(min_heap[0], min_heap[0] + groupSize):
                if i not in count:
                    return False
                count[i] -= 1
                if count[i] == 0:
                    del count[i]
        return True
