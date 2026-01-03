# Номінали монет
COINS = [50, 25, 10, 5, 2, 1]


def find_coins_greedy(amount):

    # Жадібний алгоритм видачі решти
    
    result = {}

    for coin in COINS:
        if amount >= coin:
            count = amount // coin
            result[coin] = count
            amount -= coin * count

    return result


def find_min_coins(amount):

    # Алгоритм динамічного програмування для мінімальної кількості монет

    dp = [float("inf")] * (amount + 1)
    dp[0] = 0

    last_coin = [0] * (amount + 1)

    for coin in COINS:
        for i in range(coin, amount + 1):
            if dp[i - coin] + 1 < dp[i]:
                dp[i] = dp[i - coin] + 1
                last_coin[i] = coin

    # відновлення набору монет
    result = {}
    current = amount

    while current > 0:
        coin = last_coin[current]
        result[coin] = result.get(coin, 0) + 1
        current -= coin

    return result


# ---------------- ПЕРЕВІРКА РОБОТИ ----------------
if __name__ == "__main__":
    amount = 113

    print("Сума для видачі:", amount)

    greedy_result = find_coins_greedy(amount)
    dp_result = find_min_coins(amount)

    print("\nЖадібний алгоритм:")
    print(greedy_result)

    print("\nАлгоритм динамічного програмування:")
    print(dp_result)

    # Перевірка, що обидва алгоритми дають правильну суму
    greedy_sum = sum(k * v for k, v in greedy_result.items())
    dp_sum = sum(k * v for k, v in dp_result.items())

    print("\nПеревірка коректності:")
    print("Жадібний алгоритм дає суму:", greedy_sum)
    print("Динамічне програмування дає суму:", dp_sum)
