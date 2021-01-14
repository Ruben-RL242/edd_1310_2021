from pilas import Stack
import time
print("1.-Crear una lista de enteros en Python y realizar la suma con recursividad, el caso base es cuando la lista este vacia." , end="")
def suma_lista_rec(lista):
    if len(lista) == 1:
        return lista[0]
    else:
        return lista.pop() + suma_lista_rec(lista)

def main():
    datos=[4,2,3,5]
    res=suma_lista_rec(datos)
    print(f"la suma de los siguientes numeros: 4,2,3,5  es: {res}\n")

main()

print("2.-Hacer un contador regresivo con recursión.")
def printRev(n):
    if n > 0:
        time.sleep(1)
        print(f"\t{n}")
        printRev(n-1)
    time.sleep(0.1)

def main2():
    printRev(5)
    print("exploto la bomba\n")
    time.sleep(1)

main2();


print("3.-Sacar de un ADT pila el valor en la posición media.")
def eliminar(pila, size, recorrido) :
    if (pila.is_empty() or recorrido == size) :
        return "lista vacia"
    repaso = pila.peek()
    pila.pop()
    eliminar(pila, size, recorrido+1)
    mitad=(size/2)
    if mitad == int(mitad):
        if (recorrido != mitad and recorrido != (mitad-1)):
            pila.push(repaso)
    else:
        if (recorrido != int(size/2)) :
            pila.push(repaso)
def main3():
    pila = Stack()
    pila.push('R')
    pila.push('A')
    pila.push('N')
    pila.push('I <--')
    pila.push('M <--')
    pila.push('I')
    pila.push('L')
    pila.push('E')
    print("Pila sin eliminar datos, ELIMINAR")
    pila.to_string()
    print("Pila Nueva eliminando las letras de en medio que son M y I")
    eliminar(pila, pila.length(), 0)
    pila.to_string()

main3()
