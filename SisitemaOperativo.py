# Universidad del Valle de Guatemala
# Hoja de Trabajo 5
# Jose Miguel Castañeda 18161
# Silvio Orozco 18282
# 01-03-2019
import simpy
import random
import statistics

#Nuestro simulador del sistema operativo que une al CPU, RAM, Procesos y Simulador
def OperatingSystem(env,simulationTime,processName,simulationMemory,simulationInstructions,instructionsForTimeUnit):
    #Pasamos a la etapa New
    yield env.timeout(simulationTime)
    print("El %s utilizara %s de la memoria RAM"%(processName,simulationMemory))
    entranceTime = env.now
    #Pasamos a la etapa ready
    #Obtiene la memoria de nuestra RAM necesaria para el proceso
    yield RAMMemory.get(simulationMemory)
    print("/tSe ha obtenido la memoria %s en tiempo %s" %(simulationMemory,env.now))
    while simulationInstructions > 0:
        #Se realizan tres instrucciones
        simulationInstructions = simulationInstructions - INSTRUCTIONS
        yield env.timeout(1)
        #Pasamos a la etapa Waiting
        decision = random.randint(1,2)
        if decision == 2:
            with WAIT.request() as request:
                        yield request
                        yield env.timeout(1)      
        #Pasamos a la etapa Terminated
        yield RAMMemory.put(simulationMemory)
        print("/tSe ha regresado la memoria %s a la RAM en tiempo %s" %(simulationMemory,env.now))
        #Tiempo tardado para el proceso total
        ProcessTime= (env.now-entranceTime)
        #Se guarda el tiempo tardado del proceso para analisis de datos
        global TOTALTIME
        global TIMES
        TOTALTIME = TOTALTIME + ProcessTime
        TIMES.append(ProcessTime)

#constantes
CAPACITY = 1 #Capacidad de CPU
INSTRUCTIONS = 3  # Instruccciones que puede ejecutar el CPU por unidad de tiempo
MEMORY = 100  # Memoria RAM
PROCESS = 25  # Cantidad de procesos
INTERVAL = 10  # Intervalo de creacion de procesos
TOTALTIME = 0 # Tiempo total de ejecucion
TIMES = [] #Todos los tiempos
SEED = 8 #Semilla para random
random.seed(SEED)

#Creamos nuestro ambiente, nuestro CPU modelado como resource, RAMMemory modelado como Container y Wait
env = simpy.Environment()
CPU = simpy.Resource(env, capacity= CAPACITY)
RAMMemory = simpy.Container(env,init=MEMORY,capacity=MEMORY)
WAIT = simpy.Resource(env, capacity= CAPACITY)
    
#Main para la simulacion
def main():

    for i in range(PROCESS):
        simulationTime = random.expovariate(1.0/INTERVAL)
        simulationInstructions = random.randint(1,10)
        simulationMemory = random.randint(1,10)
        env.process(OperatingSystem(env,simulationTime,"Proceso %s" %i,simulationMemory,simulationInstructions,INSTRUCTIONS))
    env.run()
    
    MeanTime = float(TOTALTIME/PROCESS)
    StdevTime = statistics.stdev(TIMES)

    print("Procesos Terminados")
    print("El tiempo total para %s procesos fue de %.2f, el tiempo por proceso promedio fue de %.2f con desviacion estandar de %.2f" %(PROCESS, TOTALTIME,MeanTime ,StdevTime))

    
main()



