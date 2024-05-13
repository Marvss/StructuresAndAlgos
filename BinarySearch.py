#La busqueda binaria es un algoritmo de busqueda eficiente que busca un item en una lista ordenada, 
#compara el item con el valor del medio de la lista y elimina la mitad en la que el item no puede estar en cada iteracion.
def binary_search(list, item):
 low = 0 
 high = len(list) - 1 

 while low <= high: 
  mid = (low + high)
  guess = list[mid]
  if guess == item:
   return mid
  if guess > item: 
   high = mid - 1
 else: 
  low = mid + 1
 return None 

my_list = [5, 3, 5, 7, 9]

print(binary_search(my_list, 3)) # => 1
print(binary_search(my_list, -1)) # => None