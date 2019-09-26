def hello(func):
    def wrapper():
        print('hihi')
        func()
        print('hahahahaha')
    return wrapper

@hello
def bye():
    print('byebye')

bye()