use std::io::{self, BufRead};

fn max_product(prices: &[u64], clicks: &[u64]) -> u64 {
    let mut prices: Vec<u64> = prices.into();
    let mut clicks: Vec<u64> = clicks.into();

    prices.sort();
    clicks.sort();

    let mut result = 0;
    for i in 0..prices.len() {
        result += prices[i] * clicks[i];
    }

    return result;
}

fn main() {
    let stdin = io::stdin();
    let mut it = stdin.lock().lines();
    let _ = it.next().unwrap().unwrap();
    let line_1 = it.next().unwrap().unwrap();
    let line_2 = it.next().unwrap().unwrap();
    let prices_str: Vec<&str> = line_1.split(' ').collect();
    let prices: Vec<u64> = prices_str
        .iter()
        .map(|pr| pr.parse::<u64>().unwrap())
        .collect();
    let clicks_str: Vec<&str> = line_2.split(' ').collect();
    let clicks : Vec<u64>= clicks_str
        .iter()
        .map(|pr| pr.parse::<u64>().unwrap())
        .collect();

    println!("{}", max_product(&prices, &clicks))
}

#[cfg(test)]
mod tests {
    use crate::max_product;

    #[test]
    fn max_product_works() {
        // given
        let prices = [23];
        let clicks = [39];

        // when
        let result = max_product(&prices, &clicks);

        // then
        assert_eq!(result, 897);
    }
}
