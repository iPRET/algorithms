import random
random.seed(42)

def quicksort_sort(arr, st = None, nd = None):
  if st is None:
    arr = arr.copy()
    quicksort_sort(arr, 0, len(arr))
    return arr
  
  if st + 1 >= nd:
    return
  
  piv = arr[random.randint(st, nd - 1)]
  l = st
  r = nd
  while l != r:
    if arr[l] < piv:
      l+= 1
    elif arr[l] > piv:
      arr[l], arr[r - 1] = arr[r - 1], arr[l]
      r-= 1
    else:
      if random.randint(0, 1) == 0:
        l+= 1
      else:
        arr[l], arr[r - 1] = arr[r - 1], arr[l]
        r-= 1
  
  quicksort_sort(arr, st, l)
  quicksort_sort(arr, l, nd)
  
  return


if __name__ == "__main__":
  import sort_test
  sort_test.test_sort(quicksort_sort)