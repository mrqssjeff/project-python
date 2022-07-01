from prettytable import PrettyTable

table = PrettyTable()
table.add_column("Pokemon Name", ["Pikachu", "Bulbassaur", "Squirtle", "Charmander", "Gengar"])
table.add_column("Type", ["Electric", "Grass", "Water", "Fire", "Ghost"])
table.align = 'l'
print(table)
