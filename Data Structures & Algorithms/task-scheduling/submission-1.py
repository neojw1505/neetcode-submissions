class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # init freq map
        task_freq = collections.Counter(tasks)
        # init max heap
        max_heap = [ [-freq, task] for task,freq in task_freq.items()]
        heapq.heapify(max_heap)
        # init cooldown queue
        cool_down_queue = collections.deque([])
        # init current running time
        curr_running_time = 0
        # start the processing
        while max_heap or cool_down_queue:
            curr_running_time += 1
            # check the maxheap
            if max_heap:
                neg_freq, task = heapq.heappop(max_heap)
                neg_freq += 1
                if neg_freq < 0:
                    release_time = curr_running_time + n
                    cool_down_queue.append([neg_freq, task, release_time])
            # check the cool_down_queue
            if cool_down_queue and cool_down_queue[0][2] == curr_running_time:
                neg_freq, task, release_time = cool_down_queue.popleft()
                heapq.heappush(max_heap, [neg_freq, task])
        return curr_running_time
