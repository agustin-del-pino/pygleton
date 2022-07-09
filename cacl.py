import pygleton

_this = pygleton.Single(hola=None)

def add(a: int, b: int) -> int:
    _this.hola = "hola"
    return a+b


def sub(a: int, b: int) -> int:
    return a-b

