def findLocalMinimum(start, end, array):
   #print(1, start, end)
   minimum = array[start]
   index = start
   #print(start,end)
   for i in range(start+1, end):
      if(array[i] < array[index]):
         minimum = array[i]
         index = i

   return (minimum, index) 	

def selectionSortG(array):
   for i in range(len(array)):
      minimum, index = findLocalMinimum(i, len(array), array)
      temp = array[i]
      array[i] = minimum
      array[index] = temp
   print(array)


print('Enter elements of array: ')
array = [int(i) for i in input().split()]
arrayG = [int(i) for i in array]
print("-------INPUT ARRAY----------")
print(arrayG)
print("------SORTED ARRAY AFTER GREEDY SELECTION SORT------")
selectionSortG(arrayG)
