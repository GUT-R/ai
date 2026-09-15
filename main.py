from typing import Callable, Any, Optional
red = '\033[31m'
green = '\033[32m'
class Neuronio:
    def __init__(self, conexoes: dict[int, Neuronio], wrapper: Callable[..., Any] | None = None):
        self.conexoes = conexoes
        self.wrapper = wrapper
    def disparar(self):
        if self.wrapper:
            self.wrapper()
        for peso, neuronio in self.conexoes.items():
            if peso >= 5:
                neuronio.disparar()
    

class RedeNeural:
    def __init__(self, layers: tuple[int]):
        self.layers = layers
        self.network: list[Neuronio] = []
    def gen_random_network(self, layer: Optional[int]=None):
        layer = layer or self.layers[0]
        match layer:
            case 0:
                color = green
            case len(self.layers):
                color = red
            case _:
                color = ''

        for i in range(layer):
            if 0 < layer < len(self.layers):
                self.network[]