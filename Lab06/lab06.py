"""O objetivo desse código é definir funções que aplicam certas operações em
vetores, como soma de seus termos, e permitir que o usuário final consiga usar
estas para alcançar um resultado"""


def main() -> None:
    """Função principal do código"""
    vetor1_str = input()
    vetor1 = listificador(vetor1_str)
    while True:
        operação = input()

        if operação == "soma_vetores":
            vetor1 = soma_vetores(vetor1, listificador(input()))
        elif operação == "subtrai_vetores":
            vetor1 = subtrai_vetores(vetor1, listificador(input()))
        elif operação == "multiplica_vetores":
            vetor1 = multiplica_vetores(vetor1, listificador(input()))
        elif operação == "divide_vetores":
            vetor1 = divide_vetores(vetor1, listificador(input()))
        elif operação == "multiplicacao_escalar":
            escalar = int(input())
            vetor1 = multiplicacao_escalar(vetor1, escalar)
        elif operação == "n_duplicacao":
            vetor1 = n_duplicacao(vetor1, int(input()))
        elif operação == "soma_elementos":
            vetor1 = [soma_elementos(vetor1)]
        elif operação == "produto_interno":
            vetor1 = [produto_interno(vetor1, listificador(input()))]
        elif operação == "multiplica_todos":
            vetor1 = multiplica_todos(vetor1, listificador(input()))
        elif operação == "correlacao_cruzada":
            vetor1 = correlacao_cruzada(vetor1, listificador(input()))
        elif operação == "fim":
            break
        print(vetor1)


def listificador(nao_lista: str) -> list[int]:
    """Transforma uma string no formato N1,N2,... em uma lista de inteiros, com
    N_i sendo um inteiro qualquer.

    Parâmetros:
    não_lista -- string a ser transformada

    Retorna:
    list      -- lista no formato [N1, N2, ...]
    """
    if nao_lista is not None:
        lista = [int(x) for x in nao_lista.split(",")]
    else:
        lista = []
    return lista


def soma_vetores(vetor1: list[int], vetor2: list[int]) -> list[int]:
    """Soma os elementos de dois vetores.

    Parâmetros:
        vetor1  -- lista de números inteiros a serem somados
        vetor2  -- lista de números inteiros a serem somados

    Retorna:
        list    -- lista que contém a soma dos termos do vetor1 e vetor2
    """
    vetor_corrente = []

    if len(vetor1) > len(vetor2):
        vetor2 += (len(vetor1) - len(vetor2)) * [0]
    else:
        vetor1 += (len(vetor2) - len(vetor1)) * [0]
    for i in range(min(len(vetor1), len(vetor2))):
        soma = vetor1[i] + vetor2[i]
        vetor_corrente.append(soma)
    return vetor_corrente


def subtrai_vetores(vetor1: list[int], vetor2: list[int]) -> list[int]:
    """Subtrai os elementos de dois vetores.

    Parâmetros:
        vetor1  -- primeira lista de números inteiros
        vetor2  -- lista de números inteiros a serem subtraídos dos elementos
                   do vetor1

    Retorna:
        list    -- lista que contém a diferença dos termos do vetor1 e vetor2
    """
    vetor2 = [-x for x in vetor2]
    vetor_corrente = soma_vetores(vetor1, vetor2)
    return vetor_corrente


def multiplica_vetores(vetor1: list[int], vetor2: list[int]) -> list[int]:
    """Multiplica os elementos de dois vetores.

    Parâmetros:
        vetor1  -- primeira lista de números inteiros
        vetor2  -- lista de números inteiros que serão multiplicados

    Retorna:
        list    -- lista que contém o produto dos termos de vetor1 e vetor2
    """
    vetor_corrente = []

    if len(vetor1) > len(vetor2):
        vetor2 += (len(vetor1) - len(vetor2)) * [1]
    else:
        vetor1 += (len(vetor2) - len(vetor1)) * [1]
    for i in range(min(len(vetor1), len(vetor2))):
        produto = vetor1[i] * vetor2[i]
        vetor_corrente.append(produto)
    return vetor_corrente


