def es_palindromo(cadena):
    return cadena == cadena[::-1]

cadena = input("Ingresa un palindromo:")
resultado = es_palindromo(cadena)
print(f"¿'{cadena}' es un palíndromo? {resultado}")
