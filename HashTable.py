#un HashTable es una estructura de datos que implementa una matriz asociativa, una estructura que puede asignar claves a valores, de la manera que un diccionario lo hace.
cache = {}
def get_page(url):
 if cache.get(url):
  return cache[url] #Returns cached data
else:
    data = get_data_from_server(url)
 cache[url] = data Saves this data in your cache first
 return data