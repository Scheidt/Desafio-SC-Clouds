#Criar uma função em sua linguagem preferida. A função deve receber um numero N >= 0 (deve validar o input para a função), e retornar
#    o valor correspondente desse número na sequência Fibonacci. EX. fib(0) =0; fib(1) = 1; fib(2) = 1; fib(3) = 2; fib(5) = 5; fib(6) = 8.

def fib(pos, secondlast = 0, last = 1, cursor=1):
    while not type(pos) is int and pos < 0:
        try:
            pos = input("O valor deve ser um número maior que zero! Insira um novo número: ")
            pos = int(pos)
        except:
            pass
    if pos == 0:
        return 0
    if pos == cursor:
        return last
    else:
        return fib(pos, last, secondlast + last, cursor+1)

print(fib(10))