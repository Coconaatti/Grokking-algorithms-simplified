def findSmallest(list):
  smallest = list[0]
  for i in range(1,len(list)):
    if arr[i] < smallest:
      smallest = arr[i]
      smallest_index = i
  return smallest_index
  
def selectionSort(arr):
  newArr = []
  modArr = list(arr)
  for i in range(len(modArr)):
    smallest = findSmallest(compiedArr)
    newArr.append(copiedArr.pop(smallest))
  return smallest
      
