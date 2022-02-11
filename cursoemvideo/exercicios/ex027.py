nome = str(input('Digite seu nome completo: ')).strip()
print(f'''Olá, seu \033[33mprimeiro\033[m nome é {nome.split()[0].title()}\n
Seu \033[34múltimo\033[m nome é {nome.split()[-1].title()}''')