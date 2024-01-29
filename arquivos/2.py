def bytes_para_mb(bytes):
    return bytes / (1024 * 1024)

def calcular_percentual(espaco_ocupado, espaco_total):
    return (espaco_ocupado / espaco_total) * 100

def main():
    # Lendo o arquivo de entrada
    with open('usuarios.txt', 'r') as entrada:
        usuarios = entrada.readlines()

    # Calculando espaço total ocupado e espaços ocupados por cada usuário
    espaco_total = 0
    espacos_usuarios = []
    for usuario in usuarios:
        nome, espaco = usuario.split()
        espaco = int(espaco)
        espaco_total += espaco
        espacos_usuarios.append((nome, espaco))

    # Ordenando usuários pelo espaço ocupado
    espacos_usuarios.sort(key=lambda x: x[1], reverse=True)

    # Escrevendo o relatório
    with open('relatorio_usuarios.txt', 'w') as saida:
        saida.write("ACME Inc.               Uso do espaço em disco pelos usuários\n")
        saida.write("------------------------------------------------------------------------\n")
        saida.write("Nr.  Usuário        Espaço utilizado     % do uso\n\n")
        
        nr = 1
        for nome, espaco in espacos_usuarios:
            espaco_mb = bytes_para_mb(espaco)
            percentual = calcular_percentual(espaco, espaco_total)
            saida.write(f"{nr:<5} {nome:<15} {espaco_mb:>15.2f} MB {' ' * 9} {percentual:>6.2f}%\n")
            nr += 1

        espaco_total_mb = bytes_para_mb(espaco_total)
        espaco_medio_mb = espaco_total_mb / len(espacos_usuarios)
        saida.write(f"\nEspaço total ocupado: {espaco_total_mb:.2f} MB\n")
        saida.write(f"Espaço médio ocupado: {espaco_medio_mb:.2f} MB\n")

if __name__ == "__main__":
    main()
