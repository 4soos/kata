mod categorize_new_member;
mod parse_num;
mod reverse_listnode;
mod fib;

use categorize_new_member::open_or_senior;


fn main() {
    let a = vec![(45, 12), (55, 21), (19, -2), (104, 20)];
    open_or_senior(a);
}
