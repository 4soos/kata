# good practice 1
def rgb_good_1(r, g, b):
    round = lambda x: min(255, max(x, 0))
    return ("{:02X}" * 3).format(round(r), round(g), round(b))


# good practice 2
def rgb_good_2(*args):
    return ''.join(map(lambda x: '{:02X}'.format(min(max(0, x), 255)), args))


# not smart
def rgb(r, g, b):
    def convert(color):
        if color <= 0: return '00'
        if color < 16: return '0'+hex(color)[2:]
        if color >= 255: return 'FF'
        else: return hex(color)[2:]
    return str(convert(r) + convert(g) + convert(b)).upper()

def rgb2(*args):
    return ''.join(map(lambda x: f'{:02X}'.format(min(max(0, x), 255)), args));

