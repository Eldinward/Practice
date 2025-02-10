#Завдання-Перше:

n = int(input("Введіть число n: "))

for a in range(1, n + 1):
    for b in range(a, n + 1):
        for c in range(b, n + 1):
            if a * a + b * b == c * c:
                print(a, b, c)

#Завдання-Друге:

n = int(input("Введіть кількість рядків: "))
triangle = [[1] * (i + 1) for i in range(n)]

for i in range(2, n):
    for j in range(1, i):
        triangle[i][j] = triangle[i - 1][j - 1] + triangle[i - 1][j]

for row in triangle:
    print(row)

#Завдання-Третє:

n = 1000
sieve = [True] * (n + 1)
sieve[0] = sieve[1] = False

for i in range(2, int(n**0.5) + 1):
    if sieve[i]:
        for j in range(i * i, n + 1, i):
            sieve[j] = False

primes = [i for i in range(n + 1) if sieve[i]]
print(primes)

#Завдання-Четверте:

n = int(input("Введіть число: "))
factors = []
d = 2

while d * d <= n:
    while n % d == 0:
        factors.append(d)
        n //= d
    d += 1

if n > 1:
    factors.append(n)

print("Множники:", factors)

#Завдання-П'яте:

def is_palindrome(num):
    return str(num) == str(num)[::-1]

for num in range(1, 100):
    square = num ** 2
    if is_palindrome(num) and is_palindrome(square):
        print(num, "=>", square)

#Завдання-Шосте:

def number_to_words(n):
    ones = ["", "один", "два", "три", "чотири", "п’ять", "шість", "сім", "вісім", "дев’ять"]
    teens = ["десять", "одинадцять", "дванадцять", "тринадцять", "чотирнадцять", "п’ятнадцять", "шістнадцять", "сімнадцять", "вісімнадцять", "дев’ятнадцять"]
    tens = ["", "десять", "двадцять", "тридцять", "сорок", "п’ятдесят", "шістдесят", "сімдесят", "вісімдесят", "дев’яносто"]
    hundreds = ["", "сто", "двісті", "триста", "чотириста", "п’ятсот", "шістсот", "сімсот", "вісімсот", "дев’ятсот"]
    
    if n == 1000:
        return "тисяча"
    
    result = []
    
    h = n // 100
    t = (n % 100) // 10
    o = n % 10
    
    if h > 0:
        result.append(hundreds[h])
    
    if t == 1:
        result.append(teens[o])
    else:
        if t > 0:
            result.append(tens[t])
        if o > 0:
            result.append(ones[o])
    
    return " ".join(result)

num = int(input("Число від 1 до 1000: "))
if 1 <= num <= 1000:
    print(number_to_words(num))
else:
    print("Не в межах, повторіть")

#Завдання-Сьоме:

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

n = int(input("Введіть число n: "))

for i in range(n, 2 * n - 1):
    if is_prime(i) and is_prime(i + 2):
        print(i, i + 2)

#Завдання-Восьме:

import textwrap

text = "В осини листя жотіє, скоро почнется зима."
n = 50

print("\n\n".join(textwrap.fill(para, n) for para in text.split("\n\n")))
