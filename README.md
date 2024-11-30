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

![image](https://github.com/user-attachments/assets/c5dfd3dd-a3bb-4bc9-b91c-bbbbdfab1d86)

![image](https://github.com/user-attachments/assets/64c201ff-186a-4bad-b8a6-02369abfaa63)

print(" ")
print("Gomez Garcia Andres Noe: 1184")
print(" ")
#DEfine una clase llamada agenda con varias funciones
class Agenda:
    #Funcion genera lista de los contactos
    def __init__(self):
        self.contactos = []

    # Añadir un nuevo contacto
    def añadir_contacto(self, nombre, telefono, email):
        self.contactos.append({"Nombre": nombre, "Teléfono": telefono, "Email": email})
        print(f"Contacto {nombre} añadido.")

    # Mostrar todos los contactos
    def lista_contactos(self):
        if not self.contactos:
            print("No hay contactos en la agenda.")
        else:
            for contacto in self.contactos:
                print(f"Nombre: {contacto['Nombre']}, Teléfono: {contacto['Teléfono']}, Email: {contacto['Email']}")

    # Buscar un contacto por nombre
    def buscar_contacto(self, nombre):
        for contacto in self.contactos:
            if contacto["Nombre"].lower() == nombre.lower():
                print(f"Encontrado: {contacto['Nombre']}, {contacto['Teléfono']}, {contacto['Email']}")
                return
        print("Contacto no encontrado.")

    # Editar un contacto por nombre
    def editar_contacto(self, nombre):
        for contacto in self.contactos:
            if contacto["Nombre"].lower() == nombre.lower():
                contacto["Nombre"] = input(f"Nuevo nombre para {nombre}: ")
                contacto["Teléfono"] = input(f"Nuevo teléfono para {nombre}: ")
                contacto["Email"] = input(f"Nuevo email para {nombre}: ")
                print(f"Contacto {nombre} editado.")
                return
        print("Contacto no encontrado.")

    # Mostrar el menú de opciones
    def mostrar_menu(self):
        while True:
            print("\n1. Añadir contacto")
            print("2. Lista de contactos")
            print("3. Buscar contacto")
            print("4. Editar contacto")
            print("5. Cerrar agenda")
            opcion = input("Elige una opción: ")

            if opcion == '1':
                nombre = input("Nombre: ")
                telefono = input("Teléfono: ")
                email = input("Email: ")
                self.añadir_contacto(nombre, telefono, email)
            elif opcion == '2':
                self.lista_contactos()
            elif opcion == '3':
                nombre = input("Nombre a buscar: ")
                self.buscar_contacto(nombre)
            elif opcion == '4':
                nombre = input("Nombre a editar: ")
                self.editar_contacto(nombre)
            elif opcion == '5':
                print("Cerrando agenda...")
                break
            else:
                print("Opción inválida.")

# Crea la agenda y muestra el menú
agenda = Agenda()
agenda.mostrar_menu()

![image](https://github.com/user-attachments/assets/e62359f9-e741-4093-b3c0-430dadb9187d)

![image](https://github.com/user-attachments/assets/babf8c3e-e3a2-4680-815f-31abaa61b676)

![image](https://github.com/user-attachments/assets/7aa86c18-f760-49d5-b74a-49d3bb79b0ec)

![image](https://github.com/user-attachments/assets/2c78572d-edc5-4ede-98e9-e89069cbf657)




















