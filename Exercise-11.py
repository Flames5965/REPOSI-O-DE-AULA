#Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
#o produto do dobro do primeiro com metade do segundo .
#a soma do triplo do primeiro com o terceiro.
#o terceiro elevado ao cubo
if __name__ == '__main__':
    print("Olá meu reii!!😎")
    ValorInt1 = int(input("Insira um valor inteiro:"))
    ValorInt2 = int(input("Insira um valor inteiro:"))
    ValorReal = float(input("Insira um valor real:"))


    resultsoma = (ValorInt1*2) + (ValorInt2/2)
    print("Seguinte meu parceiro, o produto do dobro do primeiro com metade do segundo é :",resultsoma)
    resultTriple = (ValorInt1*3) + (ValorReal)
    print("Seguinte meu parceiro, a soma do triplo do primeiro com o terceiro é :",resultTriple)
    resultCubo = ValorReal**3
    print("Seguinte meu parceiro, o terceiro elevado ao cubo é :",resultCubo)
