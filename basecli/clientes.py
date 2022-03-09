# MODULO DE CADASTRO DE CLIENTES E BUSCA DE CLIENTES
# -*- coding: utf-8 -*-
# ----------------------------------------------------------------------------
# Created By  : Ricardo Antonio Cardoso
# Created Date: Mar-2022
# version ='1.0'
# ---------------------------------------------------------------------------


class Cores:
    vermelho = '\033[31m'
    verde = '\033[32m'
    azul = '\033[94m'
    normal = '\033[0m'


class Cliente:
    def __init__(self, nome, cpf, telefone, idade, endereco):
        self.nome = nome
        self.cpf = cpf
        self.telefone = telefone
        self.idade = idade
        self.endereco = endereco
        self.ativo = False

    def alterar_cpf(self, _troca_cpf):
        while True:
            _troca_cpf = _troca_cpf.zfill(11)
            _troca_cpf = f"{_troca_cpf[0:3]}.{_troca_cpf[3:6]}.{_troca_cpf[6:9]}-{_troca_cpf[9:11]}"
            print(f"{Cores.vermelho}Alterar CPF {self.cpf} por {_troca_cpf}{Cores.normal}?")
            confirma = input("Deseja continuar: (S/N): ").upper()
            if confirma[0] == "S":
                self.cpf = _troca_cpf
                print(f"{Cores.verde}CPF alterado{Cores.normal}")
                break
            elif confirma[0] == "N":
                print(f"CPF não alterado: {self.cpf}")
                break
            else:
                print("Digite apenas (S/N).")
                continue
        return self.cpf

    def ativar_cliente(self):
        self.ativo = True
        print(f"{Cores.verde}Cliente ativado.{Cores.normal}")
        return self.ativo

    def alterar_telefone(self, _troca_telefone):
        while True:
            _troca_telefone = _troca_telefone.zfill(11)
            _troca_telefone = f"{_troca_telefone[0:2]}.{_troca_telefone[2:7]}.{_troca_telefone[7:11]}"
            print(f"{Cores.vermelho}Alterar CPF {self.telefone} por {_troca_telefone}{Cores.normal}?")
            confirma = input("Deseja continuar: (S/N): ").upper()
            if confirma[0] == "S":
                self.telefone = _troca_telefone
                print('Telefone alterado')
                break
            elif confirma[0] == "N":
                print(f"Telefone não alterado {self.telefone}")
                break
            else:
                print("Digite apenas (S/N).")
                continue
        return self.telefone

    def __str__(self):
        print(50 * "-")
        print(f"{Cores.verde}Dados do cliente.")
        print(f"Nome     : {self.nome}.")
        print(f"Idade    : {self.idade}.")
        print(f"CPF      : {self.cpf}.")
        print(f"Telefone : {self.telefone}")
        print(f"Endereço : {self.endereco}{Cores.normal}")
        print(50 * "-")
