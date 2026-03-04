import random

def partition_lomuto(arr,low,high):
    # схема Ломуто: pivot это последний элемент
    pivot=arr[high]
    i=low-1
    # проходим по массиву и переносим элементы <=pivot в левую часть
    for j in range(low,high):
        if arr[j]<=pivot:
            i+=1
            arr[i],arr[j]=arr[j],arr[i]
    # ставим pivot между двумя частями
    p=i+1
    arr[p],arr[high]=arr[high],arr[p]
    return p
  
def quick_sort(arr,low=0,high=None):
    if high is None:
        high=len(arr)-1
      
    if low<high:
        # рандомизация pivot
        pivot_index=random.randint(low,high)
        arr[pivot_index],arr[high]=arr[high],arr[pivot_index]
        # разбиение массива
        p=partition_lomuto(arr,low,high)
        # рекурсивная сортировка частей
        quick_sort(arr,low,p-1)
        quick_sort(arr,p+1,high)
