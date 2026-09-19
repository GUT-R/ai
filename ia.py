from typing import Callable, Any, Optional
from random import randint, choice
from string import ascii_lowercase, digits
import uuid

red   = '\033[31m'
green = '\033[32m'
reset = '\033[0m'
ASCII = ascii_lowercase + digits

type NeuronCallback = Callable[['Neuronio'], Any]

def peso_aleatorio():
    return randint(0, 10)

def simple_id():
    return choice(ASCII) + choice(ASCII)

class Neuronio:
    def __init__(self, conexoes: dict[int, Neuronio], callback: Optional[NeuronCallback] = None):
        self.conexoes = conexoes
        self.callback = callback
        self.id = simple_id()
    
    def disparar(self):
        if self.callback:
            self.callback(self)
        for peso, neuronio in self.conexoes.items():
            if peso <= 5:
                neuronio.disparar()

    def __str__(self):
        return self.id

    def __repr__(self):
        return self.id + '(' + ', '.join(map(lambda x: x.id, self.conexoes.values())) + ')'

def colorized_log(color):
    def wrapper(n: Neuronio):
        print(f'{color}[{n.id} DISPARADO]{reset}')
    return wrapper

class RedeNeural:
    def __init__(self, layers: tuple[int], input_callback: Optional[NeuronCallback]=None, process_callback: Optional[NeuronCallback]=None, output_callback: Optional[NeuronCallback]=None):
        self.layers = [layer for layer in layers if layer != 0]
        self.network: dict[int, list[Neuronio]] = {}
        self.inpt_callback = input_callback
        self.proc_callback = process_callback
        self.otp_callback  = output_callback
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
                    callback=self.proc_callback
                )
                if last:
                    n.conexoes[peso_aleatorio()] = last
                last = n
                output.append(n)
        
        elif i == 0:
            for _ in range(layer):
                output.append(Neuronio(
                    {peso_aleatorio(): neuronio for neuronio in self.random_network(i + 1)},
                    callback=self.inpt_callback
                ))
        else:
            for _ in range(layer):
                output.append(Neuronio(
                    {}, callback=self.otp_callback
                ))
        
        self.network[i] = output
        return output

    def __len__(self):
        return len(self.network)

    def __getitem__(self, key):
        return self.network[key]

        # eu acho que funcionou
