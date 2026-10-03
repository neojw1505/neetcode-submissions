class FreqStack:

    def __init__(self):
        self.max_freq = 0
        self.count = collections.defaultdict(int) # num -> freq 
        self.stacks = collections.defaultdict(list) # freq -> list of nums with that freq

    def push(self, val: int) -> None:
        self.count[val] += 1 # increment count
        self.stacks[self.count[val]].append(val) # append val for this new freq
        if self.count[val] > self.max_freq: # update max_freq 
            self.max_freq = self.count[val]
        
    def pop(self) -> int:
        most_freq_recent_val = self.stacks[self.max_freq].pop()
        self.count[most_freq_recent_val] -= 1 # decrement cause pop 
        if not self.stacks[self.max_freq]:
            self.max_freq -= 1

        return most_freq_recent_val     


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()