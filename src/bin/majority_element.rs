use std::{
    collections::HashMap,
    io::{stdin, BufRead},
};

fn main() {
    // input:
    // n: count
    // 1 23 34: numbers whitespace seperated
    // output:
    // 1, if there is a number with more than n/2 counts, 0 otherwise
    let mut it = stdin().lock().lines();
    let _ = it.next().unwrap().unwrap();
    let numbers = it.next().unwrap().unwrap();
    let numbers: Vec<i32> = numbers
        .split(' ')
        .map(|x| x.parse::<i32>().unwrap())
        .collect();
    print!("{}", majority_element(&numbers))
}

fn majority_element(numbers: &[i32]) -> u8 {
    let mut number_counts: HashMap<&i32, usize> = HashMap::new();
    for number in numbers {
        number_counts.entry(number).or_default();
        let count = number_counts.get_mut(&number).unwrap();
        *count += 1;
        if *count > numbers.len() / 2 {
            return 1;
        }
    }
    0
}

#[cfg(test)]
mod tests {
    use crate::majority_element;

    #[test]
    fn given_more_than_half_when_called_then_returns_1() {
        // given
        let numbers = [1, 2, 2, 2, 3];

        // when
        let result = majority_element(&numbers);

        // then
        assert_eq!(result, 1);
    }

    #[test]
    fn given_less_than_half_when_called_then_returns_0() {
        // given
        let numbers = [1, 2, 2, 2, 3, 1];

        // when
        let result = majority_element(&numbers);

        // then
        assert_eq!(result, 0);
    }
}
