text1 = str(input('Digite o primeiro texto: ')).strip()
text2 = str(input('Digite o segundo texto: ')).strip()
print(f'A quantidade de caracteres em "{text1}" é {len(text1) - text1.count(" ")}')
print(f'A quantidade de caracteres em "{text2}" é {len(text2) - text2.count(" ")}')
print(f'''As strings possuem a mesma quantidade de caracteres?
{bool(len(text1) == len(text2))}''')
print(f'As strings são iguais? {bool(text1 == text2)}')