def divide_vetores(vetor1: list[int], vetor2: list[int]) -> list[int]:
    """Divide os elementos de dois vetores.

    Parâmetros:
        vetor1  -- primeira lista de números inteiros
        vetor2  -- lista de números inteiros que serão os dividendos

    Retorna:
        list    -- lista que contém a divisão dos termos de vetor1 e vetor2
    """
    vetor_corrente = []

    if len(vetor1) > len(vetor2):
        vetor2 += (len(vetor1) - len(vetor2)) * [1]
    else:
        vetor1 += (len(vetor2) - len(vetor1)) * [0]
    for i in range(min(len(vetor1), len(vetor2))):
        divisão = vetor1[i] // vetor2[i]
        vetor_corrente.append(divisão)
    return vetor_corrente


def multiplicacao_escalar(vetor: list[int], escalar: int) -> list[int]:
    """Multiplica os elementos de um vetor por um escalar.

    Parâmetros:
        vetor1  -- lista de números inteiros
        escalar -- número inteiro

    Retorna:
        list    -- lista que contém o produto dos termos de vetor1 e o escalar
    """
    vetor_corrente = []

    for i in range(len(vetor)):
        produto_escalar = vetor[i] * escalar
        vetor_corrente.append(produto_escalar)
    return vetor_corrente


def n_duplicacao(vetor: list[int], n: int) -> list[int]:
    """Duplica o vetor n vezes em uma nova lista de inteiros.

    Parâmetros:
        vetor1  -- lista de números inteiros
        n       -- número inteiro

    Retorna:
        list    -- lista que contém as duplicações do vetor1
    """
    vetor_corrente = n * vetor
    return vetor_corrente


def soma_elementos(vetor: list[int]) -> int:
    """Soma todos os elementos de um vetor.

    Parâmetros:
        vetor1  -- lista de números inteiros

    Retorna:
        int     -- resultado da soma
    """
    soma_dos_elementos = 0
    for i in vetor:
        soma_dos_elementos += i
    vetor_corrente = soma_dos_elementos
    return vetor_corrente


def produto_interno(vetor1: list[int], vetor2: list[int]) -> int:
    """Multiplica os elementos de dois vetores e soma cada resultado.

    Parâmetros:
        vetor1  -- lista de números inteiros
        vetor2  -- lista de números inteiros a serem multiplicados

    Retorna:
        int    -- resultado da soma
    """
    produto_dos_elementos = multiplica_vetores(vetor1, vetor2)
    soma_dos_elementos = soma_elementos(produto_dos_elementos)
    vetor_corrente = soma_dos_elementos
    return vetor_corrente


def multiplica_todos(vetor1: list[int], vetor2: list[int]) -> list[int]:
    """Multiplica cada elemento de um vetor pela soma dos elementos do outro
    vetor.

    Parâmetros:
        vetor1  -- lista de números inteiros
        vetor2  -- lista de números inteiros a serem multiplicados

    Retorna:
        list    -- resultados das somas
    """
    vetor_corrente = []

    for i in range(len(vetor1)):
        vetor_corrente.append(vetor1[i] * soma_elementos(vetor2))
    return vetor_corrente


def correlacao_cruzada(vetor: list[int], mascara: list[int]) -> list[int]:
    """Multiplica n elementos de um vetor, começando do elemento 0, pelos
    elementos de um segundo vetor e soma esses produtos, tal que n é o tamanho
    do segundo vetor, dai repete o processo começando do elemento 1, assim
    sucessivamente até o que todos os elementos do primeiro vetor tenham
    sofrido alguma operação pelo menos uma vez. Daí retorna uma lista com
    os resultados, ordenados do primeiro ao último.

    Parâmetros:
        vetor1  -- lista de números inteiros
        mascara -- lista de números inteiros

    Retorna:
        list    -- resultados das operações
    """
    vetor_corrente = []

    for i in range(len(vetor) - len(mascara) + 1):
        soma = 0
        for j in range(len(mascara)):
            produto = vetor[i + j] * mascara[j]
            soma += produto
        vetor_corrente.append(soma)
    return vetor_corrente


if __name__ == '__main__':
    main()
