pub fn open_or_senior(data: Vec<(i32, i32)>) -> Vec<String> {
    // code here
    let mut ret = Vec::new();
    for item in data {
        // println!("{}",item.0.clone() -item.1.clone());
        match item.0 >= 55 && item.1 > 7 {
            true => { ret.push(String::from("Senior")) }
            false => { ret.push(String::from("Open")) }
        }
    }

    ret
}

#[cfg(test)]
mod tests {
    use super::*;
    #[test]
    fn returns_expected() {
        assert_eq!(open_or_senior(vec![(45, 12), (55,21), (19, -2), (104, 20)]),
                   vec!["Open", "Senior", "Open", "Senior"]);
        assert_eq!(open_or_senior(vec![(3, 12), (55,1), (91, -2), (54, 23)]),
                   vec!["Open", "Open", "Open", "Open"]);
    }
}

