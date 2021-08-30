def foo1(value):
    if value:
        return value
    else:
        return None


def foo2(value):
    """纯return语句，相当于`return None`"""
    if value:
        return value
    else:
        return


def foo3(value):
    """无return语句，也相当于`return None"""
    if value:
        return value

