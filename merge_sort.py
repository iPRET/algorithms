def merge_sort(arr: list) -> list:
  """
  :param arr: List of objects wher < and > work.
  :return: New sorted list.
  """
  if len(arr) <= 1:
    return arr
  else:
    result = []
    mid = len(arr) // 2
    arrl = merge_sort(arr[:mid])
    arrr = merge_sort(arr[mid:])
    l = 0
    r = 0
    for _ in range(len(arr)):
      if l == len(arrl):
        result.append(arrr[r])
        r+= 1
        continue
      elif r == len(arrr):
        result.append(arrl[l])
        l+= 1
      elif arrl[l] < arrr[r]:
        result.append(arrl[l])
        l+= 1
      else:
        result.append(arrr[r])
        r+= 1
    return result


test = [5, 1, 7, 4, 3, 2, 6, 8, 9, 10]

print("Original:", test)
print("Sorted  :", merge_sort(test))
      
