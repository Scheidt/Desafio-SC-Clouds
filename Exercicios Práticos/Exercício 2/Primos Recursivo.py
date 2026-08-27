#-- Criar uma função em sua linguagem preferida. A função deve receber um numero N > 1 (validar o input), e retornar todos os números
#    primos até o número N. EX. p(2) = [2]; p(3) = [2, 3]; p(10) = [2, 3, 5, 7];

def isPrime(number, div = 2):
    if number == 2:
        return True
    elif number % div == 0:
        return False
    elif div * div > number:
        return True
    return isPrime(number, div+1)

def p(target, primes=None):
    if primes is None:
        primes = []

    while True:
        try:
            target = int(target)
            if target > 1:
                break
            else:
                print("O número deve ser um inteiro maior que um.")
        except ValueError:
            print("Deve ser um número.")

        target = input("O valor deve ser um número maior que um! Insira um novo número: ")

    if target == 2:
        primes.append(2)
        primes.reverse()
        return primes
    if isPrime(target):
        primes.append(target)
    return p(target - 1, primes)


while True:
    print(p(input("Insira um número: ")))