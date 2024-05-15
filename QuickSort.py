#Quicksort es un algoritmo de divide y vencerás. Funciona así: se elige un elemento de la lista, llamado pivote, y 
# se reorganiza la lista de manera que todos los elementos menores al pivote estén a su izquierda y todos los mayores a su derecha. 
# uego, se aplica recursivamente esta operación a las sub-listas de elementos menores y mayores. Una vez que las sub-listas tienen menos de dos elementos, 
# se concatenan y se devuelve la lista completa. El pseudocódigo es el siguiente:
def quicksort(array):
    if len(array) < 2:
        return array  # Base case: arrays with 0 or 1 element are already “sorted.”
    else:
        pivot = array[0]  # Recursive case
        less = [i for i in array[1:] if i <= pivot]  # Sub-array of all the elements less than the pivot
        greater = [i for i in array[1:] if i > pivot]  # Sub-array of all the elements greater than the pivot
        return quicksort(less) + [pivot] + quicksort(greater)
print(quicksort([10, 5, 2, 3]))
