import numbers


def add(a,b):
    if(isinstance(a,numbers.Number) and isinstance(b,numbers.Number)):
        return a + b
    else:
        return None

def sub(a,b):
    if(isinstance(a,numbers.Number) and isinstance(b,numbers.Number)):
        return a - b
    else:
        return None

def mul(a,b):
    if(isinstance(a,numbers.Number) and isinstance(b,numbers.Number)):
        return a * b
    else:
        return None

def div(a,b):
    if(isinstance(a,numbers.Number) and isinstance(b,numbers.Number)):
        try:
            result = a /b
            return result
        except ZeroDivisionError:
            return None
    else:
        return None


