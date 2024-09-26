def new_format(value):
    formatted_value = f'{int(value):,}'.replace(',', '.')
    return formatted_value





assert new_format("1000000") == "1.000.000"
assert new_format("100") == "100"
assert new_format("1000") == "1.000"
assert new_format("100000") == "100.000"
assert new_format("10000") == "10.000"
assert new_format("0") == "0"
print('SUCCES')





def is_leap(year):
    leap = False

    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

    return leap


year = int(input())
print(is_leap(year))


if __name__ == '__main__':
    n = int(input())
    result = ''.join(str(i) for i in range(1, n + 1))
    print(result)


if __name__ == '__main__':

    def check_number(n):
        if n % 2 != 0:
            print("Weird")
        elif n % 2 == 0 and 2 <= n <= 5:
            print("Not Weird")
        elif n % 2 == 0 and 6 <= n <= 20:
            print("Weird")
        elif n % 2 == 0 and n > 20:
            print("Not Weird")

n = int(input().strip())
check_number(n)
