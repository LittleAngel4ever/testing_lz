import math

def logarimf(f, g, h):
    result = (math.log2(f) + g / (h - 1))
    return result

def main():
    try:
        f = float(input("Введите f: "))
        g = float(input("Введите g: "))
        h = float(input("Введите h: "))
    except ValueError:
        print("The line must contain forward")
        raise SystemExit
    if f <= 0:
        print(f"f must be positive, received f={f}")
        raise SystemExit
    if h == 1:
        print("h - 1 = 0, division by zero")
        raise SystemExit
    print(function(f, g, h))


if __name__ == "__main__":
    main()