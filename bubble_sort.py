def bubble_sort(arr: list) -> list:
  """
  Sorts an array with bubble sort.

  :param arr: List of items which can be compared with < >.
  :return: New sorted list.
  """
  arr = arr.copy()
  for i in range(len(arr) - 1):
    for j in range(0, len(arr) - 1 - i):
      if arr[j + 1] < arr[j]:
        arr[j], arr[j + 1] = arr[j + 1], arr[j]
  return arr

test = [5, 1, 7, 4, 3, 2, 6, 8, 9, 10]

print("Original:", test)
print("Sorted  :", bubble_sort(test))

