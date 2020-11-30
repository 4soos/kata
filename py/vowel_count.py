def get_count(input_str):
    num_vowels = 0
    # your code here
    num_vowels += input_str.count('a')
    num_vowels += input_str.count('e')
    num_vowels += input_str.count('i')
    num_vowels += input_str.count('o')
    num_vowels += input_str.count('u')

    return num_vowels
