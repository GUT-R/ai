from random import randint

# R' = R × p + 255 × (1 - p)
# G' = G × p + 255 × (1 - p)
# B' = B × p + 255 × (1 - p)

p = 0.5
reset = '\033[0m'
type Color = tuple[int, int, int]

def to_pastel(color: Color) -> Color:
    r,g,b = color
    R = int(r * p + 255 * (1 - p))
    G = int(g * p + 255 * (1 - p))
    B = int(b * p + 255 * (1 - p))
    return (R, G, B)

def random_color() -> Color:
    R, G, B = tuple(randint(0, 255) for _ in range(3))
    return R, G, B

def random_pastel() -> Color:
    return to_pastel(random_color())

def rgb_ansi(color: Color) -> str:
    r,g,b = color
    return f'\033[38;2;{r};{g};{b}m'

def rgb_text(color: Color, text: str) -> str:
    return rgb_ansi(color) + text + reset

def pastel_ansi(color: Color) -> str:
    return rgb_ansi(to_pastel(color))

def pastel_text(color: Color, text: str) -> str:
    return pastel_ansi(color) + text + reset

def random_pastel_ansi():
    return rgb_ansi(random_pastel())

def random_pastel_text(text: str):
    return rgb_text(random_pastel(), text)