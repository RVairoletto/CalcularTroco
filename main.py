import sys


def receber_valor():
    valor = input('Insira o valor a ser calculado: R$')

    try:
        return float(valor.replace(',', '.'))
    except ValueError:
        print('O valor digitado é inválido, o programa será encerrado')
        sys.exit()


def calcular_troco(valor):
    notas = {
        200: 0,
        100: 0,
        50: 0,
        20: 0,
        10: 0,
        5: 0,
        2: 0,
    }

    for k in notas.keys():
        while valor >= k:
            notas[k] += 1

            valor -= k

    moedas = {
        1.0: 0,
        0.5: 0,
        0.25: 0,
        0.10: 0,
        0.05: 0,
        0.01: 0,
    }

    for k in moedas.keys():
        while valor >= k:
            moedas[k] += 1

            valor -= k
            valor = round(valor, 2)  # A imprecisão do ponto flutuante fazia uma morda sumir em certos casos

    return notas, moedas


executar = True

while executar:
    notas, moedas = calcular_troco(receber_valor())

    for k in notas.keys():
        if notas[k] > 0:
            print(f'Notas de R${k}: {notas[k]}')

    for k in moedas.keys():
        if moedas[k] > 0:
            print(f'Moedas de R${k}: {moedas[k]}')
