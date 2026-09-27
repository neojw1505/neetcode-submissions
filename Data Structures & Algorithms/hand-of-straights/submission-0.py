class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        n = len(hand)
        if n % groupSize: return False # cannot break into groupSize

        count = collections.Counter(hand)
        min_heap = list(count.keys())
        heapq.heapify(min_heap)

        while min_heap:
            # 1. Pop out elements whose counts already hit 0
            if count[min_heap[0]] == 0:
                heapq.heappop(min_heap)
                continue
            # 2. Form a consecutive group
            smallest = min_heap[0]
            for i in range(smallest, smallest + groupSize):
                if i not in count: return False  # Missing a card -> Fail!
                count[i] -= 1
                if count[i] == 0:
                    del count[i]
        return True
                