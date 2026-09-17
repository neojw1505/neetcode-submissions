class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_freq_map = collections.Counter(nums)
        freq_idx_num_list_value = [[] for _ in range(len(nums)+1)]

        for num, freq in num_freq_map.items():
            freq_idx_num_list_value[freq].append(num)
        
        res = []
        for i in range(len(nums),0,-1):
            if freq_idx_num_list_value[i]:
                for num in freq_idx_num_list_value[i]:
                    res.append(num)
                    if len(res) == k:
                        return res
                