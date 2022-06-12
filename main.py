def test1():
    print('Задание №1')
    var_int = int(10)
    var_float = float(8.4)
    var_str = str('No')

    big_int = var_int * 3.5
    var_float -= 1
    print(var_int / var_float)
    print(big_int / var_float)
    var_str = var_str * 2 + "Yes" * 3
    print(var_int, var_float, big_int, var_str)


def test2():
    print('Задание №2')
    x = int(10)
    y = float(8.4)

    print(x == x and x >= y, y < x and y != x, y > x and x != y, x == y and y == x)
    print(y == x or x != y, x == y or y != x, x != x or x >= y, y == x or y != x)
    print('Text 1' != 'text 1' and 'text 1' == 'text 1')


def test3():
    print('Задание №3')
    x = int(10)
    y = float(8.4)

    if x > 0:
        print(1)
    elif y == 0:
        print(0)
    else:
        print(-1)


def test4():
    print('Задание №4')
    x = int(10)
    y = float(8.4)

    if x > y:
        z = x - y
    elif x < y:
        z = x + y
    elif x != y:
        z = x / y
    else:
        z = x * y
    print(z)


def test5():
    print('Задание №5')
    a, b = 0, 1
    c = 0

    for i in range(21):
        a, b = b, a + b
        if i >= 5:
            print(b, end='; ')
    print('\n')
    for i in range(0, 21, 1):
        print(i, end='; ')
    print('\n')
    for i in range(-1, -21, -3):
        print(i, end='; ')
    print('\n')
    while c < 100:
        c += 10
        print(c, end='; ')


def test6():
    print('Задание №6')
    x = '12345678'
    y = '123456789012345'
    s = x[-2:-1]
    x = x.replace(x[0], "", 1)
    x = x.replace(x[1], "", 1)
    x = x[0:-3]
    x = x + s
    print(len(x))

    print(y[:8])
    print(y[int(len(y) / 2 - 2):int(len(y) / 2 + 2):])
    print(y[2::3])


def test7():
    print('Задание №7')
    x = [1, 2, 3, 4, 5]
    y = [-1, -2, -3, -4, -5]
    v = []

    print(x[1])

    y[-1] = -6
    print(y)

    v.extend(x)
    v.extend(y)
    print(v)

    u = v[1:-2:2]
    print(u)

    u.append(-5)
    u.append(-7)
    print(u)


def test8():
    print('Задание №8')
    num = []
    text = ['Текст, строка 1', 'Текст, строка 2', 'Текст, строка 3', 'Текст, строка 4']
    for i in range(len(text)):
        print(text[i])

    for i in range(len(text)):
        text[i] = text[i] + '-'
        print(text[i])

    for i in range(1, 20, 2):
        num.append(float(i))
    print(num)


if __name__ == '__main__':
    test1()
    test2()
    test3()
    test4()
    test5()
    test6()
    test7()
    test8()
