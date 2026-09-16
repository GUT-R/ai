from ia import RedeNeural
from pprint import pprint
from time import sleep
from subprocess import call
for _ in range(120*4):
    rede_neural = RedeNeural((3, 5, 2))
    pprint(rede_neural.network)
    sleep(0.3)
    call('clear', shell=True)