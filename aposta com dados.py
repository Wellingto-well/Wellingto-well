from random import randint

saldo = 1000
vitoria = []
derrota = []

for aposta in range(0,1000):

    dado1 = randint(1, 6)
    dado2 = randint(1, 6)

    soma_dos_dados = dado1 + dado2
    print('EXPLICANDO O JOGO')
    print('')
    print(f'Vamos sortear 2 dados e soma-los se der 7 ou 2 voce ganhar o dobro dq aposto')
    print(f'Se der 6 voce perde o que aposto')
    print(f'Se der 10 vai empatar e vc nao perde e nem ganha nada')
    print(f'Se nao der nenhum desses resultado vc tera oportunidade de tentar novamente')
    print(f'')
    

    somas_das_vitoria = sum(vitoria)
    somas_das_derrotas = sum(derrota)

    fim_do_jogo_saldo_total = saldo + (somas_das_vitoria + somas_das_derrotas)

    print(f'Esse é seu saldo: R${fim_do_jogo_saldo_total}')
    print('')
    valor_da_aposta = int(input('Digite o valor que ira apostar: '))

    if valor_da_aposta < fim_do_jogo_saldo_total:

        if soma_dos_dados == 7 or soma_dos_dados == 2 or soma_dos_dados == 8:
            print(f'Parabens voce ganhou o resultado do dado foi {soma_dos_dados}')
            total_vitoria =+ 1
            novo_saldo_vitoria = 0 + valor_da_aposta * 2
            vitoria.append(novo_saldo_vitoria)

            tentar_novamente_vitoria = int(input('Se quiser tentar novamente digite 1 caso \nSe nao quiser tentar novamente digite 2: '))
            if tentar_novamente_vitoria == 1:
                continue
            else:
                break

        elif soma_dos_dados == 6 or soma_dos_dados == 5:
            print(f'Que pena voce perdeu o resultado do dado foi {soma_dos_dados}')
            total_derrota =+ 1
            novo_saldo_derrota = 0 - valor_da_aposta  
            derrota.append(novo_saldo_derrota)

            tentar_novamente_derrota = int(input('Se quiser tentar novamente digite 1 caso \nSe nao quiser tentar novamente digite 2: '))
            if tentar_novamente_derrota == 1:
                continue
            else:
                break

        elif soma_dos_dados == 10:
            print(f'Empatou o resultado do dado foi {soma_dos_dados}') 

            tentar_novamente_empate = int(input('Se quiser tentar novamente digite 1 caso \nSe nao quiser tentar novamente digite 2: '))
            if tentar_novamente_empate == 1:
                continue
            else:
                break

        else:
            print(f'Quer tentar denovo? O resultado do dado foi {soma_dos_dados}')

            tentar_novamente = int(input('Se quiser tentar novamente digite 1 caso \nSe nao quiser tentar novamente digite 2: '))

            if tentar_novamente == 1:
                continue
            else:
                break
    else:
        print(f'O valor da aposta é maior que o saldo. Esse é seu saldo{saldo}')

    somas_das_vitoria = sum(vitoria)
    somas_das_derrotas = sum(derrota)

    fim_do_jogo_saldo_total = saldo + (somas_das_vitoria + somas_das_derrotas)

print(f'ESSE FOI O SEU SALDO COM O ENCERRAMENTO DO JOGO: R${fim_do_jogo_saldo_total}')
