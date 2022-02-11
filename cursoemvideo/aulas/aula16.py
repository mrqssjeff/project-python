pizza = ('Muçarela', 'Pepperoni', 'Calabresa', 'Atum')
#for c in pizza:
  #  print(f'Eu vou comer pizza de {c}!')

#mostrar posição
#for c in range(0, len(pizza)):
#print(f'Vou comer pizza de {pizza[c]} na posição {c}')

for pos, comida in enumerate(pizza):
    print(f'Comi pizza de {comida} na posição {pos}')
