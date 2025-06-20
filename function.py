class Except(Exception):
    pass

import math

def logarifm(f, g, h):
    try:
        if f <= 0:
            raise Except
        result = (math.log2(f) + g / (h - 1))
    except TypeError:
        result = "The line must contain forward"
    except ZeroDivisionError:
        result = "h - 1 = 0, division by zero"
    except ValueError:
        result = "The line must be non-empty"
    except Except:
        result = "f must be positive, received f={f}"
    return result

def main():
    print(logarifm(" ", " ", " "))

if __name__ == "__main__":
    main()