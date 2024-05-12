# Importamos la librería json
import json

# Definimos una función que busca el salida y el llegada del laberinto en la ruta
def meta(ruta):
  salida = None
  llegada = None
  
  # Recorremos la matriz por filas y columnas
  for i in range(len(ruta)):
    for j in range(len(ruta[i])):
      # Si encontramos la letra S, guardamos su posición como inicio
      if ruta[i][j] == 'S':
        salida = (i, j)
        
      # Si encontramos la letra E, guardamos su posición como fin
      if ruta[i][j] == 'E':
        llegada = (i, j)
        
  # Devolvemos una tupla con el inicio y el fin
  return (salida, llegada)

# Definimos una función que busca los lugares válidos de una coordenada en el laberinto
def buscar_camino(ruta, coordenada):
  lugares = []
  # Obtenemos las coordenadas
  i, j = coordenada
  
  # Comprobamos si la celda de arriba es válida
  if i > 0 and ruta[i-1][j] != '1':
    lugares.append((i-1, j))
    
  # Comprobamos si la celda de abajo es válida
  if i < len(ruta) - 1 and ruta[i+1][j] != '1':
    lugares.append((i+1, j))
    
  # Comprobamos si la celda de la izquierda es válida
  if j > 0 and ruta[i][j-1] != '1':
    lugares.append((i, j-1))
    
  # Comprobamos si la celda de la derecha es válida
  if j < len(ruta[i]) - 1 and ruta[i][j+1] != '1':
    lugares.append((i, j+1))
    
  # Devolvemos la lista de lugares válidos
  return lugares

# Definimos una función que resuelva el laberinto usando una búsqueda en anchura
def resolver_laberinto(camino):
  # Buscamos el salida y el llegada del laberinto
  salida, llegada = meta(camino)
  # Creamos una cola para almacenar los nodos a explorar
  cola = [salida]
  # Creamos un diccionario para almacenar los nodos por los que se pasó y sus predecesores
  recorridos = {salida: None}
  
  # Mientras la cola no esté vacía
  while cola:
    # Sacamos el primer valor de la cola
    valor = cola.pop(0)
    
    # Si el valor es llegada, hemos encontrado el camino
    if valor == llegada:
      break
    
    # Buscamos los lugares válidos del nodo
    lugares = buscar_camino(camino, valor)
    
    # Para cada lugar
    for lugar in lugares:
      if lugar not in recorridos:
        # Lo añadimos a la cola
        cola.append(lugar)
        
        # Lo marcamos como visitado y guardamos su predecesor
        recorridos[lugar] = valor
        
  # Si no hemos encontrado llegada, el laberinto no tiene solución
  if valor != llegada:
    return None
  
  # Si hemos encontrado llegada, reconstruimos el camino
  ruta = []
  while valor != salida:
    # Añadimos el valor a la ruta
    ruta.append(valor)
    
    # Obtenemos el predecesor del valor
    valor = recorridos[valor]
  # Añadimos el inicio al camino
  
  ruta.append(salida)
  
  # Invertimos el orden del camino
  ruta.reverse()
  
  # Marcamos el camino con la letra X en la matriz
  for i, j in ruta:
    camino[i][j] = 'X'
    
  # Devolvemos la matriz con el camino marcado
  return camino

# Leemos el input del usuario como un JSON
laberinto = input("Introduce el laberinto como un JSON: ")

# Convertimos el JSON a una matriz de Python
camino = json.loads(laberinto)

# Resolvemos el laberinto
solucion = resolver_laberinto(camino)

# Si hay solución, la mostramos
if solucion:
  print("El laberinto resuelto es:")
  for fila in solucion:
    print(fila)
    
# Si no hay solución, lo indicamos
else:
  print("El laberinto no tiene solución")