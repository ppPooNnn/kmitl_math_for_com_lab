import random

m = random.randrange(1, 100)
s = 66050261

def decript(x0, y0, x1, y1) :
    secret_code = (y0 * (-x1 / (x0 - x1))) + (y1 * (-x0 / (x1 - x0)))
    return secret_code

def compute_equation(x) :
    y = (m * x) + s
    return y

def main() :
    y = []
    for x in range(1, 5) :
        y.append(compute_equation(x))
        print("y when x =", x, "is", y[x - 1])
    print(decript(1, y[1-1], 3, y[3-1]))
    return

if __name__ == "__main__" :
    main()