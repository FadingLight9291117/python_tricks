def validate1(name):
    if len(name) < 10:
        raise ValueError


class NameTooShortError(ValueError):
    pass


def validate2(name):
    if len(name) < 10:
        raise NameTooShortError(name)
