
num_alumnos = 0
nombre_alumno = " "
num_examenes = 0
nota_examenes = []
nota_trabajos = []
nota_ex = 0
nota_trab = 0
suma_examenes = 0
num_trabajos = 0
suma_trabajos = 0
nota_final = 0
contador = 0
nombre_nota = {}

def lee_entero():
    while True:
        valor = raw_input("Ingrese el numero de alumnos: ")
        try:
            valor = int(valor)
            return valor
        except ValueError:
            print "ATENCION: Debe ingresar un numero entero."

num_alumnos = lee_entero()
num_examenes = input("Numero de examenes hecho: ")
num_trabajos = input("Numero de trabajos realizados: ")

while contador != num_alumnos:
    nombre_alumno = raw_input("Nombre del alumno: ")
    for i in range(0, num_examenes):
        nota_ex = input("Introduce nota examen " + str(i+1) + ": ")
        nota_examenes.append(nota_ex)
        suma_examenes = suma_examenes + nota_examenes[i]

    porcentaje_examenes = (suma_examenes / float(num_examenes)) * 0.60
    print porcentaje_examenes

    for i in range(0, num_trabajos):
        nota_trab = input("Introduce nota trabajo " + str(i+1) + ": ")
        nota_trabajos.append(nota_trab)
        suma_trabajos = suma_trabajos + nota_trabajos[i]

    porcentaje_trabajos = (suma_trabajos / float(num_trabajos)) * 0.20

    print porcentaje_trabajos

    nota_libreta = 0
    nota_libreta = input("Nota de la libreta: ")

    porcentaje_libreta = nota_libreta * 0.20

    print (porcentaje_libreta)
    nota_final = porcentaje_libreta + porcentaje_examenes + porcentaje_trabajos
    print "Nota final: " + str(nota_final)
    nombre_nota[nombre_alumno] = nota_final

    for i in nota_examenes[:]:
        nota_examenes.remove(i)
    for i in nota_trabajos[:]:
        nota_trabajos.remove(i)
    nota_ex = 0
    nota_trab = 0
    suma_examenes = 0
    suma_trabajos = 0
    porcentaje_trabajos = 0
    porcentaje_examenes = 0
    nota_final = 0

    contador += 1
archivo = open("notas.txt", "w")
for key in nombre_nota:
    archivo.write(str(key) + ": " + str(nombre_nota[key]) + "\n\n")

archivo.close()
