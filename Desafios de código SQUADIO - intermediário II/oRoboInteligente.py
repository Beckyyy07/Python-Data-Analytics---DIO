def classificar_numero (numero):
    if numero > 0: 
        print("positivo!")
        return 1
    elif numero < 0: 
        print ("negativo!")
        return -1

positivos = 0
negativos = 0

while True:

    numero = int(input())

    if numero == 0:
        break

    resultado = classificar_numero(numero)

    if resultado == 1:
        positivos += 1
    elif resultado == -1:
        negativos += 1

print(f"{positivos} números positivos, {negativos} números negativos")
    




    

     
