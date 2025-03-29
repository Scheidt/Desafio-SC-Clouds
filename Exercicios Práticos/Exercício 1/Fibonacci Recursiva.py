#Criar uma função em sua linguagem preferida. A função deve receber um numero N >= 0 (deve validar o input para a função), e retornar
#    o valor correspondente desse número na sequência Fibonacci. EX. fib(0) =0; fib(1) = 1; fib(2) = 1; fib(3) = 2; fib(5) = 5; fib(6) = 8.

def fib(pos, secondlast = 0, last = 1, cursor=1):

    while True:
        try:
            pos = int(pos)
            if pos >= 0:
                break
            else:
                print("O número deve ser positivo.")
        except ValueError:
            print("Deve ser um número.")
        
        pos = input("O valor deve ser um número maior que zero! Insira um novo número: ")

    if pos == 0:
        return 0
    if pos == cursor:
        return last
    else:
        return fib(pos, last, secondlast + last, cursor+1)

while True:
    print(fib(input("Insira um número: ")))