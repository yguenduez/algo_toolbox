def money_change(money):
    amount_coins = 0
    while money > 0:
        amount_coins += 1
        money -= select_best_coin(money)
    return amount_coins

def select_best_coin(money):
    coins = [10,5,1]
    if coins[0] <= money:
        return coins[0]
    elif coins[1] <= money:
        return coins[1]
    else: return coins[2]


if __name__ == '__main__':
    money = int(input())
    print(money_change(money))

def test_money_change_given_sequence_of_coins_and_money_when_called_then_returns_number_of_coins():
    # given
    money_amount = 10
    
    # when
    amount_coins = money_change(money_amount)

    # then
    assert amount_coins == 1