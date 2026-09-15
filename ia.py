from typing import Callable, Any, Optional
from random import randint
import uuid

red   = '\033[31m'
green = '\033[32m'
reset = '\033[0m'

type NeuronWrapper = Callable[['Neuronio'], Any]

def peso_aleatorio():
    return randint(0, 10)

class Neuronio:
    def __init__(self, conexoes: dict[int, Neuronio], wrapper: Optional[NeuronWrapper] = None):
        self.conexoes = conexoes
        self.wrapper = wrapper
        self.id = str(uuid.uuid4())[:2]
    
    def disparar(self):
        if self.wrapper:
            self.wrapper(self)
        for peso, neuronio in self.conexoes.items():
            if peso <= 5:
                neuronio.disparar()

    def __str__(self):
        return self.id

    def __repr__(self):
        return self.id + '(' + ', '.join(map(lambda x: x.id, self.conexoes.values())) + ')'

def colorized_log(color):
    def callback(n: Neuronio):
        print(f'{color}[{n.id} DISPARADO]{reset}')
    return callback

class RedeNeural:
    def __init__(self, layers: tuple[int], input_wrapper: Call):
        self.layers = [layer for layer in layers if layer != 0]
        self.network: dict[int, list[Neuronio]] = {}
        self.random_network()
            
    def random_network(self, i: Optional[int]=None):
        i = i or 0
        layer = self.layers[i]
        if layer == 0:
            raise ValueError('Uma camada não pode conter 0 neurônios')

        output = []

        if 0 < i < len(self.layers) - 1:
            last = None
            for _ in range(layer):
                n = Neuronio(
                    { peso_aleatorio(): neuronio for neuronio in self.random_network(i + 1) },
                    wrapper=colorized_log(color='')
                )
                if last:
                    n.conexoes[peso_aleatorio()] = last
                    last.conexoes[peso_aleatorio()] = n
                last = n
                output.append(n)
        
        elif i == 0:
            for _ in range(layer):
                output.append(Neuronio(
                    {peso_aleatorio(): neuronio for neuronio in self.random_network(i + 1)},
                    wrapper=colorized_log(color=red)
                ))
        else:
            for _ in range(layer):
                output.append(Neuronio(
                    {}, wrapper=colorized_log(color=green)
                ))
                self.current_node += 1
        
        self.network[i] = output
        return output
