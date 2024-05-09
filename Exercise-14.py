#João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário de seu trabalho. Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do estado de São Paulo (50 quilos) deve pagar uma multa de R$ 4,00 por quilo excedente. João precisa que você faça um programa que leia a variável peso (peso de peixes) e calcule o excesso. Gravar na variável excesso a quantidade de quilos além do limite e na variável multa o valor da multa que João deverá pagar. Imprima os dados do programa com as mensagens adequadas.
if __name__ == '__main__':
    print("Só vamo meu fio, você já sabe por que eu estou aqui" )
    Peso = float(input("Quantos quilos você conseguiu pegar hoje? Insira o valor:"))
    PesoLimite = 50
    if Peso > PesoLimite:
        QntPassou = Peso - PesoLimite
        Multita = QntPassou*4
        print("Peso maior que o limite permitido:",QntPassou,"Kg","\nMulta a ser paga R$:",Multita)
    else:
        print("Se safou ein safado")

