#Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo que calcule seu peso ideal, usando a seguinte fórmula: (72.7*altura) - 58
if __name__ == '__main__':
    print("Olá,calculo seu peso ideal baseado na altura, vai ser um prazer lhe ajudar!!😎")
    Altura = float(input("Insira a sua altura:"))

    result = (72.7*Altura) - 58
    print("Seguinte meu parceiro, seu peso ideal é:",result)
