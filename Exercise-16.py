if __name__ == '__main__':
    print("Você sabe por que está aqui nobre, sabe o que eu posso faze por isso veio até mim HAHAHA!")
    Area = float(input("Insira o area a ser pintada (M²): "))

    Litritos = Area / 3

    Latas = Litritos / 18

    Valor = Latas * 80

    print("Você vai precisar de",Latas, "latitas de tinta.")
    print("Valor em Tintas: R$", Valor)
