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


