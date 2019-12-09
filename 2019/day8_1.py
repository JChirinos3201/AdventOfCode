def calc(layers):
    out_img = ['2' for i in range(25*6)]
    for layer in layers:
        for i in range(150):
            if out_img[i] == '2':
                out_img[i] = layer[i]
    return out_img

def go():
    s = open('day8_INPUT.txt').read().strip()
    a = 25 * 6
    layers = [s[i*a:(i+1)*a] for i in range(len(s) // a)]
    img = calc(layers)
    out = 'P3 25 6 255\n'
    for i in range(25*6):
        if img[i] == '0':
            out += '0 0 0\n'
        elif img[i] == '1':
            out += '255 255 255\n'
        else:
            out += '100 100 100\n'
    with open('day8_OUTPUT.ppm', 'w+') as f:
        f.write(out)
