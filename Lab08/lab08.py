def main():
    """The main function of the code
    """


movies_list = []
n_movies = int(input())

for i in range(n_movies):
    movie_name = input()
    movies_list.append(movie_name)

n_evals = int(input())
movie_evaluation = {}
eval_list, movies_evals = [], []

for i in range(n_evals):
    evaluation = input()
    eval_list = evaluation.split(", ")
    movie_evaluation = {
        "evaluator": eval_list[0],
        "category": eval_list[1],
        "movie": eval_list[2],
        "rating": int(eval_list[3])}
    movies_evals.append(movie_evaluation)

simple_categories = ["filme que causou mais bocejos",
                     "filme que foi mais pausado",
                     "filme que mais revirou olhos",
                     "filme que não gerou discussão nas redes sociais",
                     "enredo mais sem noção"]

average_ratings = {}
average_rating = 0

for movie in movies_list:
    movie_ratings = {}
    for category in simple_categories:
        amount_votes = 0
        total = 0
        for k in range(len(movies_evals)):
            if movies_evals[k]["movie"] == movie and\
               movies_evals[k]["category"] == category:
                total += movies_evals[k]["rating"]
                amount_votes += 1
        if amount_votes != 0:
            average_rating = float(total/amount_votes)
        else:
            average_rating = 0
        movie_ratings[category] = average_rating
    average_ratings[movie] = movie_ratings

winner_movies = {}

for category in simple_categories:
    highest_rating = 0
    winner_movie = ""
    for movie in movies_list:
        if movie in average_ratings and category in average_ratings[movie]:
            rating = average_ratings[movie][category]
            if rating > highest_rating:
                highest_rating = rating
                winner_movie = movie
    winner_movies[category] = winner_movie

list_of_winners = []
repetitions = {}
number_of_repetitions = 0

for movie in winner_movies.values():
    list_of_winners.append(movie)
    number_or_repetitions = list_of_winners.count(movie)
    repetitions[movie] = number_of_repetitions

worst_movies = []

for movie, highest_repetition in repetitions.items():
    if highest_repetition == max(repetitions.values()):
        worst_movies.append(movie)

worst_movies_average = {}

for movie in worst_movies:
    worst_movies_average[movie] = sum(average_ratings[movie].values())
worst_movie_list = []
worst_movie_average = max(worst_movies_average.values())
for movie, rating in worst_movies_average.items():
    if rating == worst_movie_average:
        worst_movie_list.append(movie)
print(worst_movie_list)
not_belong_list = []

for movie, rating in average_ratings.items():
    if rating == 0:
        not_belong_list.append(movie)

# print("#### abacaxi de ouro ####\n")
# print("categorias simples")
# for category, movie in winner_movies.items():
#     print("categoria:", category)
#     print("-", movie)
# print("\ncategorias especiais")
# print("prêmio pior filme do ano")
# print("-", worst_movie)
# print("prêmio não merecia estar aqui")
# if not_belong_list != []:
#     print("- ", end='')
#     print(*not_belong_list, sep=', ')
# else:
#     print("- sem ganhadores")

if __name__ == "__main__":
    main()
