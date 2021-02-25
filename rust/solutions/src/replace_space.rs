impe Solution {
    pub fn replace_space(s: String)-> String {
        s.split(" ").collect::<Vec<&str>>().join("%20")
    }
}

#[cfg(test)]
mod #[test]
fn test_replace_space() {
    assert_eq!(
        replace_space("We are happy."),
        "We%20are%20happy."
    )
}
