def determinante(matriz):
    suma_1 = (matriz[0][0]*matriz[1][1]*matriz[2][2]*matriz[3][3]*matriz[4][4])
    suma_2 = (matriz[1][0]*matriz[2][1]*matriz[3][2]*matriz[4][3]*matriz[0][4])
    suma_3 = (matriz[2][0]*matriz[3][1]*matriz[4][2]*matriz[0][3]*matriz[1][4])
    suma_4 = (matriz[3][0]*matriz[4][1]*matriz[0][2]*matriz[1][3]*matriz[2][4])
    suma_5 = (matriz[4][0]*matriz[0][1]*matriz[1][2]*matriz[2][3]*matriz[3][4])
    
    resta_1 = (matriz[4][0]*matriz[3][1]*matriz[2][2]*matriz[1][3]*matriz[0][4])
    resta_2 = (matriz[0][0]*matriz[4][1]*matriz[3][2]*matriz[2][3]*matriz[1][4])
    resta_3 = (matriz[1][0]*matriz[0][1]*matriz[4][2]*matriz[3][3]*matriz[2][4])
    resta_4 = (matriz[2][0]*matriz[1][1]*matriz[0][2]*matriz[4][3]*matriz[3][4])
    resta_5 = (matriz[3][0]*matriz[2][1]*matriz[1][2]*matriz[0][3]*matriz[4][4])

    solucion = suma_1 + suma_2 + suma_3 + suma_4 + suma_5 - resta_1 - resta_2 - resta_3 - resta_4 - resta_5
    return solucion

print("El determinante de la matriz 5x5 es", determinante([[2,7,4,3,1],[5,4,2,3,9],[7,4,1,2,4],[9,6,1,2,9],[3,7,2,9,1]]))
