from arbol import Nodo

def compara(nodo):
    return nodo.get_coste()

def buscar_solucion_UCS(conexiones, estado_inicial, solucion):
    solucionado = False
    nodos_visitados = []
    nodos_frontera = []
    nodo_inicial = Nodo(estado_inicial)
    nodo_inicial.set_coste(0)
    nodos_frontera.append(nodo_inicial)

    while (not solucionado) and len(nodos_frontera) != 0:
        # ordenar la lista de nodos frontera
        nodos_frontera = sorted(nodos_frontera, key=compara)
        nodo = nodos_frontera[0]
        # extraer nodo y añadirlo a visitados
        nodos_visitados.append(nodos_frontera.pop(0))

        if nodo.get_datos() == solucion:
            # solución encontrada
            solucionado = True
            return nodo
        else:
            # expandir nodos hijo (ciudades con conexión)
            dato_nodo = nodo.get_datos()
            lista_hijos = []

            for un_hijo in conexiones[dato_nodo]:
                hijo = Nodo(un_hijo)
                coste = conexiones[dato_nodo][un_hijo]
                hijo.set_coste(nodo.get_coste() + coste)
                lista_hijos.append(hijo)

                if not hijo.en_lista(nodos_visitados):
                    # si está en la lista lo sustituimos con
                    # el nuevo valor de coste si es menor
                    if hijo.en_lista(nodos_frontera):
                        for n in nodos_frontera:
                            if n.igual(hijo) and n.get_coste() > hijo.get_coste():
                                nodos_frontera.remove(n)
                                nodos_frontera.append(hijo)
                    else:
                        nodos_frontera.append(hijo)
            nodo.set_hijos(lista_hijos)

if __name__ == "__main__":
    conexiones = {
        'EDO.MEX': {'CDMX': 125, 'SLP': 513},
        'PUEBLA': {'SLP': 514},
        'CDMX': {'EDO.MEX': 125, 'SLP': 423, 'MICHOACAN': 491},
        'MICHOACAN': {'CDMX': 491, 'SLP': 356, 'MONTERREY': 309, 'SONORA': 346},
        'SLP': {'QRO': 203, 'PUEBLA': 514, 'EDO.MEX': 513, 'CDMX': 423, 'SONORA': 603, 'GUADALAJARA': 437, 'MICHOACAN': 356, 'MONTERREY': 313, 'GUADALAJARA': 437, 'HIDALGO': 599},
        'QRO': {'HIDALGO': 390, 'SLP': 203},
        'HIDALGO': {'QRO': 390, 'SLP': 599},
        'GUADALAJARA': {'SLP': 437, 'MONTERREY': 394},
        'MONTERREY': {'SONORA': 296, 'MICHOACAN': 309, 'SLP': 313},
        'SONORA': {'MONTERREY': 296, 'SLP': 603, 'MICHOACAN': 346}
    }

    estado_inicial = 'EDO.MEX'
    solucion = 'HIDALGO'

    nodo_solucion = buscar_solucion_UCS(conexiones, estado_inicial, solucion)

    # mostrar resultado
    resultado = []
    nodo = nodo_solucion

    while nodo.get_padre() != None:
        resultado.append(nodo.get_datos())
        nodo = nodo.get_padre()

    resultado.append(estado_inicial)
    resultado.reverse()
    print(resultado)
    print('Coste: ' + str(nodo_solucion.get_coste()))
