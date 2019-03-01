import simpy
import random
import statistics

CAPACITY = 1 #Capacidad de CPU
INSTRUCTIONS = 3  # Instruccciones que puede ejecutar el CPU por unidad de tiempo
MEMORY = 100  # Memoria RAM
PROCESS = 25  # Cantidad de procesos
INTERVAL = 10  # Intervalo de creacion de procesos
TOTALTIME = 0 # Tiempo total de ejecucion
TIMES = [] #Todos los tiempos
SEED = 8 #Semilla para random
random.seed(SEED)

for i in PROCESS:
    


env = simpy.Environment()
CPU = simpy.Resource(env, capacity= CAPACITY)
env.run()


