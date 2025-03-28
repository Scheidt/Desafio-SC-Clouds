#Criar uma função em sua linguagem preferida. A função deve receber um numero N >= 0 (deve validar o input para a função), e retornar
#    o valor correspondente desse número na sequência Fibonacci. EX. fib(0) =0; fib(1) = 1; fib(2) = 1; fib(3) = 2; fib(5) = 5; fib(6) = 8.


def fib(alvo):
    while not type(alvo) is int and alvo < 0:
        try:
            alvo = input("O valor deve ser um número maior que 0! Insira um novo número: ")
            alvo = int(alvo)
        except:
            pass

    if alvo == 0:
        return 0
    elif alvo == 1:
        return 1
    last = 0
    new = 1
    while alvo > 1:
        last, new = new, last + new
        alvo -= 1
    return new

print(fib(10))