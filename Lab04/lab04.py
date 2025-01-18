# Number of days
days=int(input())

# Repeat for the number of days
for day in range(1, days+1):

    # Number of pairs of animals that fight each other
    number_of_pairs=int(input())

    # Pairs of names of the animals that fight each other
    list_pairs=[]
    for i in range(0, number_of_pairs):
        pair=input().split()
        list_pairs.append(pair)

    # List of procediments and quantities of each procedure
    list_pxq=input().split()
    pairs_pxq=[list_pxq[x:x+2] for x in range(0, len(list_pxq), 2)]

    # Number of animals in the day
    number_of_animals=int(input())

    # Procediments
    pairs_axp=[]
    for i in range(0, number_of_animals):
        axp=input().split()
        pairs_axp.append(axp)

    unavailable_procediments=[]
    for p in range(0, len(pairs_axp)):
        if pairs_axp[p][1] not in list_pxq:
            unavailable_procediments.append(pairs_axp[p][1])

    # Shows the day
    if day == 1:
        print("Dia:", day)
    else:
        print("\nDia:", day)

    # Shows the number of fights in that day
    fights=[]
    for x in range(0, number_of_pairs):
        for y in range(0, number_of_animals):
            for z in range(0, number_of_animals):
                if list_pairs[x][0]==pairs_axp[y][0] and list_pairs[x][1]==pairs_axp[z][0]:
                    fights.append(x)
    print("Brigas:", len(fights))

    # Shows the animals that were attended
    attended_animals_list=[]
    for p in range(0, len(pairs_axp)):
        for q in range (0, len(pairs_pxq)):
            if pairs_axp[p][1]==pairs_pxq[q][0] and int(pairs_pxq[q][1])>0:
                pairs_pxq[q][1]=str(int(pairs_pxq[q][1])-1)
                attended_animals_list.append(pairs_axp[p][0])

    attended_animals_names=str()
    for i in range(0, len(attended_animals_list)):
        attended_animals_names=attended_animals_names+attended_animals_list[i]
        if i<len(attended_animals_list)-1:
            attended_animals_names=attended_animals_names+str(", ")

    if attended_animals_names!=str():
        print("Animais atendidos:", attended_animals_names)

    # Animals that request unavailable procediments
    unavailable_procediments_animals_list=[]
    for p in range(0, len(pairs_axp)):
        if pairs_axp[p][1] not in list_pxq:
            unavailable_procediments_animals_list.append(pairs_axp[p][0])


    # Not attended animals
    not_attended_animals_list=[]
    for x in range(0, len(pairs_axp)):
        if pairs_axp[x][0] not in attended_animals_names and pairs_axp[x][0] not in unavailable_procediments_animals_list:
            not_attended_animals_list.append(pairs_axp[x][0])

    not_attended_animals_names=str()
    for i in range(0, len(not_attended_animals_list)):
        not_attended_animals_names=not_attended_animals_names+not_attended_animals_list[i]
        if i<len(not_attended_animals_list)-1:
            not_attended_animals_names=not_attended_animals_names+str(", ")

    if not_attended_animals_names!=str():
        print("Animais não atendidos:", not_attended_animals_names)

    for i in range(0, len(unavailable_procediments_animals_list)):
        print("Animal", unavailable_procediments_animals_list[i], "solicitou procedimento não disponível.")
