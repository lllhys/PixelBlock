def get_hex_color(red, green, blue, white=0):
    red = int(red)
    green = int(green)
    blue = int(blue)
    white = int(white)
    return (white << 24) | (red << 16) | (green << 8) | blue


def get_RGB_color(hex_color):
    return (hex_color>>16)&0xff,(hex_color>>8)&0xff,hex_color&0xff

