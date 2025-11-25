**sorting-suite** is a simple Python library providing a comprehensive collection of numerical sorting algorithms, along with helpful utility functions.  
---

## Sorting Algorithms by Average Runtime

**O(n + k)**
- Bucket Sort

**O(log^2 n)**
- Bitonic Sort (can only be used on lists with size that is multiple of 2)

**O(n log n)**
- Heap Sort
- Merge Sort
- Quick Sort
- Shell Sort

**O(n^2)**
- Bubble Sort
- Comb Sort
- Insertion Sort
- Selection Sort

**O(n!)**
- Bogo Sort (please do not use this one)

---

## Stable Sorts
- Bucket Sort
- Bubble Sort
- Insertion Sort
- Merge Sort

---

## Utility Functions

- **`swap(a, b)`** – Swap two elements.  
- **`is_sorted(arr)`** – Check if an array is sorted.  
- **`reverse(arr)`** – Reverse the elements of a list. Allows above sorting functions
to sort in descending order, if desired.

---

## Installation

```bash
pip install sorting-suite
