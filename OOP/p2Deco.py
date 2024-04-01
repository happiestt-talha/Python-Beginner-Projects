def nar(h):
    def beep():
        print('G Bosss Aa gy o??')
        h()
        print('Ab nikal bhi jaiy')
    return beep


@nar
def hello():
    print('Hello')


@nar
def pak():
    print('Marny Ki Jagha Welcome')


pak()
hello()
