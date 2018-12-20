def easy_sort(arr=[]):
    n = len(arr)
    for i in range(n-1):
        for j in range(i+1, n):
            if (arr[i]>arr[j]):
                arr[i], arr[j] = arr[j], arr[i] # swap two elements
def print_array(arr=[]):
    for i in arr:
        print(i, end=" ")
    print()

my_array = [8, 4, 1, 3, 9, 2]
print_array(my_array)
easy_sort(my_array)
print_array(my_array)