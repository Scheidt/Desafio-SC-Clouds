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

def p(alvo, lista = []):

    while not type(alvo) is int and alvo < 1:
        try:
            alvo = input("O valor deve ser um número maior que um! Insira um novo número: ")
            alvo = int(alvo)
        except:
            pass
    if alvo == 2:
        lista.append(2)
        lista.reverse()
        return lista
    if isPrime(alvo):
        lista.append(alvo)
    return p(alvo - 1, lista)


print(p(10))