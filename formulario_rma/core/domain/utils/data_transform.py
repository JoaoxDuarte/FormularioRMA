

def data_transform(number):
    if number > 11:
        return 'Dezembro'
    elif number > 10:
        return 'Novembro'
    elif number > 9:
        return 'Outubro'
    elif number > 8:
        return 'Setembro'
    elif number > 7:
        return 'Agosto'      
    elif number > 6:
        return 'Julho'
    elif number > 5:
        return 'Junho'
    elif number > 4:
        return 'Maio'
    elif number > 3:
        return 'Abril'
    elif number > 2:
        return 'Março'
    elif number > 1:
        return 'Fevereiro'
    elif number > 0:
        return 'Janeiro'
    elif number == 0:
        return 'Dezembro'
    return 'Janeiro'

