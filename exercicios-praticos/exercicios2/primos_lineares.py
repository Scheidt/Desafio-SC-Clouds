#-- Criar uma função em sua linguagem preferida. A função deve receber um numero N > 1 (validar o input), e retornar todos os números
#    primos até o número N. EX. p(2) = [2]; p(3) = [2, 3]; p(10) = [2, 3, 5, 7];
from math import isqrt

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
    Retorna uma lista de todos os números primos até um número alvo 'N'.

    Faz o cálculo usando o crivo de Eratóstenes, que possui complexidade O(NloglogN):
    https://pt.wikipedia.org/wiki/Crivo_de_Erat%C3%B3stenes
    Args:
        target: Número limite 'N' a ser testado

    Returns:
        Lista de números inteiros de todos os números primos até 'N'

    Raises:
        TypeError: Se a entrada não for um int
        ValueError: Se a entrada for menor ou igual a um

    """
    if not isinstance(target, int):
        raise TypeError("Deve ser um número inteiro")
    if target <= 1:
        raise ValueError("O número deve ser maior que um")

    # Um bytearray gasta 1 byte por número, contra 8 de uma list (explicação detalhada no readme [1]).

    # É instanciado um array de bytes com N+1 posições, para poder considerar o 0 e ficar mais fácil para um usuário ler o array.
    # Dessa forma ler is_prime[i] == 1 verifica se exatamente 'i' é primo, que é mais lógico que verificar 'i' com is_prime[i-1].
    # Gasta um byte a mais, mas melhora imensamente a leitura.
    # Todos os números começam valor com '1', indicando que são possívelmente primos, e serão descartados
    # se descoberto que são múltiplos de dois fatores inteiros.
    is_prime = bytearray([1]) * (target + 1)
    is_prime[0] = is_prime[1] = 0

    # Só é necessário analisar os números abaixo da raiz do N, devido a natureza do crivo (explicação detalhada no readme [2])
    for prime in range(2, isqrt(target) + 1):
        if not is_prime[prime]: 
            continue# Pular números que já foram descartados como não primos. O resto do
                    # código executa só para números primos

        
        # Pega os múltiplos do número avaliado para remover (Explicação mais detalhada no Readme [2]).
        # Começa no quadrado do número. Não precisa avaliar multiplicadores menores que o próprio
        # multiplicado pois esses já teriam sido eliminados quano o multiplicando menor fosse
        # avaliado anteriormente.
        prime_squared = prime**2
        multiples = range(prime_squared, target + 1, prime)

        # Remove a "primazia" os múltiplos do número, partindo do quadrado do primo e seguindo na 
        # mesma lógica acima. Remover todos de uma vez é mais rápido que percorrer o array com um for,
        # pois é utilizada uma função CPython. O python também exige que ambos os arrays tenham o mesmo
        # comprimento, então é pego um slice do array principal
        is_prime[prime_squared::prime] = bytearray(len(multiples))

    # Converte o array em uma lista de ints normais e retorna
    return [number for number in range(target + 1) if is_prime[number]]


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
