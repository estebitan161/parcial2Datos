import random

from Paciente import Paciente

class funciones:



   #metodo para crear un paciente random
    def crearPacientes(self):
        edades = random.randint(15, 100)
        nombres = random.choice(["Juan", "María", "Carlos", "Ana", "Pedro", "Luis"])
        apellidos = random.choice(["González", "Pérez", "Martínez", "Fernández", "López", "Díaz"])
        idPaciente = random.randint(1000000000, 9999999999)
        peso = random.randint(50, 100)
        pacienteRandom = Paciente(nombres, apellidos, edades, peso, 0, idPaciente)
        return pacienteRandom

    #metodo para asignar triaje
    def Triaje(self, paciente, listaCodigoAzul, listaUrgente, listaNormal, listaLeve):
        paciente.asignarTriaje()
        if paciente.codigoDeAtencion == "Código Azul":
            paciente.prioridad = 1
            listaCodigoAzul.encolar(paciente)

        elif paciente.codigoDeAtencion == "Estabilidad Urgente":
            paciente.prioridad = 2

            listaUrgente.encolar(paciente)
        elif paciente.codigoDeAtencion == "Urgencias Normales":
            paciente.prioridad = 3

            listaNormal.encolar(paciente)
        elif paciente.codigoDeAtencion == "Urgencias Leves":
            paciente.prioridad = 4

            listaLeve.encolar(paciente)












