#calculo_imc
peso_a = 50
peso_b = 80
peso_c = 110
altura_a = 1.65


imc = peso_c / (altura_a * altura_a)
print(imc.__round__(2))


if (imc <= 24.9) :
    print("Normal")
elif (imc >= 25 and imc <= 29.9) :
    print("Sobrepeso")
else :
    print("Obesidade")