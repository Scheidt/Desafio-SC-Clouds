#-- Criar uma função em sua linguagem preferida. A função deve receber um numero N > 1 (validar o input), e retornar todos os números
#    primos até o número N. EX. p(2) = [2]; p(3) = [2, 3]; p(10) = [2, 3, 5, 7];


def parse_input(maybe_number: str) -> int:
    """Tenta converter a entrada em um número maior que um, ou levanta ValueError se falhar
    Args:
        maybe_number: Texto de entrada

    Returns:
        entrada convertida para int

    Raises:
        ValueError: Se não for um inteiro ou se for menor ou igual a um
    """
    number = int(maybe_number)
    if number <= 1:
        raise ValueError("O número deve ser maior que um.")
    return number

def primes_linear(target: int) -> list[int]:
    """
    Retorna todos os números primos até N, dada a entrada N
    Args:
        target: Limite superior da busca, incluso

    Returns:
        Lista crescente dos primos menores ou iguais a N

    Raises:
        TypeError: Se não receber um número inteiro (para chamadas de função pública)
        ValueError: Se receber um número inteiro menor ou igual a um (para chamadas de função pública)

    """
    if not isinstance(target, int):
        raise TypeError("Deve ser um número inteiro")
    if target <= 1:
        raise ValueError("O número deve ser maior que um")

    found = [2]
    new = 2
    while new < target:
        new += 1
        for divisor in range(2, (new//2)+1):
            if new % divisor == 0:
                break
        else:
            found.append(new)
    return found

def main() -> None:
    while True:
        try:
            text = input("Insira um número: ")
        except (EOFError, KeyboardInterrupt):
            print()
            print("Execução cancelada pelo operador.")
            return
        try:
            limit = parse_input(text)
            found = primes_linear(limit)
            print(found)
            print()
        except ValueError:
            print("Deve ser um número inteiro maior que um.")
            print()

if __name__ == "__main__":
    main()
