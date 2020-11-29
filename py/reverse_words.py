def reverse_words(text):
  #go for it
    res = ''
    text_slice = text.split(' ')
    count = len(text_slice)
    for (idx,val) in enumerate(text_slice):
        if idx == (count-1):
            res += val[::-1]
        else:
            res += val[::-1]
            res += ' '
    return res