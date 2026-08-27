#Criar uma função em sua linguagem preferida. A função deve receber um numero N >= 0 (deve validar o input para a função), e retornar
#    o valor correspondente desse número na sequência Fibonacci. EX. fib(0) =0; fib(1) = 1; fib(2) = 1; fib(3) = 2; fib(5) = 5; fib(6) = 8.


def fib(target):
    while True:
        try:
            target = int(target)
            if target >= 0:
                break
            else:
                print("O número deve ser positivo.")
        except ValueError:
            print("Deve ser um número.")
        
        target = input("O valor deve ser um número maior que zero! Insira um novo número: ")

    if target == 0:
        return 0
    elif target == 1:
        return 1
    last = 0
    new = 1
    while target > 1:
        last, new = new, last + new
        target -= 1
    return new

while True:
    print(fib(input("Insira um número: ")))