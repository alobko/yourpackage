def try_me():
    from random import randrange
    arg = input('choose heads or tail :')

    if arg == 'heads':
        arg = 0
    else:
        arg = 1

    res = randrange(2)
    if res == arg:
        print('looser ...')
    else:
        print('niiiice, good choice')