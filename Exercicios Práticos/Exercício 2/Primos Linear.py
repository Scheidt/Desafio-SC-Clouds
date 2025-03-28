#-- Criar uma função em sua linguagem preferida. A função deve receber um numero N > 1 (validar o input), e retornar todos os números
#    primos até o número N. EX. p(2) = [2]; p(3) = [2, 3]; p(10) = [2, 3, 5, 7];

def p(alvo):

    while not type(alvo) is int and alvo < 1:
        try:
            alvo = input("O valor deve ser um número maior que um! Insira um novo número: ")
            alvo = int(alvo)
        except:
            pass

    atual = 2
    primos = [2]
    if alvo == 2:
        return primos
    while atual < alvo:
        atual += 1
        for i in range(2, (atual//2)+1):
            print(f"i: {i}")
            if atual % i == 0:
                break
        else:
            primos.append(atual)
    return primos

print(p(10))