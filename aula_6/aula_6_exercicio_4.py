# Faça um programa que calcule o salário de um colaborador na empresa XYZ.
# O salário é pago conforme a quantidade de horas trabalhadas.
# Quando um funcionário trabalha mais de 40 horas ele recebe um adicional de 1.5 nas horas extras trabalhadas.

def calculo_salarial_XYZ(hrs_trb, salario_hr):
        if hrs_trb <= 40:
            salario_total = salario_hr * hrs_trb
            return print("Salário total R$ {0:.2f}".format(salario_total))
        else:
            salario_total = ((salario_hr * (hrs_trb - 40)) * 1.5) + (hrs_trb * salario_hr)
            return print("Salário total com 50% adicional R$ {0:.2f}".format(salario_total))



ht = int(input("Digite o número de horas trabalhadas: "))
sh = float(input("Digite o valor ganho por hora: "))

calculo_salarial_XYZ(ht, sh)