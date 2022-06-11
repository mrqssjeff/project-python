import random
countries = ['Afghanistan', 'Albania', 'Algeria', 'Andorra', 'Angola', 'Anguilla',
             'Antarctica', 'Argentina', 'Armenia', 'Aruba', 'Australia', 'Austria', 'Azerbaijan',
             'Bahamas', 'Bahrain', 'Bangladesh', 'Barbados', 'Belarus', 'Belgium', 'Belize', 'Benin', 'Bermuda',
             'Bhutan', 'Bolivia', 'Bosnia', 'Botswana', 'Brazil', 'Bulgaria', 'Cambodia', 'Cameroon', 'Canada',
             'Cape Verde', 'Chile', 'China', 'Colombia', 'Comoros', 'Congo', 'Costa Rica', 'Croatia', 'Cuba',
             'Cyprus', 'Czech Republic', 'Denmark', 'Dominica', 'Dominican Republic', 'Ecuador', 'Egypt', 'El Salvador',
             'Estonia', 'Ethiopia', 'Malvinas', 'Faroe Islands', 'Fiji', 'Finland', 'France',
             'Gambia', 'Georgia', 'Germany', 'Ghana', 'Gibraltar', 'Greece', 'Greenland', 'Grenada', 'Guatemala',
             'Guinea', 'Guinea-Bissau', 'Haiti', 'Vatican', 'Honduras', 'Hong Kong', 'Hungary', 'Iceland', 'India',
             'Indonesia', 'Iran', 'Iraq', 'Ireland','Israel', 'Italy', 'Jamaica', 'Japan',
             'Jordan', 'Kazakhstan', 'Kenya', "Korea", 'Kuwait', 'Kyrgyzstan', 'Lebanon',
             'Liberia', 'Libya', 'Liechtenstein', 'Lithuania', 'Luxembourg', 'Macao',
             'Macedonia', 'Madagascar', 'Malawi', 'Malaysia', 'Maldives', 'Mali', 'Malta',
             'Mexico', 'Moldova', 'Monaco', 'Mongolia', 'Montenegro', 'Montserrat',
             'Morocco', 'Mozambique', 'Myanmar', 'Namibia', 'Nepal', 'Netherlands',
             'New Zealand', 'Nicaragua', 'Niger', 'Nigeria',
             'Norway', 'Pakistan', 'Panama', 'Paraguay', 'Peru', 'Philippines', 'Poland', 'Portugal', 'Puerto Rico',
             'Qatar', 'Romania', 'Russia', 'Rwanda', 'San Marino', 'Sao Tome and Principe', 'Saudi Arabia', 'Senegal',
             'Serbia', 'Sierra Leone', 'Singapore', 'Slovakia', 'Slovenia', 'Somalia', 'South Africa', 'Spain',
             'Sri Lanka', 'Sudan', 'Suriname', 'Sweden', 'Switzerland', 'Syria', 'Taiwan', 'Tanzania',
             'Thailand', 'Timor-Leste', 'Togo', 'Trinidad and Tobago', 'Tunisia', 'Turkey',
             'Uganda', 'Ukraine', 'United Arab Emirates', 'United Kingdom', 'United States', 'Uruguay', 'Uzbekistan',
             'Venezuela', 'Vietnam', 'Yemen', 'Zambia', 'Zimbabwe']
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']
chosen_word = random.choice(countries)
display = []
lives = 6
for letter in chosen_word:
    display += "_"
print(""" ___________.._______
| .__________))______|
| | / /      ||
| |/ /       ||
| | /        ||.-''.
| |/         |/  _  \
| |          ||  `/,|
| |          (\\`_.'
| |         .-`--'.
| |        /Y . . Y\
| |       // |   | \\
| |      //  | . |  \\
| |     ')   |   |   (`
| |          ||'||
| |          || ||
| |          || ||
| |          || ||
| |         / | | \
*********|_`-' `-' |***|
|"|*******\ \       '"|"|
| |        \ \        | |
: :         \ \       : :  sk
. .          `'       . .
""")
print("A country's name was assigned!")
end_game = False
count = 0
while not end_game:
    guess = str(input("Guess a letter: ")).strip().lower()
    count += 1
    for position, letter in enumerate(chosen_word):
        if letter == guess:
            display[position] = letter
    if guess not in display:
        lives -= 1
    display_b = ''
    for character in display:
        display_b += f" {character}"
    while lives > 0:
        print(display_b)
        print(stages[lives])
        print(f"You still have {lives} lives!")
        if count != 1:
            if guess in display:
                print("You already guessed that letter!")
                break
        break
    if lives == 0:
        print(display_b)
        print(stages[lives])
        print(f"YOU LOSE! The assigned word was: {chosen_word}")
        end_game = True
    if "_" not in display:
        print(display_b)
        print(stages[lives])
        print(f"CONGRATULATIONS! YOU'VE WON! The assigned word was: {chosen_word}")
        end_game = True
