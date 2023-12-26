def merge_sort(arr):
    if len(arr)>1:
        left_arr = arr[:len(arr)//2]
        right_arr = arr[len(arr)//2:]
        merge_sort(left_arr)
        merge_sort(right_arr)
        i = j = k = 0 # merged array index
        while i < len(left_arr) and j < len(right_arr):
            if left_arr[i] < right_arr[j]:
                arr[k] = left_arr[i]
                i = i+1
            else:
                arr[k] = right_arr[j]
                j = j + 1
            k = k+1

        while i < len(left_arr):
            arr[k] = left_arr[i]
            i = i+1
            k = k+1
        while j < len(right_arr):
            arr[k] = right_arr[j]
            j = j + 1
            k = k + 1

arr_test = [2,3,6,9,4,5,7,45,6,8,64,34,45,3435]
merge_sort(arr_test)
print(arr_test)
