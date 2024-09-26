
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


a = int(input())
b = int(input())
c = a + b
d = a * b
if a > b:
    f = a - b
else:
    f = b - a

print(f"{c}\n{f}\n{d}")