#Um professor, muito legal, fez 3 provas durante um semestre, mas só vai levar em conta as duas notas mais altas para calcular a média.
#Faça uma aplicação que peça o valor das 3 notas, mostre como seria a média com essas 3 provas, a média com as 2 notas mais altas, 
# bem como sua nota mais alta e sua nota mais baixa.

def medias(nota1, nota2, nota3):
    
    media_3n = (nota1 + nota2 + nota3) / 3.0
    print("=======================================")
    print("Média com 3 notas = {0:.1f}".format(media_3n))
    mn1 = nota1
    if nota2 > mn1:
            mn1 = nota2
    elif nota3 > mn1:
            mn1 = nota3
    primeira_nota_maior = mn1
    
    mn2 = nota1
    if nota2 < mn2:
        mn2 = nota2
    elif nota3 < mn2:
        mn2 = nota3
        
    
    if nota1 > mn2 and nota1 < mn1:
                mn3 = nota1
    elif nota2 >mn2 and nota2 < mn1:
                mn3= nota2             
    else:
        mn3= nota3
       
    media_2nm = (mn1 + mn3) / 2.0
    print("=======================================")
    print("A média das duas maiores notas é = {0:.1f}".format(media_2nm))
    print("=======================================")

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))

medias(nota1, nota2, nota3)
 
