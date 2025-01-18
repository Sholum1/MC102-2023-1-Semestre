# Define some variables
number_of_players=int(input())
magic_number=list(input().split())
limits=list(input().split())
list_of_players=list(range(1,number_of_players+1))
limits_per_player=[limits[x:x+2] for x in range(0, len(limits), 2)]
player=0

# Start the game with the first half
first_half_points_list=[]
while player in range(0, number_of_players-number_of_players//2):
    first_half_points=(int(limits_per_player[player][1])-int(limits_per_player[player][0]))*int(magic_number[player])
    first_half_points_list.append(first_half_points)
    player=player+1

# Now the second half
second_half_points_list=[]
while player in range(number_of_players-number_of_players//2, number_of_players):
    second_half_points=(int(limits_per_player[player][1])-int(limits_per_player[player][0]))+int(magic_number[player])
    second_half_points_list.append(second_half_points)
    player=player+1

# Concatenate the lists
all_players_points_list=first_half_points_list+second_half_points_list

# Finding out if there are equal values and, if not, finding the biggest number
winner_point=all_players_points_list[0]
winner=0
point=1

while point<number_of_players:
    if all_players_points_list[point]>winner_point:
        winner=point
        winner_point=all_players_points_list[point]
    elif all_players_points_list[point]==winner_point:
        winner=None
    point=point+1
if winner!=None:
    winner_position=list_of_players[winner]
    print("O jogador número", winner_position, "vai receber o melhor bolo da cidade pois venceu com", all_players_points_list[winner], "ponto(s)!")
else:
    print("Rodada de cerveja para todos os jogadores!")
