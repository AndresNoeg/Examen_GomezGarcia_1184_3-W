# Examen_GomezGarcia_1184_3-W

print(" ")
print("Gomez Garcia Andres Noe: 1184")
print(" ")

#Define una clase llamada alumno con un funcion
class alumno:
    #Define una funcion llamada califas que nos dice si el alumno esta aprobado o reprobado
    def califa(n1,n2,n3):
        if n1<=5:
            print("Esta reprobado")
        else:
            print("Esta aprobado")

        if n2<=5:
            print("Esta reprobado")
        else:
            print("Esta aprobado")

        if n3<=5:
            print("Esta reprobado")
        else:
            print("Esta aprobado")
    
    #invoca la funcion con los valores dados 
    print(califa(5,7,10))

![image](https://github.com/user-attachments/assets/f953d467-640e-473b-ac27-ea2fa7e5859d)

![image](https://github.com/user-attachments/assets/c3ba2f28-de2a-43bb-af8a-5ff47c7318e7)


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

![image](https://github.com/user-attachments/assets/0ed3ee96-632c-4a3c-ad2f-4dab8573f98c)

![image](https://github.com/user-attachments/assets/946ceadb-ef80-40f5-bc8c-947cb3b74166)


print(" ")
print("Gomez Garcia Andres Noe: 1184")
print(" ")

#Define una clase con una funcion
class triangulos:
    #Define una funcion que dice si el triangulo es isoceles escaleno o equilatero
    def definicion(cateto1,cateto2,base):
        if cateto1==cateto2==base:
            print("Es un triangulo equilatero")
        elif cateto1==cateto2!=base:
            print("Es un triangulo isoceles")
        elif cateto1!=cateto2==base:
            print("Es un triangulo isoceles")
        elif cateto1!=cateto2!=base:
            print("Es un triangulo isoceles")
    
    print(definicion(12,12,12))
    print(" ")
    print(definicion(12,13,12))
    print(" ")
    print(definicion(12,13,14))

![image](https://github.com/user-attachments/assets/06d0109b-58cd-4199-96e5-11295f025927)

![image](https://github.com/user-attachments/assets/9ec3f152-3437-460b-b824-5a36fbe974e5)











