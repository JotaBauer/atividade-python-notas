i=0
ap=0
rp=0
re=0
while True:

    print('====Controle de Notas====')
    print('1 - Cadastrar notas de um aluno')
    print('2 - Mostrar a quantidade de alunos cadrastrados')
    print('3 - Mostrar a quantidade de aprovados')
    print('4 - Mostrar a quantidade de recuperação')
    print('5 - Mostrar a quantidade de reprovados')
    print('6 - Encerrar')
    print('\n')

    p = int(input('Escolha uma opção: '))

    # x >= 7 aprovado
    # 7 > x >= 5 recuperação
    # x < 5 reprovado

    if p == 1:
        i+=1
        n = int(input('Qual a primeira nota do aluno? '))
        n1 = int(input('Qual a segunda nota do aluno? '))
        if n<0 and n1<0:
            print('Nota inválida')
            break
        if n>10 and n1<10:
            print('Nota inválida')
            break

        soma_notas=(n+n1)/2

        if soma_notas >=7:
            ap+=1
            print('Aluno aprovado')
        elif soma_notas<7 and soma_notas >=5:
            rp+=1
            print('Aluno em recuperação')
        else:
            re+=1
            print('Aluno reprovado')

        media = soma_notas/i
        print(f'A média do aluno é de {soma_notas}')


    elif p == 2:
        print(f'{i} Alunos foram cadastrados.')

    elif p == 3:
        print(f'{ap} Alunos foram aprovados.')

    elif p == 4:
        print(f'{rp} Alunos estão de recuperação.')

    elif p == 5:
        print(f'{re} Alunos foram reprovados.')

    elif p == 6:
        print('Encerrando programa')
        break
    else:
        print('Opção inválida!')
        break