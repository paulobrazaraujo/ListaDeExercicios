'''
Faça um programa que converta da notação de 24 horas para a notação de 12 horas.
Por exemplo, o programa deve converter 14:25 em 2:25 P.M. A entrada é dada em
dois inteiros. Deve haver pelo menos duas funções: uma para fazer a conversão
e uma para a saída. Registre a informação A.M./P.M. como um valor ‘A’ para
A.M. e ‘P’ para P.M. Assim, a função para efetuar as conversões terá um
parâmetro formal para registrar se é A.M. ou P.M. Inclua um loop que permita
que o usuário repita esse cálculo para novos valores de entrada todas as vezes
que desejar.
'''

def hora():
    h = 9999
    print('Digite a hora ou 100 para fechar o programa!')
    while h != 100:
        h = int(input('Digite a hora: '))
        if h == 100:
            break
        m = input('Digite os min: ')
        if h > 12:
            print(f'{h-12}:{m} P.M.')
        elif h == 00:
            print(f'{12}:{m} P.M.')
        else:
            print(f'{h}:{m} P.M.')
hora()
