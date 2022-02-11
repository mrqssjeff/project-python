nome = str(input('Qual o seu nome? ')).strip()
print(f'Seu nome tem \033[4mSilva\033[m? {"silva" in nome.lower()}')


