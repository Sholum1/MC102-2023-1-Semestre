linux_question = input("Este é um sistema que irá te ajudar a escolher a sua próxima Distribuição Linux. Responda a algumas poucas perguntas para ter uma recomendação.\nSeu SO anterior era Linux?\n(0) Não\n(1) Sim\n")

if linux_question == "0":
    macos_question = input("Seu SO anterior era um MacOS?\n(0) Não\n(1) Sim\n")
    if macos_question == "0":
      print("Você passará pelo caminho daqueles que decidiram abandonar sua zona de conforto, as distribuições recomendadas são: Ubuntu Mate, Ubuntu Mint, Kubuntu, Manjaro.")
    elif macos_question == "1":
        print("Você passará pelo caminho daqueles que decidiram abandonar sua zona de conforto, as distribuições recomendadas são: ElementaryOS, ApricityOS.")
    else:
        print("Opção inválida, recomece o questionário.")
elif linux_question == "1":
    programmer_question = input("É programador/ desenvolvedor ou de áreas semelhantes?\n(0) Não\n(1) Sim\n(2) Sim, realizo testes e invasão de sistemas\n")
    if programmer_question == "0":
        print("Ao trilhar esse caminho, um novo guru do Linux irá surgir, as distribuições que servirão de base para seu aprendizado são: Ubuntu Mint, Fedora.")
    elif programmer_question == "2":
        print("Ao trilhar esse caminho, um novo guru do Linux irá surgir, as distribuições que servirão de base para seu aprendizado são: Kali Linux, Black Arch.")
    elif programmer_question == "1":
        difficulty_question = input("Gostaria de algo pronto para uso ao invés de ficar configurando o SO?\n(0) Não\n(1) Sim\n")
        if difficulty_question == "0":
            arch_question = input("Já utilizou Arch Linux?\n(0) Não\n(1) Sim\n")
            if arch_question == "0":
                print("Ao trilhar esse caminho, um novo guru do Linux irá surgir, as distribuições que servirão de base para seu aprendizado são: Antergos, Arch Linux.")
            elif arch_question == "1":
                print("Suas escolhas te levaram a um caminho repleto de desafios, para você recomendamos as distribuições: Gentoo, CentOS, Slackware.")
            else:
                print("Opção inválida, recomece o questionário.")
        elif difficulty_question == "1":
            ubuntu_question = input("Já utilizou Debian ou Ubuntu?\n(0) Não\n(1) Sim\n")
            if ubuntu_question == "0":
               print("Ao trilhar esse caminho, um novo guru do Linux irá surgir, as distribuições que servirão de base para seu aprendizado são: OpenSuse, Ubuntu Mint, Ubuntu Mate, Ubuntu.")
            elif ubuntu_question == "1":
                print("Suas escolhas te levaram a um caminho repleto de desafios, para você recomendamos as distribuições: Manjaro, ApricityOS.")
            else:
                print("Opção inválida, recomece o questionário.")
        else:
            print("Opção inválida, recomece o questionário.")
    else:
        print("Opção inválida, recomece o questionário.")
else:
    print("Opção inválida, recomece o questionário.")

    [TODO] melhorar esse código e reenviar
