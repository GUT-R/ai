from typing import Callable, Any, Optional, TypeVar
from random import randint, choice
from string import ascii_lowercase, digits

red   = '\033[31m'
green = '\033[32m'
reset = '\033[0m'
ASCII = ascii_lowercase + digits

_T = TypeVar('_T')

type NeuronCallback = Callable[['Neuronio'], Any]

def simple_id():
    return ''.join(choice(ASCII) for _ in range(3))

class RandomInteger:
    def __init__(self):
        self.value = 0
        self.random()
    def __lt__(self, other: int | float):
        return self.value < other
    def __le__(self, other: int | float):
        return self.value <= other
    def __gt__(self, other: int | float):
        return self.value > other
    def __ge__(self, other: int | float):
        return self.value >= other
    def random(self):
        self.value = randint(0, 10)

class Neuronio:
    def __init__(self, conexoes: dict['Neuronio', float | int | RandomInteger], callback: Optional[NeuronCallback] = None):
        self.conexoes = conexoes
        self.callback = callback
        self.carga = 0.0
        self.id = simple_id()
    
    def disparar(self):
        if self.callback:
            self.callback(self)
        for neuronio, peso in self.conexoes.items():
            if self.carga > peso:
                neuronio.carga += self.carga
                yield neuronio
        self.carga = 0.0


    def __str__(self):
        return self.id

    def __repr__(self):
        return self.id + '(' + ', '.join(map(lambda x: x.id, self.conexoes.keys())) + ')'

    def __bool__(self):
        return self.carga > 0

def colorized_log(color: str):
    def wrapper(n: Neuronio):
        print(f'{color}[{n.id} DISPARADO]{reset}')
    return wrapper

class RedeNeural:
    def __init__(self, layers: tuple[int, ...], input_callback: Optional[NeuronCallback]=None, process_callback: Optional[NeuronCallback]=None, output_callback: Optional[NeuronCallback]=None):
        self.layers = [layer for layer in layers if layer != 0]
        self.network: dict[int, list[Neuronio]] = {}
        self.inpt_callback = input_callback
        self.proc_callback = process_callback
        self.otp_callback  = output_callback
        self.teto_territory: list[RandomInteger] = []
        self.random_network()

    def _random_weight(self):
        random_value = RandomInteger()
        self.teto_territory.append(random_value)
        return random_value

    def randomize_all(self):
        tuple(map(lambda x: x.random(), self.teto_territory))

    def random_network(self, i: int=0) -> list[Neuronio]:
        layer = self.layers[i]

        peso_aleatorio = self._random_weight

        if layer == 0:
            raise ValueError('Uma camada não pode conter 0 neurônios')

        if len(self.get(i, [])) == layer:
            return self[i]
        
        output: list[Neuronio] = []

        if 0 < i < len(self.layers) - 1:
            last = None
            for _ in range(layer):
                n = Neuronio(
                    { neuronio: peso_aleatorio() for neuronio in self.random_network(i + 1) },
                    callback=self.proc_callback
                )
                if last:
                    n.conexoes[last] = peso_aleatorio()
                last = n
                output.append(n)
        
        elif i == 0:
            for _ in range(layer):
                output.append(Neuronio(
                    { neuronio: peso_aleatorio() for neuronio in self.random_network(i + 1) },
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

    def __getitem__(self, key: int):
        return self.network[key]

    def get(self, key: int, default: _T=None) -> list[Neuronio] | _T:
        return self.network.get(key, default)


    def efetuar_input(self, input: tuple[bool, ...]):
        neuronios_de_entrada: set[Neuronio] = set()
        for neuronio, deve_ativar in zip(self.network[0], input):
            if deve_ativar:
                neuronio.carga += 1
                neuronios_de_entrada.add(neuronio)
        return self.disparo_em_cadeia(a_partir_de=neuronios_de_entrada)
    
    def disparo_em_cadeia(self, a_partir_de: set[Neuronio]):
        neuronios = a_partir_de
        novos_neuronios: set[Neuronio] = set()
        for neuronio in neuronios:
            novos_neuronios.update(neuronio.disparar())
        if not novos_neuronios:
            return novos_neuronios
        self.disparo_em_cadeia(a_partir_de=novos_neuronios)
        return novos_neuronios

    def obter_saida(self) -> tuple[bool, ...]:
        return tuple(map(bool, self.network[len(self) - 1]))

    def treinar(self, objetivo: tuple[ tuple[tuple[bool, ...], tuple[bool, ...]], ... ]):
        concluido = False
        while not concluido:
            concluido = True
            for input, task in objetivo:
                self.efetuar_input(input)
                if self.obter_saida() != task:
                    self.randomize_all()
                    concluido = False
                    break

    def __str__(self) -> str:
        return '\nAinda não tem exibição, animal.\n'