import collections

class stack:

    ElementWithCachedMax = collections.namedtuple('ElementWithCachedMax', ('element', 'max'))

    def __init__(self):
        self._element_with_cached_max = []

    def is_empty(self):
        return len(self._element_with_cached_max) == 0
    
    def max(self):
        if self.is_empty():
            raise IndexError('max(): empty stack')
        return self._element_with_cached_max[-1].max


    # need to update this because probelem if the max is being deleted
    def pop(self):
        del self.stack[-1]
    
    # write this less pythonic
    def add(self, element):
        self._element_with_cached_max.append(
            self.ElementWithCachedMax(element, element if self.is_empty() else element, max(element, self.max()))
        )



s = stack()
s.add(2)
s.add(8)
s.add(5)
s.add(12)
m = s.max()
print(m)