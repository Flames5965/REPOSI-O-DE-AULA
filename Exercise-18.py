if __name__ == '__main__':
    TamanhoMB = float(input("Informe o tamanho do arquivo para download (MB): "))
    VelocidadeMS = float(input("Insiraa velocidade do link de Internet (Mbps): "))

    VelocidadeMS = VelocidadeMS / 8

    DownSeg = TamanhoMB /VelocidadeMS

    Down = DownSeg/ 60
    print("Tempo de download:", Down, "minutitos\nSim toda essa eternidade HAHA")
