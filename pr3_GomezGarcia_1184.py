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
    