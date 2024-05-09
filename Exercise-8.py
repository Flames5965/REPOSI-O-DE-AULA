#Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês
if __name__ == '__main__':
    print("Olá,calculo seu salário mensal, vai ser um prazer lhe ajudar!!😎")
    print("Insira quanto que você ganha por hora⏬:")
    Valorhora = float(input())

    print("Insira quantas horas você trabalhou esse mês⏬:")
    VhoraTrabalhadas = float(input())

    result = Valorhora*VhoraTrabalhadas
    print("Seguinte meu parceiro, Seu salário bruto esse mês foi de R$:",result)
