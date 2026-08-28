# Mudanças do código original

A primeira versão testava cada número por divisão por tentativa: para todo `n` até N, dividia por cada `divisor` de 2 até `n//2`, parando no primeiro divisor exato. Este método gerava uma complexidade de O((N^2)/logN), muito ineficiente para um problema deste tipo, e foi esse o retorno da SC Cloud na época "[...] as respostas sobre os números primos poderiam ser melhor otimizadas.".

Então lembrei do [Crivo de Eratóstenes](https://pt.wikipedia.org/wiki/Crivo_de_Erat%C3%B3stenes), que eu havia encontrado enquanto decidia meu tema do TCC. Ele é o método ideal dada a natureza da pergunta, que pede todos os primos dentro de um range pré-definido, que é exatamente sua função. O método posui complexidade `O(N log log N)`, pois re-aproveita contas anteriores. Todavia, esse método requer a criação de um array auxiliar do mesmo tamanho do range requisitado, gerando um espaço adicional que não era necessário no método anterior (O(N)).

Linear:

| | Original | Atual |
|---|---|---|
| Tempo | `O(N^2 / log N)` | `O(N log log N)` |
| Espaço adicional | `O(1)` | `O(N)` bytes |
| Tempo médio para N = 1.000.000 (10 execuções) | ~20 minutos`*` | 0.0530 s`**` |

`*` O tempo de execução é se aproxima do quadrático dado um N grande.

`**` aproximadamente 24.000x mais rápido

Recursivo:

A versão recursiva sofria do mesmo problema de ir até N//2 ao invés de raiz(N), o que criava um problema ainda pior devido ao limite de recursão do Python. A recursão repetia N vezes, então o `RecursionError` do Python (que possui limite padrão de ~1000 frames) travava a função em N = ~1.000, fechando a execução muito cedo, para limites pequenos, antes das ineficiencias de tempo se tornarem um problema relevante.

O código é muito semelhante ao linear, substituindo o laço de execução externo por uma chamada de recursão, fazendo com que um número chame a mesma função para o número seguinte. Como o laço externo agora só vai até a raiz de N (passo 6 da demonstração em [2]), a profundidade da pilha cai de N para `sqrt(N)`, passando o limite de N para ~1.000.000 (que antes era ~1.000).

Recebe um argumento e dois acumuladores, isso foi proposital e está explicado em [3].

| | Original | Atual |
|---|---|---|
| Tempo | `O(N^1.5 / log N)` | `O(N log log N)` |
| Espaço adicional | `O(N)` frames de pilha | `O(N)` bytes + `O(sqrt N)` frames de pilha |
| Maior N executável (limite de recursão padrão) | ~1.000 | ~1.000.000`*` |
| Tempo médio para N = 980 | 0,001061 s | 0,000056 s`**` |
| Tempo médio para N = 960.000 | `RecursionError` | 0,0472 s`***` |

`*` A profundidade da pilha é `sqrt(N)`, então o teto exato depende de quantos frames já estão em uso pelo chamador.

`**` aproximadamente 19x mais rápido, no maior N que a versão original conseguia processar.

`***` praticamente empatado com a versão linear (0,0469 s no mesmo N), todavia possui o limite de recursão máximo, que é uma limitação a mais se comparado com o linear

Referência: [Crivo de Eratóstenes](https://pt.wikipedia.org/wiki/Crivo_de_Erat%C3%B3stenes)

--------------------------

# Justificativas de Implementação

## [1] Por que utilizar um Bytearray ao invés de um list[bool]?:

### Armazenamento:
Uma lista padrão python (list[bool]) cria um array de pointers para singletons 'true' e false', significando um aumento de espaço no armazenamento de aproximadamente 8x, uam vez que pointers python 64-bit tem tamanho de 8 bytes (em python 32-bits são 4 bytes por pointer, então o aumento seria só 4x).
Sim, criar um byte é mais eficiente que um bool, já que um bool consiste em um pointer para um simpleton. Coisas de Python.

### Eficiência:
Esta redução de memória gera maior eficiência real na execução de código, uma vez que reduz o overhead de acesso à memória, que é o maior gargalo do código. O tempo de processador do código é relativamente curto, pois as contas realizadas são simples e executadas em poucos ciclos de clock, o real problema é que o código percorre várias vezes o array, e portanto precisa passar múltiplas vezes o array inteiro entre o cache e memória (RAM) e pelo barramento. Um aumento de ~8x do espaço de armazenamento significa uma taxa maior de cache miss (por exemplo, para um N= 2.000.000 significaria 2MB em um bytearray contra 16 em uma lista), obrigando o cache controller a realizar a operação demorada de mover o array da memória para o cache, múltiplas vezes por execução.

### "Por que não usar NumPy?" 
Uma versão ideal deste código utilizaria NumPy, pois sua vetorização e métodos altamente otimizados tornariam seu tempo de execução ainda mais rápido. Todavia, elegi não utilizar NumPy para tentar evitar a utilização de bibliotecas externas, utilizando somente funcionalidades do próprio Python. Python é uma linguagem famosa por suas inúmeras bibliotecas, ao ponto que uma grande quantidade de problemas classicos poderia ser resolvido com "from biblioteca import solução / solução()". Nesse caso eu estaria demonstrando meu conhecimento de bibliotecas, não de lógica de programação.
Portanto, escolhi não utilizar bibliotecas em geral, incluindo NumPy.

Fonte (preprint):
Mitrajit Ghorui. Benchmarking and Optimization of the Sieve of Eratosthenes in Python and C++. Authorea. 15 September 2025. DOI: https://doi.org/10.22541/au.175793436.63536096/v1

--------------------------


## [2] Por que iniciar a verificação por Primo^2 ao invés de percorrer os multiplicadores menores?

Essa escolha advém do fato de que todo múltiplo de um primo abaixo do seu quadrado já foi descartado por um primo menor. 

### Demonstração:

1. Assuma um primo `p` sendo analisado, e um múltiplo seu `p*k` menor que `p^2`, ou seja, `2 <= k < p`;
2. Como `k` é maior que um, ele possui pelo menos um fator primo `q`. E como `q <= k < p`, esse fator é necessariamente menor que `p`;
3. Se `q` divide `k`, então `q` também divide `p*k`. Ou seja, `p*k` é múltiplo de `q`;
4. Como `q` é menor que `p`, ele já foi analisado em uma iteração anterior, e sua passagem descartou os múltiplos de `q` a partir de `q^2`. E `p*k` está dentro desse trecho, pois `p*k > q*k >= q*q` (já que `p > q` e `k >= q`);
5. Portanto `p*k` já estava descartado antes de `p` ser analisado. Como isso vale para todo `k < p`, o primeiro múltiplo de `p` que ainda necessita ser analisado é `p*p = p^2`, e é por ele que a verificação deve começar.

Como consequência direta, o laço externo só precisa ir até a raiz de N:

6. Se `p > sqrt(N)`, então `p^2 > N`, e pelo passo 5 não existe nenhum múltiplo de `p` a descartar dentro do crivo. Por isso o laço percorre apenas o intervalo de 2 até `isqrt(N)`.

### Exemplo concreto:

Tomando `N = 100` e o primo `p = 7`, cujo quadrado é `49`:

1. Um múltiplo de `7` menor que `49` é `42 = 7*6`, ou seja, `k = 6`, e de fato `2 <= 6 < 7`;
2. `6` é maior que um, então possui fatores primos: `6 = 2*3`. Tomando `q = 3`, vale `3 <= 6 < 7`, isto é, `q` é menor que `p`;
3. `3` divide `6`, logo `3` também divide `42` (`42 = 3*14`). Ou seja, `42` é múltiplo de `3`;
4. Como `3 < 7`, o número `3` foi analisado antes de `7`, e sua passagem descartou `9, 12, 15, ..., 42, ...` a partir de `3^2 = 9`. E `42` está dentro desse trecho, pois `42 > 18 >= 9`;
5. Portanto `42` já estava marcado como não primo antes de `7` ser analisado. O mesmo vale para todos os outros múltiplos de `7` abaixo de `49` (`14` e `28` caíram na passagem do `2`, `21` e `42` na do `3`, `35` na do `5`) e por isso a passagem do `7` começa direto em `49`, marcando apenas `49, 56, 63, 70, 77, 84, 91, 98`;
6. O próximo primo, `11`, é maior que `sqrt(100) = 10`, e seu quadrado `121` já ultrapassa `N = 100`. Não há nenhum múltiplo de `11` a descartar dentro do crivo, então o laço externo para em `10` e os primos entre `11` e `100` são apenas lidos do array, sem nunca iniciar uma passagem própria.

--------------------------


## [3] Por que uma única função recursiva, e não um par "função pública + auxiliar recursiva"?

A recursão precisa carregar estado entre as chamadas (o candidato a primo da vez e o array de números), mas também precisa executar código que ocorreria somente na primeira execução (instanciar o array, verificar a entrada) para tal há duas formas de codificar:

1. Um par de wrapper + helper. Na qual o wrapper público recebe só `target` como argumento, e é responsavel por validar o input, montar o array e chamar uma segunda função recursiva "privada" (não existe função privada em Python, ele não impede o chamado delas), que carrega os acumuladores. É a estrutura mais comum em código de produção, pois a função pública abre somente os parâmetros que ficam a encargo do usuário e protege os acumuladores de serem passados diretamente, além de garantir que a validação será rodada, sem ser possível pulá-la enviando os acumuladores na chamada de função.
2. Uma função única com acumuladores opcionais. Os acumuladores ficam na própria assinatura com valor default, e um desses acumuladores identifica a primeira execução da recursão (`is_prime`, nesse caso) sendo esta primeira execução a única que valida o input e monta o array. É a mesma técnica que a versão original já usava com `found: list[int] | None = None`.

Foi escolhido o segundo método. Embora o primeiro método seja mais ideal para esse caso, por permitir que o wrapper instancie o array e faça a verificação de entrada, além de proteger os acumuladores de edição externa; todavia, dado que o desafio pedia para _"Criar **uma função** [...]._" e que _"**A função** deve receber um número N > 1 (validar
o input), e retornar todos os números primos até o número N"_. Dado que o enunciado está no singular, elegi desenvolver a solução em uma função única, por ser mais próximo do enunciado, mesmo que idealmente essa funcionalidade funcionaria melhor com um par de funções. 

Novamente, um solução envolvendo as duas funções seria ideal, pois o método atual possui os seguintes problemas (explicitados aqui para demonstrar que sei destes problemas, mas que o método utilizado foi uma escolha de implementação _apesar_ destes erros):

- A assinatura pública expõe dois parâmetros internos. Seria possível por exemplo chamar `primes_recursive(10, 5, bytearray(11))`, o que devolveria lixo sem validação nenhuma. Tentei deixar claro na docstring que os dois argumentos são acumuladores internos, mas isso não impede de um usuário incauto executar essa chamada.
- A validação passa a rodar apenas na chamada de entrada, e não em toda chamada. Chamar `primes_recursive(100, 2, bytearray(...))` executa corretamente e possivelmente daria um resultado correto se o bytearray for criado corretamente, mas a entrada não é verificada (o `bytearray` não ser `None` pula a verificação), isso significa que `primes_recursive("foo", "bar", bytearray(...))` não cai na verificação de entrada da função (Python não limita a entrada à tipagem fornecida) e flui até o primeiro erro de código, gerando um levante de erro com uma mensagem incorreta.

Nenhum desses pontos afeta o resultado ou a complexidade, dado que são problemas no acesso da função, não de algoritmo. Trocar para o par wrapper + helper é uma mudança simples, bastando mover o bloco `if is_prime is None` para uma função externa que chama a função recursiva e deixar o resto do corpo como está.