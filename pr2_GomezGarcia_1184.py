print(" ")
print("Gomez Garcia Andres Noe: 1184")
print(" ")

#Define una clase llamada persona con una funcion
class Persona:
    #Define una funcion llamada atributos que imprime nombre y edad y si la persona e mayor o menor de edad
    def atributos(nombre,edad):
        print("El nombre de la persona es: ", nombre)
        print("La edad de", nombre,"es: ", edad)

        if edad>=18:
            print(nombre, "es mayor de edad")
        else:
            print(nombre, "no es mayor de edad")
            return (nombre, edad)
    #Invoca la funcion con los datos dados
    print(atributos("Noe", 16))


    