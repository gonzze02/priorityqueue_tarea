from queue import PriorityQueue
#definimos la cola
q = PriorityQueue()

#encolamos a los pasientes
q.put((5, 'Hector'))
q.put((2, 'Gaby'))
q.put((1, 'Rafael'))
q.put((3, 'Esther'))
q.put((1, 'Libia'))
q.put((4, 'Esteban'))

#muestra la prioridad y lo elimina de la cola
print(f"Pasientes con mayor prioridad {q.get(), q.get(), q.get()}")

#solo muestra la cola
print('Pasientes en espera :', q.qsize())

#comprobamos si el estado de la cola esta vacia
print('La lista de pasinetes esta vacia :', q.empty())

# comprobamos si aun esta llena la cola
print('Faltan pasientes por atender :', q.full())
