def bubble_sort(arr=[]):
    n = len(arr)
    for i in range(n-1):
        for j in range(n-i-1):
            if (arr[j] > arr[j+1]):
                arr[j], arr[j+1] = arr[j+1], arr[j] # swap two element

def print_array(arr=[]):
    for i in arr:
        print(i, end=" ")

my_array = [8, 4, 1, 3, 9, 2]
print_array(my_array)
print() # end line :))
bubble_sort(my_array)
print_array(my_array)
