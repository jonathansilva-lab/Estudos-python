import socket # usei a biblioteca socket de rede do python para começar o projeto


def scan_port(ip: str, port: int, timeout: float = 1.0) -> bool: # criei uma função para scannear portas 
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.settimeout(timeout)
        try:
            result = sock.connect_ex((ip, port))
            return result == 0
        except socket.error:
            return False


def main():
    print('SCANNER IP')

    ip = input('Digite um IP ou hostname: ').strip()

    try:
        porta_inicial = int(input('Digite a primeira porta: '))
        porta_final = int(input('Digite a última porta: '))
    except ValueError:
        print('Entrada inválida: use números inteiros para as portas.')
        return

    if porta_inicial < 1 or porta_final > 65535 or porta_inicial > porta_final:
        print('Faixa de portas inválida. Use valores entre 1 e 65535.')
        return

    print(f'Escaneando {ip} de {porta_inicial} a {porta_final}...')

    for porta in range(porta_inicial, porta_final + 1):
        aberta = scan_port(ip, porta)
        status = 'ABERTA' if aberta else 'fechada'
        print(f'Porta {porta}: {status}')


if __name__ == '__main__':
    main()
