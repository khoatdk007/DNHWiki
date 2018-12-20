def selection_sort(arr=[]):
    n = len(arr)
    for i in range(n-1):
        min_idx = i
        for j in range(i+1, n):
            if (arr[j] < arr[min_idx]):
                min_idx = j
        if (min_idx != i):
            arr[min_idx], arr[i] = arr[i], arr[min_idx]

def print_array(arr=[]):
    for i in arr:
        print(i, end=" ")
    print()

my_array = [8, 4, 1, 3, 9, 2]
print_array(my_array)
selection_sort(my_array)
print_array(my_array)
