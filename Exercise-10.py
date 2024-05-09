#Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit
if __name__ == '__main__':
    print("Olá,faço a conversão de Graus Celcius para Graus Fahrenheit, vai ser um prazer lhe ajudar!!😎")
    GrausC = float(input("Insira a temperatura em Celcius:"))

    result = (GrausC * 9/5) + 32
    print("Seguinte meu parceiro, esse valor fica convertido em :",result,"°F")
