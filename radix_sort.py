def radix(arr):
  """
  Sorts an array using radix sort.
  
  :param arr: List of ints in range [0..2^32 - 1].
  :return: Sorted list of ints.
  """
  arr = arr.copy()
  
  radix1 = (1 << 16) - 1
  radix2 = (1 << 32) - (1 << 16)
  
  count = [0 for _ in range(1 << 16)]
  
  for num in arr:
    count[num & radix1]+= 1
  
  cumulative = [0]
  for c in count:
    cumulative.append(cumulative[-1] + c)
  
  tmparr = [0 for _ in arr]
  
  for num in arr:
    radix = num & radix1
    tmparr[cumulative[radix]] = num
    cumulative[radix]+= 1
  
  count = [0 for _ in range(1 << 16)]
  
  for num in tmparr:
    count[(num & radix2) >> 16]+= 1
  
  cumulative = [0]
  for c in count:
    cumulative.append(cumulative[-1] + c)
  
  for num in tmparr:
    radix = (num & radix2) >> 16
    arr[cumulative[radix]] = num
    cumulative[radix]+= 1
  
  return arr
  
  
if __name__ == "__main__":
  import sort_test
  sort_test.test_sort(radix)
