use std::io::{stdin, BufRead};

fn main() {
    let mut i = stdin().lock().lines();
    let money: u32 = i.next().unwrap().unwrap().parse().unwrap();

    let denominators = [1, 3, 4];
    print!("{}", db_coins(&denominators, money))
}

fn db_coins(denoms: &[u32], change: u32) -> u32 {
    let mut min_num_coins = vec![0];
    for m in 1..=change {
        min_num_coins.push(u32::MAX);
        for coin in denoms {
            if m >= *coin {
                let num_coins = min_num_coins[(m - coin) as usize] + 1;
                if num_coins < min_num_coins[m as usize] {
                    min_num_coins[m as usize] = num_coins;
                }
            }
        }
    }
    return min_num_coins[change as usize];
}

fn greedy_coins(denoms: &[u32], change: u32) -> u32 {
    let mut current_change = change;
    let mut amount_coins = 0;
    while current_change > 0 {
        let biggest_coin = get_largest_coin(denoms, current_change);
        if biggest_coin == 0 {
            return amount_coins;
        }
        current_change -= biggest_coin;
        amount_coins += 1;
    }
    amount_coins
}

fn get_largest_coin(demons: &[u32], change: u32) -> u32 {
    for denom in demons.iter().rev() {
        if change >= *denom {
            return *denom;
        }
    }
    0
}

#[cfg(test)]
mod tests {
    use crate::{db_coins, get_largest_coin, greedy_coins};

    #[test]
    fn get_largest_coin_given_enough_change_returns_greatest_denominator() {
        // given
        let change = 10;
        let denoms = [1, 4, 7];

        // when
        let coin = get_largest_coin(&denoms, change);

        // then
        assert_eq!(coin, 7);
    }

    #[test]
    fn change_dynamic_programming_given_change_and_denominators_when_called_then_returns_optimal_number_of_coins(
    ) {
        // given
        let demoniations = [1, 8, 20];
        let change = 32;

        // when
        let needed_coins = db_coins(&demoniations, change);

        // then
        assert_eq!(needed_coins, 4);
    }

    #[test]
    fn find_smallest_int_where_greedy_fails() {
        let denoms = [1, 8, 20];
        for money in 1..40 {
            //           println!("{money}");
            //            assert_eq!(db_coins(&denoms, money), greedy_coins(&denoms, money))
        }
    }

    #[test]
    fn change_greedy_given_change_and_denominators_when_called_then_returns_optimal_number_of_coins(
    ) {
        // given
        let demoniations = [1, 8, 20];
        let change = 32;

        // when
        let needed_coins = greedy_coins(&demoniations, change);

        // then
        assert_eq!(needed_coins, 6);
    }
}
