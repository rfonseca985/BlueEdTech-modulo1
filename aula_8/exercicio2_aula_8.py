# Faça um jogo da forca. O programa terá uma lista de palavras lidas de um arquivo texto e escolherá uma aleatoriamente.
# O jogador poderá errar 6 vezes antes de ser enforcado.
palavra = "teste"
parada = ["_" for i in palavra]
chances = 6
alfabeto = list("abdcefghijklmnopqrstuvwxyz")
tentativas = []
tamanho = len(palavra) + 6

print("Voce tem 6 chances para advinhar a palavra!!!")
for i in range(tamanho):
        if parada.count("_") == 0 or chances == 0: break
        for letra in palavra:
         if letra in tentativas:
                print(letra, end=' ')
         else:
                print('_', end=' ')
        palpite = input("\nDigite seu palpite: ").lower()
        print("Chances:", chances)
        if palpite in palavra:
                for l in range(len(palavra)):
                 if palpite == palavra[l]:
                        del parada[l]
                        parada.insert(l,palpite)
                
        if palpite not in alfabeto or palpite == '':
	        print("Isso não é uma letra!")
        elif palpite in tentativas:
	        print("Você já tentou essa letra. Tente outra!")
        
        elif palpite in palavra:
                print("Muito bem acertou uma letra")
        else:
                print("Passou longe")
                chances -= 1
        tentativas.append(palpite)
        print(tentativas)
        if chances == 0: 
 	        print("Game over!!!")
        elif parada.count("_")== 0:
                print("A palavra era:",palavra.upper())
                print("Parabéns, Você venceu!!!".upper())