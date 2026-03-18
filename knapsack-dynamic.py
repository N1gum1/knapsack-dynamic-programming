
import matplotlib.pyplot as plt


def knapsack(valores, pesos, capacidade):
    n = len(valores)

    if len(valores) != len(pesos):
        raise ValueError("Listas de valores e pesos devem ter o mesmo tamanho")

    # Criando a tabela DP
    dp = [[0 for _ in range(capacidade + 1)] for _ in range(n + 1)]

    # Preenchendo a tabela
    for i in range(1, n + 1):
        for w in range(1, capacidade + 1):
            if pesos[i - 1] <= w:
                dp[i][w] = max(
                    dp[i - 1][w],
                    dp[i - 1][w - pesos[i - 1]] + valores[i - 1]
                )
            else:
                dp[i][w] = dp[i - 1][w]

    # Descobrindo itens escolhidos
    w = capacidade
    itens_escolhidos = []

    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            itens_escolhidos.append(i - 1)
            w -= pesos[i - 1]

    itens_escolhidos.reverse()

    return dp[n][capacidade], itens_escolhidos, dp


def mostrar_tabela(dp):
    print("\nTabela DP:\n")
    for linha in dp:
        print(" ".join(f"{v:3}" for v in linha))


def plotar_mochila(valores, itens_escolhidos):
    labels = [f"Item {i}" for i in range(len(valores))]
    cores = ["green" if i in itens_escolhidos else "gray" for i in range(len(valores))]

    plt.figure(figsize=(8, 5))
    plt.bar(labels, valores, color=cores)
    plt.title("Itens escolhidos na mochila")
    plt.xlabel("Itens")
    plt.ylabel("Valor")
    plt.show()


if __name__ == "__main__":
    valores = [60, 100, 120]
    pesos = [10, 20, 30]
    capacidade = 50

    valor_max, itens, dp = knapsack(valores, pesos, capacidade)

    print(f"\nValor máximo: {valor_max}")
    print(f"Itens escolhidos: {itens}")

    mostrar_tabela(dp)
    plotar_mochila(valores, itens)
    
