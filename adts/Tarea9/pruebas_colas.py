from colas import PriorityQueue

cpq = PriorityQueue()
print("=================ingresando prioridades con enqueue uno por uno")
cpq.enqueue(4, "Maestre")
cpq.to_string()
cpq.enqueue(2, "Niños")
cpq.to_string()
cpq.enqueue(4, "Mecánico")
cpq.to_string()
cpq.enqueue(3, "Hombres")
cpq.to_string()
cpq.enqueue(4, "Vigía")
cpq.to_string()
cpq.enqueue(5, "Capitan")
cpq.to_string()
cpq.enqueue(4, "Timonel")
cpq.to_string()
cpq.enqueue(3, "Mujeres")
cpq.to_string()
cpq.enqueue(2, "3era edad")
cpq.to_string()
cpq.enqueue(1, "Niñas")
cpq.to_string()
print("\n================sacando dos prioridades de la cola una por una")
cpq.dequeue()
cpq.to_string()
cpq.dequeue()
cpq.to_string()
