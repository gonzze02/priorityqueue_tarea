import heapq
dato = [1,5,4,8,6,7]

heapq.heapify(dato)
print(f"Esta lista muestra el estado de cada pasiente, {dato}, el estdo del pasiente es mas grave conforme el numero se mas pequeño")

heapq.heappush(dato, 2)
print(f"Aqui se muestra el pasiente que tenía mayor prioridad fue atendido primero y se agrego otro pasiente {dato}")

heapq.heappop(dato)
print(f"Un pasiente de mayor prioridad fue atendido y se quito de la lista {dato}")

heapq.heappushpop(dato, 3)
print(f"En esta parte el pasiente mas garve fue atendido e ingresaron a otro {dato}")

print(f"Los pasientes que se muestran a continuacion, {heapq.nlargest(3, dato)} son los que se atenderan a último")
print(f"los pasientes que se muestran a continuacion, {heapq.nsmallest(3, dato)}se atenderan mas antes que los demas")
