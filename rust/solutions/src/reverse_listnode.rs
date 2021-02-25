// Definition of singly-linked list
#[derive(Eq, PartialEq, Clone, Debug)]
pub struct ListNode {
    pub val: i32,
    pub next: Option<Box<ListNode>>,
}

impl ListNode {
    #[inline]
    fn new(val: i32) -> Self {
        ListNode {
            next: None,
            val,
        }
    }
}


impl Solution {
    // pub fn reverse_list(head: Option<Box<ListNode>>) -> Option<Box<ListNode>> {
    //     if head.is_none() {
    //         return None;
    //     }
    //     let mut prev: Option<Box<ListNode>> = None;
    //     let mut curr: Option<Box<ListNode>> = head;
    //     while curr.is_some() {
    //         let mut node = curr.take().unwrap();
    //         curr = node.next;
    //         node.next = prev;
    //         prev = Some(node);
    //     }
    //     prev
    // }
    pub fn reverse_list(head: Option<Box<ListNode>>) -> Option<Box<ListNode>> {
        let mut prev: Option<Box<ListNode>> = None;
        let mut curr: Option<Box<ListNode>> = head;
        while let Some(mut node) = curr.take() {
            curr = node.next;
            node.next = prev;
            prev = Some(node);
        }
        prev
    }
}


