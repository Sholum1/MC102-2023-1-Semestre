sheilas_choice = input()
reginaldos_choice = input()

if sheilas_choice == reginaldos_choice:
    print("empate")
elif sheilas_choice == "tesoura":
    if reginaldos_choice == "papel" or reginaldos_choice == "lagarto":
        print("Interestelar")
    else:
        print("Jornada nas Estrelas")
elif sheilas_choice == "papel":
    if reginaldos_choice == "pedra" or reginaldos_choice == "spock":
        print("Interestelar")
    else:
        print("Jornada nas Estrelas")
elif sheilas_choice == "pedra":
    if reginaldos_choice == "lagarto" or reginaldos_choice == "tesoura":
        print("Interestelar")
    else:
        print("Jornada nas Estrelas")
elif sheilas_choice == "lagarto":
    if reginaldos_choice == "spock" or reginaldos_choice == "papel":
        print("Interestelar")
    else:
        print("Jornada nas Estrelas")
elif sheilas_choice == "spock":
    if reginaldos_choice == "tesoura" or reginaldos_choice == "pedra":
        print("Interestelar")
    else:
        print("Jornada nas Estrelas")
