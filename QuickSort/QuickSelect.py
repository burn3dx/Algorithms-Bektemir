import random

def quick_select(arr,k):
    low=0
    high=len(arr)-1
    while True:
        if low==high:
            return arr[low]
        pivot_index=random.randint(low,high)
        arr[pivot_index],arr[high]=arr[high],arr[pivot_index]
        p=partition_lomuto(arr,low,high)
        # проверяем позицию pivot
        if k==p:
            return arr[p]
        elif k<p:
            high=p-1
        else:
            low=p+1
