from lista import DoubleLinkedList
l=DoubleLinkedList()
print("\n---------is_empty")
print(f"L esta vacia ? { l.is_empty() } ")
print("\n---------get_size")
print(f"el numero de elementos de la lista L son {l.get_size()}")
print("\n---------append")
print("Se usa append para agregar valores")
l.append(5)
l.append(10)
l.append(15)
l.append(10)
l.append(20)
l.append(10)
l.append(25)
print(f"L esta vacia ? { l.is_empty() } ")

print("\n---------find_from_tail")
print(f"la posicion del numero 5 desde tail es {l.find_from_tail(5)} ")

print("\n---------find_from_head")
print(f"la posicion del numero 5 desde head es {l.find_from_head(5)} ")

print("\n--------remove from head")
print(f"el numero de elementos de la lista L son {l.get_size()}")
l.transversal()
print("se elimina el numero 10 apartir de head")
l.remove_from_head(10)
print(f"el numero de elementos de la lista L son {l.get_size()}")
l.transversal()

print("\n---------remove from tail")
print(f"el numero de elementos de la lista L son {l.get_size()}")
l.transversal()
print("se elimina el numero 10 apartir de tail")
l.remove_from_tail(10)
print(f"el numero de elementos de la lista L son {l.get_size()}")
l.transversal()

print("\n---------- se intenta remover un valor que no esta en la lista")
print("l.remove_from_head(646874614)")
l.remove_from_head(646874614)
print("l.remove_from_head(0)")
l.remove_from_head(0)

print("\n---------get_size")
print(f"el numero de elementos de la lista L son {l.get_size()}")
l.transversal()

print("\n---------Recorrido transversal")
l.transversal()

print("\n---------Recorrido tranversal reverso")
l.reverse_transversal()