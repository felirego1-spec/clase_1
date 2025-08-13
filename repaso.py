from metodos import insertar_numero

lista_numeros=[]

for i in range(5):
    numero=int(input("ingrese un numero"))
    if numero %2 !=0 :
        continue   #este continue lo que me dice es que se continua con la iteracion osea ocupa un lugar de los 3 pero no se agrega a la lista ese valor mayor que 9
    insertar_numero (lista_numeros, numero)
print(f"lista de numeros: {lista_numeros}")


