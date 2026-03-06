from rich.console import Console
from rich import print
import time

cores = Console()

def print_branco(texto):
    cores.print(texto, style="#DCDCDC")

def erro(texto):
    cores.print(texto, style="#FF0000")

def erro_digitacao ():
    erro ("Você digitou algo que não é um número.")

def tracos_duplos():
    print ('[#DCDCDC]=[/]' * 50) 

def tracos():
    print ('[#DCDCDC]-[/]' * 50)

def espacamento(qtd):
    for i in range(qtd):
        print()

def pausa():
    time.sleep(0.5)

def decimal_para_binario(n):
    return bin(n)[2:]

def decimal_para_hexadecimal(n):
    return hex(n)[2:].upper()

def decimal_para_octal(n):
    return oct(n)[2:]

def binario_para_decimal(b):
    return int(b, 2)

def hexadecimal_para_decimal (h):
    return int (h, 16)

def octal_para_decimal(o):
    return int(o, 8)


def opcao_menu():
    tracos_duplos()
    print ("[#DCDCDC]===============[/] [#00BFFF]ESCOLHA SUA OPÇÃO[/] [#DCDCDC]================[/]")
    tracos_duplos()
    print_branco ("1 - Decimal Para Binário")
    print_branco ("2 - Decimal Para Hexadecimal")
    print_branco ("3 - Binário Para Decimal")
    print_branco ("4 - Hexadecimal Para Decimal")
    print_branco ("5 - Octal Para Decimal")
    print_branco ("6 - Decimal Para Octal")
    print_branco ("0 - Para Encerrar o Programa")
    tracos_duplos()


def main():
    while True: 
        espacamento(1)
        opcao_menu()
        espacamento(1)
        pausa()
        try:
            escolha_menu = int (input ("DIGITE SUA ESCOLHA: "))
            espacamento(1)
            pausa()
        except ValueError:
            espacamento(1)
            tracos()
            erro_digitacao()
            tracos()
            continue


        if escolha_menu == 1:
            tracos()
            print_branco ("-=-=-=-=-=-=-= DECIMAL PARA BINÁRIO =-=-=-=-=-=-=-")
            tracos()
            espacamento(1)
            try:
                escolha_decimal = int (input ("Digite um número Decimal: "))
                pausa()
                espacamento(2)
                print_branco (f"DECIMAL: {escolha_decimal}")
                print_branco (f"BINÁRIO: {decimal_para_binario(escolha_decimal)}")
                espacamento(2)
                tracos()
                pausa()
                espacamento(1)
            except ValueError:
                pausa()
                espacamento(1)
                tracos()
                erro_digitacao()
                tracos()


        elif escolha_menu == 2:
            tracos()
            print_branco ("-=-=-=-=-=- DECIMAL PARA HEXADECIMAL -=-=-=-=-=-=-")
            tracos()
            espacamento(1)
            try:
                escolha_decimal = int (input("Digite um número Decimal: "))
                pausa()
                espacamento(2)
                print_branco (f"DECIMAL: {escolha_decimal}")
                print_branco (f"HEXADECIMAL: {decimal_para_hexadecimal(escolha_decimal)}")
                espacamento(2)
                tracos()
                pausa()
                espacamento(1)
            except ValueError:
                pausa()
                espacamento(1)
                tracos()
                erro_digitacao()
                tracos()


        elif escolha_menu == 3:
            tracos()
            print_branco ("-=-=-=-=-=-=-= BINÁRIO PARA DECIMAL =-=-=-=-=-=-=-")
            tracos()
            espacamento(1)
            try:
                escolha_binario = input("Digite o número Binário: ")
                pausa()
                espacamento(2)
                print_branco (f"BINÁRIO: {escolha_binario}")
                print_branco (f"DECIMAL: {binario_para_decimal(escolha_binario)}")
                espacamento(2)
                tracos()
                pausa()
                espacamento(1)
            except ValueError:
                pausa()
                espacamento(1)
                tracos()
                erro_digitacao()
                tracos()


        elif escolha_menu == 4:
            tracos()
            print_branco("-=-=-=-=-=-= HEXADECIMAL PARA DECIMAL =-=-=-=-=-=-")
            tracos()
            espacamento(1)
            try:
                escolha_hexadecimal = input ("Digite o número Hexadecimal: ")
                pausa()
                espacamento(2)
                print_branco(f"HEXADECIMAL: {escolha_hexadecimal}")
                print_branco (f"DECIMAL: {hexadecimal_para_decimal(escolha_hexadecimal)}")
                espacamento(2)
                tracos()
                pausa()
                espacamento(1)
            except ValueError:
                pausa()
                espacamento(1)
                tracos()
                erro_digitacao()
                tracos()


        elif escolha_menu == 5:
            tracos()
            print_branco ("-=-=-=-=-=-=-= OCTAL PARA DECIMAL =-=-=-=-=-=-=-=-")
            tracos()
            espacamento(1)
            try:
                escolha_octal = input ("Digite o número Octal: ")
                pausa()
                espacamento(2)
                print_branco (f"OCTAL: {escolha_octal}")
                print_branco (f"DECIMAL: {octal_para_decimal(escolha_octal)}")
                espacamento(2)
                tracos()
                pausa()
                espacamento(1)
            except ValueError:
                pausa()
                espacamento(1)
                tracos()
                erro_digitacao()
                tracos()


        elif escolha_menu == 6:
            tracos()
            print_branco ("-=-=-=-=-=-=-= DECIMAL PARA OCTAL =-=-=-=-=-=-=-=-")
            tracos()
            espacamento(1)
            try:
                escolha_decimal = int (input("Digite um número Decimal: "))
                pausa()
                espacamento(2)
                print_branco (f"DECIMAL: {escolha_decimal}")
                print_branco (f"OCTAL: {decimal_para_octal(escolha_decimal)}")
                espacamento(2)
                tracos()
                pausa()
                espacamento(1)
            except ValueError:
                pausa()
                espacamento(1)
                tracos()
                erro_digitacao()
                tracos()


        elif escolha_menu == 0:
            tracos()
            erro ("PROGRAMA SE ENCERRANDO...")
            pausa()
            break


        else:
            erro ("OPÇÃO INCORRETA! TENTE UMA OPÇÃO VÁLIDA.")

if __name__ == "__main__":
    main()
