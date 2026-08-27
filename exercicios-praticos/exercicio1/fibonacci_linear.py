#Criar uma função em sua linguagem preferida. A função deve receber um numero N >= 0 (deve validar o input para a função), e retornar
#    o valor correspondente desse número na sequência Fibonacci. EX. fib(0) =0; fib(1) = 1; fib(2) = 1; fib(3) = 2; fib(5) = 5; fib(6) = 8.


def parse_input(maybe_number: str) -> int:
    """Tenta converter a entrada em um número maior ou igual a zero, ou levanta ValueError se falhar
    Args:
        maybe_number: Texto de entrada

    Returns:
        entrada convertida para int

    Raises:
        ValueError: Se o número for igual zero ou negativo
    """
    number = int(maybe_number)
    if number < 0:
        raise ValueError("O número deve ser maior ou igual a zero.")
    return number

def fib_linear(target: int) -> int:
    """
    Retorna o número N da sequência de Fibonacci, dada a entrada N
    Args:
        target: Qual a N posição da sequência
    
    Returns:
        Número na N posição

    Raises:
        TypeError: Se não receber um número inteiro (para chamadas de função pública)
        ValueError: Se receber um número inteiro menor que zero (para chamadas de função pública)

    """
    if not isinstance(target, int):
        raise TypeError("Deve ser um número inteiro")
    if target < 0:
        raise ValueError("O número deve ser maior ou igual a zero")
    
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

def main() -> None:
    while True:
        try:
            text = input("Insira um número: ")
        except (EOFError, KeyboardInterrupt):
            print()
            print("Execução cancelada pelo operador.")
            return
        try:
            position = parse_input(text)
            number = fib_linear(position)
            print(number)
            print()
        except ValueError:
            print("Deve ser um número inteiro maior ou igual a zero.")
            print()

if __name__ == "__main__":
    main()
