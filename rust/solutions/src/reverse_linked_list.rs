#[derive(PartialEq, Eq, Clone, Debug)]
pub struct ListNode {
    pub val: i32,
    pub next: Option<Box<ListNode>>
}

impl ListNode {
    #[inline]
    fn new(val: i32) -> Self {
        ListNode {
            next: None,
            val
        }
    }
}

impl Solution {
    pub fn reverse_print(head: Option<Box<ListNode>>>) -> Vec<i32> {
        let mut ans: Vec<i32> = vec![];
        let mut headlist = head;
        while let Some(node) = headlist {
            ans.push(node.val);
            headlist = node.next;
        }
        ans.reverse()
    }
}

