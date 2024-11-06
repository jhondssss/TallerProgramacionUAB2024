numeros = [23, 44, 67, 12, 88, 34, 56, 78, 90, 11, 23]
resultado = ""
cont_par = 0
cont_impar = 0

for i in range(len(numeros)):
    num = numeros[i]
    if num % 2 == 0:
        resultado += "par"
        cont_par += 1
    else:
        resultado += "impar"
        cont_impar += 1
    
    if i < len(numeros) - 1:  
        resultado += ", "

print(f"Resultados: {resultado}")
print(f"Cantidad de pares: {cont_par}")
print(f"Cantidad de impares: {cont_impar}")

