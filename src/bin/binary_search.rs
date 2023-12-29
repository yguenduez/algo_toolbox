use std::io::{stdin, BufRead};

fn main() {
    // input:
    // n: num keys
    // key_1 key_2 ...
    // m: num queries
    // query1 query2
    let mut it = stdin().lock().lines();
    let _ = it.next().unwrap().unwrap();
    let keys = it.next().unwrap().unwrap();
    let _ = it.next().unwrap().unwrap();
    let queries = it.next().unwrap().unwrap();

    let arr: Vec<i32> = keys.split(' ').map(|x| x.parse::<i32>().unwrap()).collect();
    let query_keys: Vec<i32> = queries
        .split(' ')
        .map(|x| x.parse::<i32>().unwrap())
        .collect();

    for key in query_keys {
        let value = {
            match bin_search(&arr, key, 0, arr.len() - 1) {
                Some(val) => val as i32,
                None => -1,
            }
        };
        print!("{value} ")
    }
}

fn bin_search(arr: &[i32], key: i32, left: usize, right: usize) -> Option<usize> {
    if left > right {
        return None;
    }

    let length = right - left;
    let mid = left + length / 2;
    if arr[mid] < key {
        bin_search(arr, key, mid + 1, right)
    } else if arr[mid] > key {
        if mid == 0 {
            return None;
        }
        bin_search(arr, key, left, mid - 1)
    } else {
        return Some(mid);
    }
}

#[cfg(test)]
mod tests {
    use crate::bin_search;

    #[test]
    fn binary_search_given_search_key_when_called_with_array_containing_key_then_returns_index() {
        // given
        let my_arr = [1, 2, 3, 4, 5];
        let key = 5;

        // when
        let index = bin_search(&my_arr, key, 0, my_arr.len() - 1);

        // then
        assert_eq!(index, Some(4));
    }
    #[test]
    fn binary_search_given_search_key_when_called_with_array_not_containing_key_then_returns_index()
    {
        // given
        let my_arr = [1, 2, 3, 4, 5];
        let key = 6;

        // when
        let index = bin_search(&my_arr, key, 0, my_arr.len() - 1);

        // then
        assert_eq!(index, None);
    }

    #[test]
    fn binary_search_works_with_given_stdin_input() {
        // given
        let arr = [1, 5, 8, 12, 13];
        let qs = [8, 1, 23, 1, 11, 5, 12];
        //         5
        // 1 5 8 12 13
        // 5
        // 8 1 23 11

        // when
        let results: Vec<Option<usize>> = qs
            .iter()
            .map(|q| bin_search(&arr, *q, 0, arr.len() - 1))
            .collect();

        // then
        assert_eq!(
            results,
            [Some(2), Some(0), None, Some(0), None, Some(1), Some(3)]
        )
    }
    #[test]
    fn binary_search_works_with_given_stdin_input_2() {
        // given
        let arr = [1, 2, 3, 4, 5];
        let qs = [1, 2, 3, 4, 5];
        //         5
        // 1 5 8 12 13
        // 5
        // 8 1 23 11

        // when
        let results: Vec<Option<usize>> = qs
            .iter()
            .map(|q| bin_search(&arr, *q, 0, arr.len() - 1))
            .collect();

        // then
        assert_eq!(results, [Some(0), Some(1), Some(2), Some(3), Some(4)])
    }

    #[test]
    fn division() {
        assert_eq!(2 / 3, 0);
        assert_eq!(4 / 3, 1);
        assert_eq!(5 / 3, 1);
    }
}
