#-- Criar uma função em sua linguagem preferida. A função deve receber um numero N > 1 (validar o input), e retornar todos os números
#    primos até o número N. EX. p(2) = [2]; p(3) = [2, 3]; p(10) = [2, 3, 5, 7];

def p(target):

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

    new = 2
    primes = [2]
    while new < target:
        new += 1
        for i in range(2, (new//2)+1):
            if new % i == 0:
                break
        else:
            primes.append(new)
    return primes


while True:
    print(p(input("Insira um número: ")))