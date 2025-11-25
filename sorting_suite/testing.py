from sorting import (
    swap,
    is_sorted,
    reverse,
    selection_sort,
    shell_sort,
    heap_sort,
    insertion_sort,
    bogo_sort,
    merge_sort,
    quick_sort,
    bubble_sort,
    bucket_sort,
    comb_sort
)

def test_sorting_functions():
    test_cases = [
        [],
        [1],
        [2, 1],
        [4, 2, 7, 1, 3],
        [5, 3, 8, 5, 2, 2, 9],
        [1, 2, 3, 4, 5],   
        [5, 4, 3, 2, 1], 
        [435, 2, 1090, 123, 345, 24, 45, -1204],
        [-90, -1, 0, 32, -4],
        [-1],
        [1, 1, 2, 0, 1, 1, 1, 2, 0, 1]  
    ]

    sorting_functions = [
        selection_sort,
        insertion_sort,
        shell_sort,
        heap_sort,
        merge_sort,
        quick_sort,
        bubble_sort,
        bucket_sort,
        bogo_sort,
        comb_sort
    ]

    for func in sorting_functions:
        print(f"\nTesting {func.__name__}:")
        for arr in test_cases:
            if func == bogo_sort and len(arr) > 3:
                continue
            result = func(arr)
            print(f"Input: {arr} -> Output: {result} -> Sorted: {is_sorted(result)}")

def test_utilities():
    print("\nTesting utility functions:")
    
    arr = [4,5,6]
    swap(arr, 0, 2)
    print(f"swap([4,5,6],0,2) -> ({arr})")

    arr = [1,2,3]
    print(f"reverse([1,2,3]) -> {reverse(arr)}")
    print(f"is_sorted([1,2,3]) -> {is_sorted([1,2,3])}")
    print(f"is_sorted([3,1,2]) -> {is_sorted([3,1,2])}")

if __name__ == "__main__":
    test_sorting_functions()
    test_utilities()