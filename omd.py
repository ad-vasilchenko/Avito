import random


def step1(emoji_list):
    print( "Утка-маляр 🦆 решила выпить зайти в бар.\n"
           "Взять ей зонтик? \n"
           f"{random.choice(emoji_list)}" )
    
    option = ''
    options = {'да': True, 'нет': False}
    while option not in options:
        print('Выберите: {}/{}'.format(*options))
        option = input()
    
    if options[option]:
        return step2_umbrella()
    return step2_no_umbrella()

def step2_no_umbrella():
    print("Утка не взяла зонтик. Пошел дождь.\n"
          "Утка промокла, надо что-то делать\n"
          f"Идти домой или купить новый шмот {random.choice(emoji_list)}")y

    option = ''
    options = {'домой': True, 'новый шмот': False}
    while option not in options:
        print('Выберите: {}/{}'.format(*options))
        option = input()
    
    if options[option]:
        return step3()
    return step3()


def step2_umbrella():
    print ("Утка взяла зонтик. А дождь как назло не пошел.\n"
           "А зонтик тащить с собой неудобно\n"
           "Выкинуть нафиг или отдать бомжу?")
    
    option = ''
    options = {'выкинуть': True, 'отдать': False}
    while option not in options:
        print('Выберите: {}/{}'.format(*options))
        option = input()
    
    if options[option]:
        return step3()
    return step3()

def step3():
    print("Вот и сказочке конец. А кто слушал, молодец!")

    option = ''
    options = {'заново': True, 'закончить': False}
    while option not in options:
        print('Выберите: {}/{}'.format(*options))
        option = input()
    
    if options[option]:
        return step1()


if __name__ == '__main__':
    emoji_list = [  "\U0001f600", "\U0001F606", "\U0001F923", "\U0001F604", "\U0001F605"]
    step1(emoji_list)
