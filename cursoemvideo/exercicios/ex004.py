n = str(input('Digite algo:')).strip()
print(f'''O tipo primitivo desse valor é {type(n)}
Só tem espaços? {n.isspace()}')
Só tem números? {n.isnumeric()}''')
