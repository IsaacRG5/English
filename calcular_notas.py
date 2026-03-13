nota1=int(input("nota 1 "))
nota2=int(input("nota 2 "))
nota3=int(input("nota 3 "))
notas=int(input("cuantas notas tines? "))

resultado = (nota1 + nota2 + nota3) / notas

print(resultado)

if resultado >7:
    print("paso") 
else:
    print("pierde")