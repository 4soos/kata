impl Solution {
    pub fn fib(n: i32) -> i32 {
        (0..n).fold((0, 1), |mut t, _| (t.1, t.0 + t.1)).0
    }
}