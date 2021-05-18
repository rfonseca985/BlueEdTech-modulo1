
palavra = input("Digite a palavra que deve ser adivinhada: ")
parada = ["_" for i in palavra]
chances = 0
alfabeto = list("abdcefghijklmnopqrstuvwxyz")
tentativas = []


print("Voce tem 6 chances para advinhar a palavra!!!")
while parada.count("_") != 0 and chances != 6:
        for letra in palavra:
         if letra in tentativas:
                print(letra, end=' ')
         else:
                print('_', end=' ')
        palpite = input("\nDigite seu palpite: ").lower()
        
        if palpite in palavra:
                for l in range(len(palavra)):
                 if palpite == palavra[l]:
                        del parada[l]
                        parada.insert(l,palpite)
                
        if palpite not in alfabeto or palpite == '':
	        print("Isso não é uma letra!")
        elif palpite in tentativas:
                print("Você já tentou essa letra. Tente outra!")
                continue
        elif palpite in palavra:
                print("Muito bem acertou uma letra")
        else:
                print("Passou longe")
                chances += 1
        tentativas.append(palpite)
        print("Chances pedidas:", chances)
        print(tentativas)
if chances == 6: 
 	    print("Game over!!!")
elif parada.count("_")== 0:
            print("A palavra era:",palavra.upper())
            print("Parabéns, Você venceu!!!".upper())