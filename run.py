

from funciones import funciones
from cola import cola



#clase hospital
class hospital:

    def __init__(self):
        self.funciones = funciones()
        self.listaPacientes = cola()
        self.listaCodigoAzul = cola()
        self.listaUrgente = cola()
        self.listaNormal = cola()
        self.listaLeve = cola()
        self.registro = cola()
        self.laboratorio = cola()
        self.archivo_registro = open("informe.urgencias.txt", "w")

    #metodo para ingresar pacientes
    def entradaPacientes(self):
            self.archivo_registro.write("\n entrada de pacientes \n")
            paciente =  self.funciones.crearPacientes()
            self.listaPacientes.encolar(paciente)
            self.archivo_registro.write("Entro un paciente con nombre " + paciente.nombre + " " + paciente.apellido + " con cedula " + str(paciente.id) + " Peso " + str(paciente.peso) + "  y edad " + str(paciente.edad) + "\n" )

    #metodo para asignar triaje
    def asignarTriaje(self):
            if self.listaPacientes.esta_vacia() == False:
                paciente = self.listaPacientes.desencolar()
                self.funciones.Triaje(paciente, self.listaCodigoAzul, self.listaUrgente, self.listaNormal, self.listaLeve)
                self.archivo_registro.write("El paciente " + paciente.nombre + " " + paciente.apellido + " se le asigno " + paciente.codigoDeAtencion + "\n")

    #metodo de el proceso de atención
    def atencion(self,lista):
        paciente = lista.desencolar()
        paciente.asignarTratamiento(self.archivo_registro)
        salida = paciente.salida(self.archivo_registro)
        if salida == "Alta con medicamento":
            paciente.laboratorio(self.archivo_registro)
            self.laboratorio.apilar(paciente)
        else:
            self.registro.encolar(paciente)

    #metodo para atender pacientes
    def atenderpaciente(self):
            self.archivo_registro.write("\n atencion de pacientes\n")
            if not self.listaCodigoAzul.esta_vacia():
                self.atencion(self.listaCodigoAzul)
                return False

            elif not self.listaUrgente.esta_vacia():
                self.atencion(self.listaUrgente)
                return False

            elif not self.listaNormal.esta_vacia():
                self.atencion(self.listaNormal)
                return False


            elif not self.listaLeve.esta_vacia():
                self.atencion(self.listaLeve)
                return False

            elif self.listaUrgente.esta_vacia() and self.listaNormal.esta_vacia() and self.listaLeve.esta_vacia() and self.listaCodigoAzul.esta_vacia() and self.listaPacientes.esta_vacia():

                return True

    #metodo para atender laboratorio
    def atenderLaboratorio(self, f):

        if self.laboratorio.items == 10:
            self.archivo_registro.write(" \n se atiende el laboratorio por que llego a 10 solicitudes \n")

            for i in range(len(self.laboratorio.items)):
                paciente = self.laboratorio.desapilar()
                self.archivo_registro.write("el paciente " + paciente.nombre + " " + paciente.apellido + " se le dio el medicamento " + paciente.medicamentod + "\n")
                self.registro.encolar(paciente)
        elif f == True:
            for i in range(len(self.laboratorio.items)):
                paciente = self.laboratorio.desapilar()
                self.archivo_registro.write("el paciente " + paciente.nombre + " " + paciente.apellido + " se le dio el medicamento " + paciente.medicamentod + "\n")
                self.registro.encolar(paciente)


    #metodo para contar pacientes
    def cantidadPacientes(self,triaje,sortedregistro):
        contador = 0
        for i in sortedregistro:
            if i.codigoDeAtencion == triaje:
                contador = contador + 1
                print(i.salidad)
        print(f"la cantidad de pacientes con {triaje} es: {contador} \n")



    def Run (self, np):
        for i in range(0, np):
            self.entradaPacientes()
            self.asignarTriaje()
        f = False
        while f == False:
            f = self.atenderpaciente()
            self.atenderLaboratorio(f)
        self.atenderLaboratorio(f)

        print(f"Numero de pacientes ingresados: {np}")


        sortedregistro = sorted(self.registro.items, key=lambda x: x.prioridad)


        self.archivo_registro.write("\n \n registro de pacientes \n \n")

        for i in sortedregistro:

            self.archivo_registro.write(
                " \n el paciente " + i.nombre + " " + i.apellido + " con cedula " + str(i.id) + " Peso " + str(
                    i.peso) + "  y edad " + str(
                    i.edad) + " se le asigno " + i.codigoDeAtencion + " y se le dio " + i.tratamientod + " y se le dio de salida " + i.salidad + "\n")


        print("\n \n cantidad de pacientes con codigo azul en el registro \n \n")
        self.cantidadPacientes("Código Azul",sortedregistro)
        print("\n \n cantidad de pacientes con Estabilidad Urgente en el registro \n \n")
        self.cantidadPacientes("Estabilidad Urgente",sortedregistro)
        print("\n \n cantidad de pacientes con Urgencias Normales en el registro \n \n")
        self.cantidadPacientes("Urgencias Normales",sortedregistro)
        print("\n \n cantidad de pacientes con Urgencias Leves en el registro \n \n")
        self.cantidadPacientes("Urgencias Leves",sortedregistro)
        self.archivo_registro.close()

































