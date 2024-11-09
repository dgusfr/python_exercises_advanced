import re

def validar_endereco_ip(ip):
    padrao_ip = r'^((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$'
    if re.match(padrao_ip, ip):
        return True
    else:
        return False

def main():
    with open('entrada.txt', 'r') as entrada:
        enderecos = entrada.readlines()

    validos = []
    invalidos = []
    for endereco in enderecos:
        endereco = endereco.strip()
        if validar_endereco_ip(endereco):
            validos.append(endereco)
        else:
            invalidos.append(endereco)

    with open('relatorio_enderecos.txt', 'w') as saida:
        saida.write("[Endereços válidos:]\n")
        for endereco in validos:
            saida.write(f"{endereco}\n")

        saida.write("\n[Endereços inválidos:]\n")
        for endereco in invalidos:
            saida.write(f"{endereco}\n")

#Verifica se o módulo atual está sendo executado como o programa principal.
if __name__ == "__main__":
    main()
