from metodos import insertar_numero

lista_numeros=[]

for i in range(3):
    numero=input("ingrese un numero")
    insertar_numero (lista_numeros, numero)
print(f"lista de numeros: {lista_numeros}")


