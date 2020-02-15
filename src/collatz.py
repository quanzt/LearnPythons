def collatz(number):
    res = None
    if number % 2 == 0:
        res = number // 2
    else:
        res = 3 * number + 1
    print(res)
    return res


def get_num():
    try:
        num = int(input())
        return collatz(num)
    except ValueError:
        print('Please enter an integer')


if __name__ == '__main__':
    print('Enter number:')
    getOne = get_num()

    while getOne != 1:
        getOne = get_num()

    print('You found one')
