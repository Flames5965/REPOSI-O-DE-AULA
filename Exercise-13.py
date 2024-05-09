#Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
#Para homens: (72.7*h) - 58
#Para mulheres: (62.1*h) - 44.7
if __name__ == '__main__':
    print("Olá,calculo seu peso ideal baseado na altura, vai ser um prazer lhe ajudar!!😎")
    Altura = float(input("Insira a sua altura(Use esse formato 0.00):"))

    Gender = input("Digite o seu gênero, insira (M) para macho, ou (F) para fêmea: ")
    if Gender== 'M':
            Pesito = (62.1*Altura) - 44.7
    elif Gender == 'F':
            Pesito = (72.7*Altura) - 58
    else:
        print("Vai inventar moda pra lá!!")
        exit()
    print("Seguinte meu parceiro, seu peso ideal é:",Pesito)
