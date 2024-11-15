from __future__ import absolute_import

class App:
    @staticmethod
    def add(a,b):
        return a+b

    def resta(a,b):
        return a-b

    def multiplicacion(a,b):
        return a*b

    def division(a,b):
        if b == 0:
            return 0
        else:
            return a/b

    # 1. Verifica si una lista contiene un número primo
    def contiene_numero_primo(lista):
        """
        Verifica si hay al menos un número primo en la lista.
        Retorna True si hay un número primo, de lo contrario, False.
        """
        for numero in lista:
            if numero > 1:
                es_primo = True
                for i in range(2, int(numero**0.5) + 1):
                    if numero % i == 0:
                        es_primo = False
                        break
                if es_primo:
                    return True
        return False

    # 2. Cuenta los números pares en un rango dado
    def contar_pares(inicio, fin):
        """
        Cuenta la cantidad de números pares en el rango desde 'inicio' hasta 'fin' (inclusive).
        Retorna la cantidad de números pares.
        """
        cont = 0
        for pares in range(inicio,fin+1):
            if(pares%2==0):
                cont+=1

        return cont

    # 3. Encuentra el número máximo en una lista que sea múltiplo de un valor dado
    def maximo_multiplo(lista, multiplo):
        """
        Encuentra y retorna el valor máximo de la lista que es múltiplo del parámetro 'multiplo'.
        Si no hay múltiplos, retorna None.
        """
        maximo = 0
        for maxmul in lista:
            if multiplo%maxmul == 0:
                maximo=maxmul
                
        if maximo == 0:
            return None
        else:
            return maximo
        

    # 4. Verifica si una palabra es palíndroma (se lee igual en ambos sentidos)
    def es_palindromo(palabra):
        """
        Verifica si la palabra es un palíndromo (igual al leerla al revés).
        Retorna True si es palíndromo, de lo contrario, False.
        """
        paspalabra = palabra.lower().replace(" ", "")
        return paspalabra == paspalabra[::-1]

    # 5. Calcula la suma de los primeros n números impares
    def suma_primeros_impares(n):
        """
        Calcula y retorna la suma de los primeros 'n' números impares.
        """
        suma = 0
        numero_actual = 1

        while n > 0:
            suma += numero_actual
            numero_actual += 2
            n -= 1

        return suma

    # 6. Verifica si todos los elementos de una lista son únicos
    def elementos_unicos(lista):
        """
        Verifica si todos los elementos de la lista son únicos.
        Retorna True si son únicos, de lo contrario, False.
        """
        esUnico = len(set(lista)) == len(lista)
        
        return esUnico

    # 7. Calcula el factorial de un número sin usar recursión
    def calcular_factorial(numero):
        """
        Calcula y retorna el factorial de 'numero' usando un ciclo.
        """
        factorial = 1
        for i in range(1, numero + 1):
            factorial = factorial * i
        return factorial

    # 8. Cuenta la cantidad de vocales en una cadena
    def contar_vocales(cadena):
        """
        Cuenta y retorna la cantidad de vocales en la cadena.
        """
        cadena_min = cadena.lower()
        vocales = "aeiou"
        contador = 0
        for letra in cadena_min:
            if letra in vocales:
                contador += 1
        return contador

    # 9. Encuentra el segundo número mayor en una lista
    def segundo_mayor(lista):
        """
        Encuentra y retorna el segundo número más grande en la lista.
        Si no existe, retorna None.
        """
        if len(lista) < 2:
            return None
        else:
          #Lista ordenada de menor a mayor
          lista_ordenada = sorted(lista)

          # El segundo número más grande es el último en la lista ordenada
          return lista_ordenada[-2]

    # 10. Calcula la serie de Fibonacci hasta n términos
    def fibonacci(n):
        """
        Genera y retorna una lista con los primeros 'n' términos de la serie de Fibonacci.
        """
        serie_fibonacci = [0, 1]
        for i in range(2, n):
            serie_fibonacci.append(serie_fibonacci[i - 1] + serie_fibonacci[i - 2])
        return serie_fibonacci
