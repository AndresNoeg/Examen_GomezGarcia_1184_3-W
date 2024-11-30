print(" ")
print("Gomez Garcia Andres Noe: 1184")
print(" ")

class calculadora:
    def inicio(self, n1, n2):  
        def suma():
            r = n1 + n2
            return r
        def resta():
            r = n1 - n2
            return r
        def multiplicacion():  
            r = n1 * n2
            return r
        def division():
            if n2 != 0:  # Para evitar la división por cero
                r = n1 / n2
                return r
            else:
                print("Error: División por cero") 
        
        # Mostrar los resultados de las operaciones
        return suma(), resta(), multiplicacion(), division()

# Crear una instancia de la clase y llamar al método inicio
calc = calculadora()
resultados = calc.inicio(55, 10)

# Mostrar los resultados
print("Suma: ", resultados[0])
print("Resta:", resultados[1])
print("Multiplicación:", resultados[2])
print("División:", resultados[3])

        

    
        
    

   
   
        