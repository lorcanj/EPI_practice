import heapq

# O(n) space complexity
#O(n log n), because has to bubble up each time you add a smallest
# element because will swap log n times to reach the top and
# would do this n times if the numbers were in descending order
# not take advantage of the fact that the arrays are sorted
def merge_sorted_arrays(sorted_arrays):
    new = []
    for i in sorted_arrays:
        new.extend(i)
    heapq.heapify(new)
    li = []
    while new:
        li.append(heapq.heappop(new))
    return li


def m_sort_aray(sorted_arrays):
    min_heap = []
    sorted_arrays_iters = [iter(x) for x in sorted_arrays]

    #this puts the first element from each iterator in to the 
    for i, it in enumerate(sorted_arrays_iters):
        first_element = next(it, None)
        if first_element is not None:
            heapq.heappush(min_heap, (first_element, i))
        
    result = []
    
    while min_heap:
        smallest_entry, smallest_entry_index = heapq.heappop(min_heap)
        smallest_iter = sorted_arrays_iters[smallest_entry_index]
        
        result.append(smallest_entry)
        
        next_entry = next(smallest_iter, None)
        # check for the next entry
        # add to the min heap
        if next_entry is not None:
            heapq.heappush(min_heap, (next_entry, smallest_entry_index))
    return result

    # check while something is not none
    # pop the minimum from the heap to the start of the list
    # do next for the list which the minimum was taken from
    # add the next lowest number to the heap and heapify
    # pop off the lowest element

l = [[-1, 0], [-2], [-3, 4, 8]]
newli = m_sort_aray(l)
print(newli)
