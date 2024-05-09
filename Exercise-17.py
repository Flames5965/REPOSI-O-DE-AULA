if __name__ == '__main__':
    print("Você sabe por que está aqui nobre, sabe o que eu posso faze por isso veio até mim HAHAHA!")
    Area = float(input("Insira o area a ser pintada (M²): "))

    Litritos = Area / 6
    Latas = Litritos / 18
    ValorLatas = Latas * 80
    Galudoes = Litritos / 3.6
    ValorGaludoes = Galudoes * 25

    print("Você vai precisar de",Latas, "latitas de tinta.\nValor em Tintas: R$", ValorLatas)
    print("Você vai precisar de",Galudoes, "galões de tinta.\nValor em Tintas: R$", ValorGaludoes)