#Faça um programa que calcule através de uma função o IMC de uma pessoa que tenha 1,68 e pese 75kg.
def calculo_imc(peso, altura):
    imc = peso  / (altura * altura )
    if imc < 18.5:
        return print ("IMC: {0:.1f}".format(imc),"Abaixo do peso")
    elif imc >= 18.5 and imc < 24.9:
        return print("IMC: {0:.1f}".format(imc),"Peso normal")
    elif imc >= 25 and imc <=29.9:
        return print("IMC: {0:.1f}".format(imc),"Sobrepeso")
    elif imc >=30 and imc <34.9:
        return print("IMC: {0:.1f}".format(imc),"Obesidade grau 1")
    elif imc >= 35 and imc < 39.9:
        return print("IMC: {0:.1f}".format(imc),"Obesidade grau 2")
    else:
        return print("IMC: {0:.1f}".format(imc),"Obesidade grau 3")
      
ps= float(input("Digite seu peso: ").replace(',','.'))
alt = float(input("Digite sua altura: ").replace(',','.'))
calculo_imc(ps, alt)