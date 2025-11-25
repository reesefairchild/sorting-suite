# Swaps arr[i] and arr[j]
# Runtime: O(1)
def swap(arr, i, j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp

# Checks if a list is sorted
# Runtime: O(n)
def is_sorted(arr):
    if not arr:
        return True
    return all(arr[i] <= arr[i + 1] for i in range(len(arr) - 1))

# Reverses a list
# Call on a sorted list to reverse the sorting order
# Runtime: O(n)
def reverse(arr):
    return arr[::-1]

# Sorts by "bubbling" large elements up into the correct spots
# Stable
# Runtime: O(n^2)
def bubble_sort(arr):
    arr = arr.copy()
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr    

# Sorts by picking pivots, partioning the list into sections, and recursively sorting the parts
# Runtime: O(n^2)
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    mid  = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + mid + quick_sort(right)

# Sorts by inserting elements into the correct order one at a time
# Stable
# Runtime: O(n^2)
def insertion_sort(arr):
    arr = arr.copy()
    for i in range(1,len(arr)):
        k = arr[i]
        j = i - 1

        while j >= 0 and arr[j] > k:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = k
    return arr

# Sorts by finding the next smallest elements and placing at front
# Runtime: O(n^2)
def selection_sort(arr):
    arr = arr.copy()
    n = len(arr)
    for i in range(n):
        min_inx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_inx]:
                min_inx = j
        arr[i], arr[min_inx] = arr[min_inx], arr[i]
    return arr

# Sorts by spliting the list in half and recursively sorting
# Stable
# Runtime: O(nlog(n))
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    
    return _merge(left, right)

def _merge(left, right):
    i = j = 0
    result = []
    
    while i < len(left) and j < len(right):
        if left[i] <= right[j]: 
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    return result + left[i:] + right[j:]

# Sorts by randomizing the list order and checking if the list is sorted
# Runtime: O(inf)
def bogo_sort(arr):
    import random
    arr = arr.copy()
    while not is_sorted(arr):
        random.shuffle(arr)
    return arr

# Sorts by sorting into buckets, sorting the buckets, and concatenating
# Stable
# Runtime: O(n+k), where k is number of buckets
def bucket_sort(arr, bucket_size=10):
    if len(arr) == 0:
        return arr
    arr = arr.copy()
    min_val, max_val = min(arr), max(arr)
    bucket_count = (max_val - min_val) // bucket_size + 1
    buckets = [[] for _ in range(bucket_count)]

    for num in arr:
        index = (num - min_val) // bucket_size
        buckets[index].append(num)

    sorted_arr = []
    for bucket in buckets:
        sorted_arr.extend(insertion_sort(bucket)) 

    return sorted_arr

# Sorts by comparing far apart elements and moving them
# Runtime: O(n^2)
def shell_sort(arr):
    arr = arr.copy()
    n = len(arr)
    gap = n // 2
    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp
        gap //= 2
    return arr

# Sorts by taking advantage of binary sequences
# Runtime: O(log^2(n))
def bitonic_sort(arr):
    n = len(arr)
    for k in range(2, n+1):
        j = k // 2
        while j > 0:
            for i in range(0, n):
                l = i ^ j
                if l > i:
                    if ( ((i&k)==0) and (arr[i] > arr[l]) or ( ( (i&k)!=0) and (arr[i] < arr[l])) ):
                        temp = arr[i]
                        arr[i] = arr[l]
                        arr[l] = temp
            j //= 2

# Sorts by using a binary min heap
# Runtime: O(log(n))
def heap_sort(arr):
    n = len(arr)

    for i in range(n//2, -1, -1):
      __heapify(arr, n, i)
    
    for i in range(n-1, 0, -1):
      arr[i], arr[0] = arr[0], arr[i]

      __heapify(arr, i, 0)

def __heapify(arr, n, i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2

    if l < n and arr[i] < arr[l]:
        largest = l

    if r < n and arr[largest] < arr[r]:
        largest = r

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        __heapify(arr, n, largest)

# Sorts similarly to bubble sort, but removes turtles
# Runtime: O(n^2)
def comb_sort(arr):
    n = len(arr)
    s = 1.3
    gap = n
    sorted = False

    while not sorted:
        gap = int(gap/s)
        if gap <= 1:
            sorted = True
            gap = 1

        for i in range(n-gap):
            sm = gap + i
            if arr[i] > arr[sm]:
                arr[i], arr[sm] = arr[sm], arr[i]
                sorted = False