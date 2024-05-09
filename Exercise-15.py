if __name__ == '__main__':
    print("Olá,calculo seu salário mensal, vai ser um prazer lhe ajudar!!😎")
    print("Insira quanto que você ganha por hora⏬:")
    Valorhora = float(input())

    print("Insira quantas horas você trabalhou esse mês⏬:")
    VhoraTrabalhadas = float(input())

    result = Valorhora*VhoraTrabalhadas
    print("Seguinte meu parceiro, Seu salário bruto esse mês foi de R$:",result)

    IR = result * 0.11
    print("Você pagou ao imposto de renda R$",IR)

    Inss = result * 0.08
    print("Você pagou ao inss R$",Inss)

    Sind = result * 0.05
    print("Você pagou ao sindicato R$",Sind)

    SalarioLiq = result - IR - Inss - Sind
    print("Seu salário Liquido foi de R$", SalarioLiq)
