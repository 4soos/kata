use std::convert::TryFrom;
use std::option::Option::Some;

macro_rules! map {
    ($($k: expr => $v: expr), +$(,)?) => {{
        use std::collections::HashMap;
        let mut map = HashMap::new();
        $(map.insert($k, $v);)+
        map
    };};
}


impl Solution {
    pub fn is_number(s: String) -> bool {
        if let Ok(_x) = s.trim().parse::<f64>() { true } else { false }
    }

    pub fn isNumber(s: String) -> bool {
        let mut tf = map!(
            State::Start => map!(
                Input::Sign => State::Sign1,
                Input::Digit => State::D1,
                Input::Dot => State::Dot2,
            ),
            State::Sign1 => map!(
                Input::Digit => State::D1,
                Input::Dot => State::Dot2,
            ),
            State::D1 => map!(
                Input::Exp => State::Exp,
                Input::Dot => State::Dot,
                Input::Digit => State::D1,
            ),
            State::Dot => map!(
                Input::Digit => State::D2,
                Input::Exp => State::Exp
            ),
            State::Dot2 => map!(
                Input::Digit => State::D2,
            ),
            State::D2 => map!(
                Input::Exp => State::Exp,
                Input::Digit => State::D2,
            ),
            State::Exp => map!(
                Input::Sign => State::Sign2,
                Input::Digit => State::D3
            ),
            State::Sign2 => map!(Input::Digit => State::D3),
            State::D3 => map!(Input::Digit => State::D3)
        );
        let mut state = State::Start;
        for c in s.trim().chars() {
            let tf = tf.get(&state).unwrap();
            if let Some(&new) = tf.get(&map_input(c)) {
                state = new;
            } else {
                return false;
            }
        }

        matches!(state, State::D1 | State::Dot | State::D2 | State::D3)
    }
}

#[derive(Eq, PartialEq, Hash, Copy, Clone)]
enum State {
    Start,
    Sign1,
    D1,
    D2,
    Dot,
    Dot2,
    Exp,
    Sign2,
    D3,
}

#[derive(Eq, PartialEq, Hash)]
enum Input {
    Sign,
    Dot,
    Digit,
    Exp,
    Space,
    Other,
}

fn map_input(c: char) -> Input {
    if c.is_ascii_digit() {
        Input::Digit
    } else if c == '.' {
        Input::Dot
    } else if matches!(c, '+'|'-') {
        Input::Sign
    } else if matches!(c, 'e'|'E') {
        Input::Exp
    } else if c == ' ' {
        Input::Space
    } else {
        Input::Other
    }
}