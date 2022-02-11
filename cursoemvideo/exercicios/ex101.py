def voto(ano): 
    from datetime import date
    atual = date.today().year 
    idade = atual - ano  
    if idade < 18:
        return f'Com {idade} anos: VOTO PROIBIDO!'
    elif idade >= 18 and idade < 65:
        return f'Com {idade} anos: VOTO OBRIGATÓRIO!'
    elif idade >= 65:
        return f'Com {idade} anos: VOTO FACULTATIVO!'


n = int(input('Digite seu ano de nascimento: '))
print(voto(n))
