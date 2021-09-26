matriz = [[1,1,1],[2,2,2],[3,3,3],[4,4,4]]
matriz[0].append(sum(matriz[0][:])) # Se indica la lista dentro de la matriz la cual se le va a agregar el valor de la suma de todos los componentes de la misma
matriz[1].append(sum(matriz[1][:])) 
matriz[2].append(sum(matriz[2][:]))
matriz[3].append(sum(matriz[3][:]))
print(matriz) # Se imprime la matriz