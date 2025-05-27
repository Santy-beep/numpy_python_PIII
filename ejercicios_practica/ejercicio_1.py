# Numpy [Python]
# Ejercicios de práctica

# Autor: Ing.Jesús Matías R.González
# Version: 2.0

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

# Ejercicios con lambda


if __name__ == '__main__':
    print("Bienvenidos a otra clase de Python")
    
    # Lambda expression
    # 1)
    # Realizar una funcion lambda que eleve al cuadrado
    # el número pasado como parámetro

    potencia_2 = lambda x: 2**x
    # pot_3 = potencia_2(3)

    # 2)
    # Utilice la función map para mapear una lambda expression
    # que retorne la potencia de 2 de cada numero en la lista numeros
    # El resultado (la potencia de cada numero) se debe ir almacenando
    # en una nueva lista
    numeros = [1, -5, 4, 3]
    numeros_abs = list(map(abs, numeros))
    print(numeros_abs)
    numeros_potenciados = list(map(potencia_2, numeros))
    
    numeros.append(numeros_potenciados)
    print(numeros_potenciados)
    # Nota: realizar la lambda expression "in line", es decir,
    # no declarar la lambda fuera del map sino diretamente dentro
    # Copiar la lambda creada en el paso anterior dentro del map
    # NOTA: No debe usar "potencia_2" dentro del map, debe colocar
    # directamente la lambda.

 
