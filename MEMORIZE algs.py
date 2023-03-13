# chess board 1
for x in range(8):
    if (x % 2 == 0):
        for y in range(8):
            if (y % 2 == 0):
                print("()", end="\t")
            else:
                print("[]", end="\t")
    else:
        for y in range(8):
            if (y % 2 == 0):
                print("[]", end="\t")
            else:
                print("()", end="\t")
    print("\n")

# chessboard 2
for y in range(4):
    for x in range(8):
        if x % 2 == 0:
            print("+", end="\t")
        else:
            print("-", end="\t")
    print("")
    for x in range(8):
        if x % 2 == 0:
            print("-", end="\t")
        else:
            print("+", end="\t")
    print("")
print("")  # not necessary,used as an extra line to separate chessboards 2 and 3 by a blank line in console

# chessboard 3
for y in range(8):
    for x in range(8):
        if x % 2 == 0:
            print("@", end="\t")
        else:
            print("&", end="\t")
    print("\n")


# recursion (function that returns itself, )
def recursion(a):
    if (a > 0):
        result = a + recursion(a - 1)
    else:  # -break point
        result = 1
    return result


print(recursion(5))


# fibonacci  (1,1,2,3,5,8,13,21,34...) (Fn = Fn-1 + Fn-2)
def fibonacci(h):
    if h in {0, 1}:  # -break point
        return h
    return fibonacci(h - 1) + fibonacci(h - 2)


print(fibonacci(9))


# factorial (k!)
def factorial(k):
    if k <= 0:  # -break point
        return 1
    return k * factorial(k - 1)


print(factorial(5))

#closures
def outer():
    n = 3

    def inner():
        nonlocal n
        n += 1
        print(n)
    return inner
x = outer()
x()

def multiply(n):
    def inner(m):
        print(n*m)
        return n * m

    return inner


fn = multiply(5)
fn(5)

# -----------------------------------------------------------------------------------------------------------------------
