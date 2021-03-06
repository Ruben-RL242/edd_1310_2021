from colas import Queue,BoundedPriorityQueue

q1 = Queue()
q1.enqueue(3)
q1.enqueue(33)
q1.enqueue(23)
print(q1.to_string())

print("Prueba 2 de Queue")
c1 = {"id":1 , "nombre": "Mario" , "balance": 20.5}
c2 = {"id":2 , "nombre": "Diana" , "balance": 3456.5}
c3 = {"id":3 , "nombre": "Mario" , "balance": 1000000.0}

atencion = Queue()
atencion.enqueue(c1)
atencion.enqueue(c2)
atencion.enqueue(c3)
print(atencion.to_string())
sig= atencion.dequeue()
print(f"Bienvenido sr. {sig['nombre']}, en que podemos servirle el dia de hoy?")
print(atencion.to_string())


print("=================Pruebas de las colas con prioridad acotada======================")
maestre = {"prioridad":4 , "descripción":"Maestre","persona":"juan P"}
ninos = {"prioridad":2 , "descripción":"Niños","personas":["Santi H","Ángel H"]}
mecanico = {"prioridad":4 , "descripción":"Mecánico","persona":"Mario Z"}
mujeres = {"prioridad":3 , "descripción":"Mujeres","personas":["Fernanda J","Simona la mona"]}
terceraEdad = {"prioridad":2 , "descripción":"3ra edad","personas":["Francisco M","Gloria L"]}
ninas = {"prioridad":1 , "descripción":"Niñas","personas":["Astrid R","Jimena F"]}
hombres = {"prioridad":3 , "descripción":"Hombres","personas":["Ruben RL","Rodolfo G"]}
vigia = {"prioridad":4 , "descripción":"Vigia","persona":"Yunque R"}
capitan = {"prioridad":5 , "descripción":"Capitan","persona":"Barbanegra f"}
timonel = {"prioridad":4 , "descripción":"Timonel","persona":"Smith K"}

cpa=BoundedPriorityQueue(7)
cpa.enqueue(maestre['prioridad'], maestre)
cpa.enqueue(ninos['prioridad'], ninos)
cpa.enqueue(mecanico['prioridad'], mecanico)
cpa.enqueue(mujeres['prioridad'], mujeres)
cpa.enqueue(terceraEdad['prioridad'], terceraEdad)
cpa.enqueue(ninas['prioridad'], ninas)
cpa.enqueue(hombres['prioridad'], hombres)
cpa.enqueue(vigia['prioridad'], vigia)
cpa.enqueue(capitan['prioridad'], capitan)
cpa.enqueue(timonel['prioridad'], timonel)
cpa.to_string()
print("\n se empiezan a evacuar uno por uno \n")
sig=cpa.dequeue()
cpa.to_string()
sig=cpa.dequeue()
cpa.to_string()
sig=cpa.dequeue()
cpa.to_string()
sig=cpa.dequeue()
cpa.to_string()
sig=cpa.dequeue()
cpa.to_string()
sig=cpa.dequeue()
cpa.to_string()
sig=cpa.dequeue()
cpa.to_string()
sig=cpa.dequeue()
cpa.to_string()
sig=cpa.dequeue()
cpa.to_string()
sig=cpa.dequeue()
cpa.to_string()
sig=cpa.dequeue()
