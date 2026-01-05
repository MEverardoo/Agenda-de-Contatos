def adicionar_contato(agenda, nome_contato):
    agenda = {'nome': nome_contato, 'Completada': False}
    agenda.append(agenda)
    print(f'O contato {nome_contato} foi adicionado!')
    return

agenda = []
while True:
    print('\nMenu Agenda de Contatos')
    print('1. Adicionar um contato')
    print('2. Lista de contatos')
    print('3. Editar contato')
    print('4. Favoritar contatos')
    print('5. Lista de contatos favoritos')
    print('6. Apagar contato')
    print('7. Sair')

    escolha = input('Digite um número: ')

    if escolha == '1':
        nome_contato = input('Digite o nome do novo contato: ')
        adicionar_contato(agenda, nome_contato)

    elif escolha == '7':
        break

print('Agenda finalizada!')