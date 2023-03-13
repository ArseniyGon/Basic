def dec1(input_func):
    def output_func():
        print("===")
        input_func()
        print("===")

    return output_func


@dec1
def sum1():
    print("sum")


sum1()


def dec2(input_func):
    def output_func(*args):
        x = args[0]
        y = args[1]
        if x > 5: print("---")
        input_func(x, y)
        print("---")

    return output_func


@dec2
def sum2(x, y):
    print(x + y)


sum2(6, 5)


def dec3(input_func):
    def output_func(*args):
        x = args[0]
        y = args[1]
        if x > 5: print("!!!")
        z = input_func(x, y)
        print("!!!")
        return z

    return output_func


@dec3
def sum3(a, b):
    return a + b


print(sum3(7, 5))


def decorator1(in_f):
    def out_f():
        print("*****")
        in_f()
        print("*****")

    return out_f


@decorator1
def func_print():
    print("first decorator")


func_print()

#
print("------------------------------------------")

def decorator2(input_f):
    def output_f(*args):
        x = args[0]
        y = args[1]
        if x < 4: print("negative balance")
        input_f(x, y)

    return output_f


@decorator2
def subtract(x, y):
    print(x - y)


subtract(3, 6)

#
print("------------------------------------------")

def decorator3(in_func):
    def out_func(*args):
        a = args[0]
        b = args[1]
        print("...")
        c = in_func(a,b)
        # if c < 0: return
        print(c)
        print("...")
        return c

    return out_func


@decorator3
def withdrawal(a, b):
    return a-b


r=withdrawal(50, 75)
r1=withdrawal(100, 75)
r2=withdrawal(25, 75)

print(withdrawal(50, 75))

def my_function(x):
    return 5 * x


def f1(y):
    z = y(50)
    print(z)

f1(my_function)


