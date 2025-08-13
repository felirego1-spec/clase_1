from metodos import insertar_numero

lista_numeros=[]

for i in range(3):
    numero=int(input("ingrese un numero"))
    if numero > 9:
        print(f"no se admiten numeros mayores a 9")
        continue
    insertar_numero (lista_numeros, numero)
print(f"lista de numeros: {lista_numeros}")


