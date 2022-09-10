def rgb(r, g, b):
    color_list = [r, g, b]
    hex_list = []

    for color in color_list:
        if color > 255:
            color = 255
        if color < 0:
            color = 0
        hex_list.append(f'{(color // 16):X}')
        hex_list.append(f'{int(((color / 16 - (color // 16)) * 16)):X}')

    return "".join(hex_list)


print(rgb(255, 255, 255))