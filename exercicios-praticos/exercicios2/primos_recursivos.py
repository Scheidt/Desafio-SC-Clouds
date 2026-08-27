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

def is_prime(number: int, divisor: int = 2) -> bool:
    """
    Informa se o número recebido é primo
    Args:
        number: Número a ser testado, deve ser maior que um
        divisor: Acumulador interno, divisor candidato da vez

    Returns:
        True se number for primo, False caso contrário

    """
    if number == 2:
        return True
    if number % divisor == 0:
        return False
    if divisor * divisor > number:
        return True
    return is_prime(number, divisor + 1)

def primes_recursive(target: int, found: list[int] | None = None) -> list[int]:
    """
    Retorna todos os números primos até N, dada a entrada N
    Args:
        target: Limite superior da busca, incluso
        found: Acumulador interno, primos já encontrados em ordem decrescente

    Returns:
        Lista crescente dos primos menores ou iguais a N

    Raises:
        TypeError: Se não receber um número inteiro (para chamadas de função pública)
        ValueError: Se receber um número inteiro menor ou igual a um (para chamadas de função pública)
        RecursionError: Se N ultrapassar o limite de recursão do Python (~1000)

    """
    if not isinstance(target, int):
        raise TypeError("Deve ser um número inteiro")
    if target <= 1:
        raise ValueError("O número deve ser maior que um")

    if found is None:
        found = []

    if target == 2:
        found.append(2)
        found.reverse()
        return found
    if is_prime(target):
        found.append(target)
    return primes_recursive(target - 1, found)

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
            found = primes_recursive(limit)
            print(found)
            print()
        except ValueError:
            print("Deve ser um número inteiro maior que um.")
            print()
        except RecursionError:
            print("Número grande demais para a versão recursiva.")
            print()

if __name__ == "__main__":
    main()
