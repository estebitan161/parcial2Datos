

# clase paciente
import random

class Paciente:


    def __init__ (self,nombre,apellido, edad, peso, codigoDeAtencion, id):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.peso = peso
        self.codigoDeAtencion = codigoDeAtencion
        self.prioridad = 0
        self.id = id
        self.tratamientod = None
        self.salidad = None
        self.medicamentod= None




    def asignarTriaje(self):
        triaje = random.choice(["Código Azul", "Estabilidad Urgente", "Urgencias Normales", "Urgencias Leves"])
        self.codigoDeAtencion = triaje



    def asignarTratamiento(self,t):
        tratamientos = ["exámenes médicos", "pruebas diagnósticas ", "procedimientos curativos", "estabilización"]
        tratamiento = random.choice(tratamientos)
        t.write("el paciente " + self.nombre + " se le asignara " + tratamiento + "\n" )
        self.tratamientod = tratamiento

    def salida(self,t):
        salida = ["alta", "alta voluntaria", "hospitalizacion", "espeicialista", "morgue", "Alta con medicamento", "Alta voluntaria"]
        salidas = random.choice(salida)
        t.write("el paciente " + self.nombre + " se ira para: " + salidas + "\n" )
        self.salidad = salidas
        return salidas

    def laboratorio(self,t):
        medicamentos = ["acetaminofen", "ratalina", "ibuprofeno", "dolex", "paracetamol", "dexametasona","Aderall","Metametasona","Crotolamo"]
        medicamento = random.choice(medicamentos)
        t.write("el paciente " + self.nombre + " fue a el laboratorio y se le dara " + medicamento + "\n")
        t.write("\n")
        self.medicamentod = medicamento