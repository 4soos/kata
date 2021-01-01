def duplicate_encoder(word: str):
    stack = []
    encoder_str = ''
    for i in word:
        if i not in stack:
            encoder_str += '('
            stack.append('i')
        else:
            encoder_str += ')'
            stack.pop('i')
    print(encoder_str)


if __name__ == "__main__":
    test_word = "Success"
    duplicate_encoder(test_word)
