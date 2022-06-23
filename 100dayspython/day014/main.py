import random

anime = [
    {
        "title": "Steins;Gate",
        "year": 2011,
        "genre": "Sci-Fi",
        "members": 2248778,
    },
    {
        "title": "Kimi No Na Wa",
        "year": 2016,
        "genre": "Drama",
        "members": 2367711,
    },
    {
        "title": "Monster",
        "year": 2004,
        "genre": "Suspense",
        "members": 859529,
    },
    {
        "title": "Great Teacher Onizuka",
        "year": 1999,
        "genre": "Comedy",
        "members": 727856,
    },
    {
        "title": "Code Geass",
        "year": 2006,
        "genre": "Sci-Fi",
        "members": 1996299,
    },
    {
        "title": "One Piece",
        "year": 1999,
        "genre": "Adventure",
        "members": 1894119,
    },
    {
        "title": "Death Note",
        "year": 2006,
        "genre": "Suspense",
        "members": 3422565,
    },
    {
        "title": "Bakemonogatari",
        "year": 2009,
        "genre": "Mystery",
        "members": 1281997,
    },
    {
        "title": "Perfect Blue",
        "year": 1998,
        "genre": "Horror",
        "members": 569798,
    },
    {
        "title": "Nana",
        "year": 2006,
        "genre": "Drama",
        "members": 552165,
    },
    {
        "title": "Yu Yu Hakusho",
        "year": 1992,
        "genre": "Action",
        "members": 600795,
    },
    {
        "title": "Baccano!",
        "year": 2007,
        "genre": "Comedy",
        "members": 832181,
    },
    {
        "title": "Naruto",
        "year": 2002,
        "genre": "Action",
        "members": 2494806,
    },
    {
        "title": "Psycho-Pass",
        "year": 2012,
        "genre": "Sci-Fi",
        "members": 1468429,
    },
    {
        "title": "Dragonball Z",
        "year": 1989,
        "genre": "Action",
        "members": 1098286,
    },
    {
        "title": "Neon Genesis Evangelion",
        "year": 1995,
        "genre": "Sci-Fi",
        "members": 1560436,
    },
    {
        "title": "Cowboy Bebop",
        "year": 1998,
        "genre": "Action",
        "members": 1622742,
    },
    {
        "title": "Samurai Champloo",
        "year": 1989,
        "genre": "Action",
        "members": 1105486,
    },
    {
        "title": "Attack on Titan",
        "year": 2013,
        "genre": "Action",
        "members": 3441001,
    },
    {
        "title": "Mirai Nikki",
        "year": 2011,
        "genre": "Action",
        "members": 1838677,
    },
    {
        "title": "Bleach",
        "year": 2004,
        "genre": "Action",
        "members": 1661911,
    },
    {
        "title": "Clannad",
        "year": 2007,
        "genre": "Romance",
        "members": 1300604,
    },
    {
        "title": "Toradora!",
        "year": 2008,
        "genre": "Romance",
        "members": 1982354,
    },
]


def call_anime():
    random_anime = random.choice(anime)
    return random_anime


def return_anime(check_anime):
    f_a_title = f_a_year = f_a_genre = ''
    for key in check_anime:
        if key == "title":
            f_a_title = check_anime[key]
        elif key == "year":
            f_a_year = check_anime[key]
        elif key == "genre":
            f_a_genre = check_anime[key]
    return f"{f_a_title}, {f_a_genre} from the year {f_a_year}"


def winner_anime(f_anime, s_anime):
    f_anime_members = s_anime_members = ''
    for key in f_anime:
        if key == "members":
            f_anime_members = f_anime[key]
    for key in s_anime:
        if key == "members":
            s_anime_members = s_anime[key]
    if f_anime_members > s_anime_members:
        return f_anime
    elif s_anime_members > f_anime_members:
        return s_anime


print("Higher Lower!")
option_a = call_anime()
option_b = call_anime()
game_over = False
score = 0
while not game_over:
    choice = ''
    print(f"Compare A: {return_anime(option_a)}")
    print("Versus")
    print(f"Against B: {return_anime(option_b)}")
    if option_a in anime:
        anime.remove(option_a)
    elif option_b in anime:
        anime.remove(option_b)
    player_choice = str(input(f"Who has more members on MyAnimeList? Type 'A' or 'B': ")).strip().upper()
    if player_choice == 'A':
        choice = option_a
    elif player_choice == 'B':
        choice = option_b
    winner = winner_anime(option_a, option_b)
    if winner == choice:
        score += 1
        print(f"You're right! Current score: {score}")
        if choice == option_a:
            option_b = call_anime()
        elif choice == option_b:
            option_a = option_b
            option_b = call_anime()
    elif winner != choice:
        print(f"Wrong Answer! YOU LOSE! Final score: {score}")
        game_over = True
