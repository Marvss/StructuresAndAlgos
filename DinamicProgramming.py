#Dinamic programming es una técnica de optimización que consiste en dividir un problema en subproblemas más pequeños y resolver estos subproblemas solo una vez. 
# Luego, los resultados se almacenan en una tabla para que puedan ser reutilizados más tarde, este se usa para problemas de optimización y problemas de conteo.
def fibonacci_recursive(n):
    if n <= 1:
        return n
    else:
        return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)


# Example usage
print(fibonacci_recursive(10))  # Output: 55
