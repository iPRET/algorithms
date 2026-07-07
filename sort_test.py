import random

def single_test(func, arr):
  func_res = func(arr.copy())
  
  python_res = arr.copy()
  python_res.sort()
  
  if python_res != func_res:
    print("Problem encountered while testing:")
    print("Input: ", arr)
    print("Result:", func_res)
    print("Stopping testing.")
    exit()

def test_sort(func):
  """
  Checks whether function sorts various lists.
  """
  
  single_test(func, [])
  single_test(func, [1])
  single_test(func, [1, 2])
  single_test(func, [2, 1])

  single_test(func, [1, 2, 3, 4, 5, 6, 7])
  single_test(func, [1, 2, 3, 4, 5, 6, 7, 8])
  single_test(func, [1, 2, 3, 4, 5, 6, 7, 8, 9])
  
  single_test(func, [7, 6, 5, 4, 3, 2, 1])
  single_test(func, [8, 7, 6, 5, 4, 3, 2, 1])
  single_test(func, [9, 8, 7, 6, 5, 4, 3, 2, 1])
  
  single_test(func, [1, 1, 2, 2, 3, 3, 4, 4])
  single_test(func, [4, 4, 3, 3, 2, 2, 1, 1])
  single_test(func, [1] * 10)
  
  random.seed(42)
  for i in range(1000):
    test_len = random.randint(3, 16)
    numbers = [j for j in range(test_len)]
    random.shuffle(numbers)
    single_test(func, numbers)
  
  for i in range(1000):
    test_len = random.randint(3, 16)
    numbers = [random.randint(1, 5) for j in range(test_len)]
    single_test(func, numbers)
  
  print("Tests passed!")
    
if __name__ == "__main__":
  test_sort(sorted)