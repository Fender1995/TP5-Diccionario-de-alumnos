from os import system
def cargar():
    a={}
    print("Carga de un alumno\n")
    
    a["nombre"]=input("ingrese nombre: ")
    a["apellido"]=input("ingrese apellido: ")
    a["dni"]=int(input("ingrese dni: "))
    a["fecha de nacimiento"]=input("ingrese fecha de nacimiento: ")
    a["tutor"]=input("ingrese nombre de tutor: ")
    a["faltas"]=int(input("ingrese catntidad de faltas: "))
    a["amonestaciones"]=int(input("ingrese cantidad de amonestaciones: "))
    a["notas"]=cargarNotas()
    return a

def mostrar(diccionario):
    print("nombre",diccionario["nombre"])
    print("apellido",diccionario["apellido"])
    print("dni",diccionario["dni"])
    print("fecha de nacimiento",diccionario["fecha de nacimiento"])
    print("tutor",diccionario["tutor"])
    print("faltas",diccionario["faltas"])
    print("amonestaciones",diccionario["amonestaciones"])
    print("Notas:\n")
    mostrarNotas(diccionario["notas"])



def agregar(alumnos,nuevoAlumno):
    print(alumnos)
    alumnos.append(nuevoAlumno)
    
    
def cargarmuchos():
    alumnos=[]
    b=1
    while(b==1):
        alumno=cargar()
        b=int(input("Desea seguir cargando?\n ingrese\n 0 para no y 1 para si." ))
        agregar(alumnos,alumno)
    return alumnos
def cargarNotas():
    notas={}
    b=1
    while(b==1):
        materia=input("ingrese nombre de la materia: ")
        nota=int(input("ingrese nota de la materia: "))
        notas[materia]=nota
        b=int(input("desea seguir ingresando materia para el alumno?\n ingrese\n 0 para no y 1 para si."))
    return notas

def mostrarNotas(notas):
    print("notas")
    for clave,valor in notas.items():
        print(clave+":",valor)
        
def mostraralumnos(alumnos):
    if len(alumnos)>0:
         for alumno in alumnos:
            mostrar(alumno)
    else:
        print("no hay alumnos")
       
def menu(datos):

    rta=0
    while(rta>=0 and rta<=5):
        print("1. Cargar alumno")
        print("2. Modificar alumno")
        print("3. Expulsar alumno")
        print("0. Salir")
        print("4. mostrar alumnos")
        print("5. mostrar todos los alumnos")
        rta=int(input("ingrese el número de la opción deseada"))
        if(rta==1):
            nuevoAlumno=cargar()
            agregar(datos["alumnos"],nuevoAlumno)
        elif(rta==2):
            system("cls")
            modificaralumno(datos)
        elif(rta==3):
            expulsar(datos)
        elif(rta==4):
            dni=input("ingrese dni del alumno:")
            alumnos=buscar(datos["alumnos"],dni)
            mostrar(datos["alumnos"][alumnos])
        elif(rta==5):
            mostraralumnos(datos["alumnos"])
        else:
            exit()
        
        
def buscar(alumnos,dni):
     i=0
     while(i<len(alumnos) and int(alumnos[i]["dni"])!=int(dni)):
        i=i+1
    
     if(i<len(alumnos)):
        return i
     else:
        return-1
       
def modificaralumno(datos):
    rta=0
    while(rta>=0 and rta<=9):
        print("1. nombre")
        print("2. apellido")
        print("3. dni")
        print("4. fecha de nacimiento")
        print("5. tutor")
        print("6. faltas")
        print("7. amonestaciones")
        print("8. notas")
        print("9. salir")
        rta=int(input("ingrese la opción deseada"))
        
        
        if(rta==1):
                dni=input("ingrese el dni del alumno que desea modificar: ")
                posicion=buscar(datos["alumnos"], dni)
                if posicion>-1:
                    datos["alumnos"][posicion]["nombre"]=input("ingrese el nombre nuevo")
                else:
                    print("elalumno no se encontro")

        elif(rta==2):
                dni=input("ingrese el dni del alumno que desea modificar: ")
                posicion=buscar(datos["alumnos"], dni)
                if posicion>-1:
                    datos["alumnos"][posicion]["apellido"]=input("ingrese el apellido nuevo")
                else:
                    print("elalumno no se encontro")
        elif(rta==3):    
                dni=input("ingrese el dni del alumno que desea modificar: ")
                posicion=buscar(datos["alumnos"], dni)
                if posicion>-1:
                    datos["alumnos"][posicion]["dni"]=input("ingrese el dni nuevo")
                else:
                    print("elalumno no se encontro")
        elif(rta==4):
                dni=input("ingrese el dni del alumno que desea modificar: ")
                posicion=buscar(datos["alumnos"], dni)
                if posicion>-1:
                    datos["alumnos"][posicion]["fecha de nacimiento"]=input("ingrese fecha de nacimiento nuevo")
                else:
                    print("elalumno no se encontro")
        elif(rta==5):
                dni=input("ingrese el dni del alumno que desea modificar: ")
                posicion=buscar(datos["alumnos"], dni)
                if posicion>-1:
                    datos["alumnos"][posicion]["tutor"]=input("ingrese el nombre de tutor nuevo")
                else:
                    print("elalumno no se encontro")
        elif(rta==6):
                dni=input("ingrese el dni del alumno que desea modificar: ")
                posicion=buscar(datos["alumnos"], dni)
                if posicion>-1:
                    datos["alumnos"][posicion]["faltas"]=input("ingrese las faltas")
                else:
                    print("elalumno no se encontro")
        elif(rta==7):
                dni=input("ingrese el dni del alumno que desea modificar: ")
                posicion=buscar(datos["alumnos"], dni)
                if posicion>-1:
                    datos["alumnos"][posicion]["amonestaciones"]=input("ingrese las amonestaciones")
                else:
                    print("elalumno no se encontro")
        elif(rta==8):
                dni=input("ingrese el dni del alumno que desea modificar: ")
                posicion=buscar(datos["alumnos"], dni)
                if posicion>-1:
                    menunotas(datos["alumnos"][posicion]["notas"])
                    
                else:
                    print("elalumno no se encontro")
        elif(rta==9):
                menu(datos)
        
    
def menunotas(notas):
     i=0
     for materia in notas.keys():
        i=i+1
        print(str(i)+" "+materia)
     rta=input("ingrese el nombre de la materia que desea modificar")
     notas[rta]=input("ingrese la nueva nota:")
    
    
def expulsar(datos):
       alumno=input("ingrese el número de DNI del alumno que desea expulsar")
       posicion=buscar(datos["alumnos"],alumno)
       print(posicion)
       datos["alumnos"].pop(posicion)
            

datos={"alumnos":[]}
menu(datos)


