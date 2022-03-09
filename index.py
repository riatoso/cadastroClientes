# MODULO DE CADASTRO DE CLIENTES E BUSCA DE CLIENTES INDEX
# -*- coding: utf-8 -*-
# ----------------------------------------------------------------------------
# Created By  : Ricardo Antonio Cardoso
# Created Date: Mar-2022
# version ='1.0'
# ---------------------------------------------------------------------------
import time
from basecli.clientes import Cliente as cadcli
from basecli.clientes import Cores as cor

if __name__ == "__main__":
    cliente = cadcli
    lista_cli = []


    def menu():
        while True:
            print("Qual o procedimento a ser adotado ?")
            print(50 * "*")
            print("1 - INSERIR CLIENTE ")
            print("2 - CONSULTAR POR CPF")
            print("3 - ALTERAR TELEFONE")
            print("4 - ALTERAR CPF")
            print("5 - SAIR")
            print(50 * "*")
            escolha = input("Digite sua escolha: ")
            try:
                escolha = int(escolha)
            except:
                print(f"{cor.vermelho}Escolha precisa ser numero.{cor.normal}")
                continue

            if escolha == 1:
                inserir()
            elif escolha == 2:
                consultar_cpf()
            elif escolha == 3:
                alterar_telefone()
            elif escolha == 4:
                alterar_cpf()
            elif escolha == 5:
                print(f'{cor.azul}SAINDO...{cor.normal}')
                time.sleep(3)
                break
            else:
                print("NENHUMA ESCOLHA VALIDA")
            continue


    def inserir():
        while True:
            qtd = input("Quantos clientes deseja inserir: ")
            try:
                qtd = int(qtd)
                break
            except:
                print(f"{cor.vermelho}QUANTIDADE PRECISA SER INTEIRO{cor.normal}")
                continue

        tamanho_lista = len(lista_cli)
        while len(lista_cli) != tamanho_lista + qtd:
            while True:
                tamanho = len(lista_cli)
                tamanho = str(tamanho)
                cli_temp = (f"{str('cliente')}{tamanho}")
                nome = input("Digite seu nome completo: ").title()
                while True:
                    print(f"{cor.vermelho}OBS. SEM TRAÇOS OU PONTOS{cor.normal}")
                    cpf = input("Digite seu cpf com 11 digitos: ")
                    cpf = f"{cpf[0:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:11]}"
                    confirma_cpf = input(f"Confirma este CPF: {cpf} (S/N): ").upper()
                    if confirma_cpf[0] == "S":
                        print("CONFIRMADO")
                        break
                    else:
                        continue
                while True:
                    print(f"{cor.vermelho}OBS. SEM TRAÇOS OU PONTOS{cor.normal}")
                    telefone = input("Digite seu telefone celular com DDD: ")
                    telefone = f"{telefone[0:2]}.{telefone[2:7]}.{telefone[7:11]}"
                    confirma_telefone = input(f"Confirma este Telefone: {telefone} (S/N): ").upper()
                    if confirma_telefone[0] == "S":
                        print("CONFIRMADO")
                        break
                    else:
                        continue
                while True:
                    idade = input("Digite sua idade: ")
                    try:
                        idade = int(idade)
                        break
                    except:
                        print(f"{cor.vermelho}IDADE PRECISA SER INTEIRO{cor.normal}")
                        continue
                endereco = input("Digite nome da rua e numero da casa: ").title()
                print("Dados de cliente digitado.")
                print(50 * "-")
                print(f"{cor.verde}Dados do cliente.")
                print(f"Nome     : {nome}.")
                print(f"Idade    : {idade}.")
                print(f"CPF      : {cpf}.")
                print(f"Telefone : {telefone}")
                print(f"Endereço : {endereco}{cor.normal}")
                print(50 * "-")
                valida = input("Valida as informações (S/N): ").upper()
                if valida == "S":
                    print("VALIDADO")
                    cli_temp = cliente(nome, cpf, telefone, idade, endereco)
                    lista_cli.append(cli_temp)
                    break
                else:
                    continue

            print(lista_cli)
            print(len(lista_cli))

    def consultar_cpf():
        print(f"{cor.vermelho}INSIRA O CPF SEM ESPAÇOS, PONTOS OU TRAÇOS{cor.normal}")
        while True:
            cpf_busca = input("Digite o CPF a ser procurado no banco: ")
            cpf_busca = f"{cpf_busca[0:3]}.{cpf_busca[3:6]}.{cpf_busca[6:9]}-{cpf_busca[9:11]}"
            print(f"CPF a ser procurado {cpf_busca}.")
            confirmar = input("Confirma a procura pelo CPF acima ? (S/N): ").upper()
            if confirmar[0] == "S":
                break
            else:
                continue
        for i in lista_cli:
            if i.cpf == cpf_busca:
                print(50*"-")
                print(f"Nome     : {i.nome}")
                print(f"Telefone : {i.telefone}")
                print(f'Idade    : {i.idade}')
                print(f"CPF      : {i.cpf}")
                print(50 * "-")
                time.sleep(3)
                break
            print("CPF NÃO EXISTE NO BANCO DE DADOS")

    def alterar_cpf():
        print(f"{cor.vermelho}INSIRA O CPF SEM ESPAÇOS, PONTOS OU TRAÇOS{cor.normal}")
        while True:
            cpf_busca = input("Digite o CPF a ser alterado : ")
            cpf_busca = f"{cpf_busca[0:3]}.{cpf_busca[3:6]}.{cpf_busca[6:9]}-{cpf_busca[9:11]}"
            print(f"CPF a ser procurado {cpf_busca}.")
            confirmar = input("Confirma a procura pelo CPF acima ? (S/N): ").upper()
            if confirmar[0] == "S":
                break
            else:
                continue
        for i in lista_cli:
            if i.cpf == cpf_busca:
                print(50 * "-")
                print(f"Nome     : {i.nome}")
                print(f"Telefone : {i.telefone}")
                print(f'Idade    : {i.idade}')
                print(f"CPF      : {i.cpf}")
                print(50 * "-")
                time.sleep(3)
                print(f"{cor.vermelho}INSIRA O CPF SEM ESPAÇOS, PONTOS OU TRAÇOS{cor.normal}")
                cpf_altera = input("Digite o numero novo de CPF : ")
                i.alterar_cpf(cpf_altera)
                i.__str__()
                break
            print("CPF NÃO EXISTE NO BANCO DE DADOS")

    def alterar_telefone():
        print(f"{cor.vermelho}INSIRA O NUMERO DE CELULAR SEM ESPAÇOS, PONTOS OU TRAÇOS{cor.normal}")
        while True:
            tel_busca = input("Digite o telefone a ser alterado : ")
            tel_busca = f"{tel_busca[0:2]}.{tel_busca[2:7]}.{tel_busca[7:11]}"
            print(f"CPF a ser procurado {tel_busca}.")
            confirmar = input("Confirma a procura pelo CPF acima ? (S/N): ").upper()
            if confirmar[0] == "S":
                break
            else:
                continue
        for i in lista_cli:
            if i.telefone == tel_busca:
                print(50 * "-")
                print(f"Nome     : {i.nome}")
                print(f"Telefone : {i.telefone}")
                print(f'Idade    : {i.idade}')
                print(f"CPF      : {i.cpf}")
                print(50 * "-")
                time.sleep(3)
                print(f"{cor.vermelho}INSIRA O TELEFONE SEM ESPAÇOS, PONTOS OU TRAÇOS{cor.normal}")
                tel_altera = input("Digite o numero novo de telefone : ")
                i.alterar_telefone(tel_altera)
                i.__str__()
                break
            print("TELEFONE NÃO EXISTE NO BANCO DE DADOS")


    menu()
