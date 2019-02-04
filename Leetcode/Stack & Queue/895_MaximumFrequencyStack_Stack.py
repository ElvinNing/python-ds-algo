import collections 

class FreqStack:
    ''' Leetcode 895. Maximum Frequency Stack'''
    def __init__(self):
        self._S = []
        self._frequency = collections.Counter()   
            # map from element to frequency
            # Counter() is built-in dict to count.
        self._element_stack = collections.defaultdict(list)
            # map from frequency to a list(stack) containing elements. 
            # The last element is the one to pop()
            # https://docs.python.org/3.7/library/collections.html#collections.defaultdict 
        self._maxfreq = 0

    def push(self, x):
        if isinstance(x, int):
            self._S.append(x) # unnecessary
            # try:
                # self._element_stack[self._frequency[x]].remove(x) # unnecessary.
            # except ValueError:
                # pass
            self._frequency[x] += 1 # better than self._frequency[x] = self._frequency.get(x,0) + 1 
            self._maxfreq = max(self._maxfreq, self._frequency[x])
            self._element_stack[self._frequency[x]].append(x) 
        # return (self._frequency[x], self._element_stack)

    def pop(self):
        max_freq_top = self._element_stack[self._maxfreq].pop()
        self._frequency[max_freq_top] -= 1
        if not self._element_stack[self._maxfreq]: # If there is another max frequency element
            self._maxfreq -= 1
        return max_freq_top
        


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(x)
# param_2 = obj.pop()
