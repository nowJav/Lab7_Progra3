'''import pyfirmata
import time

board = pyfirmata.Arduino('COM3')
print("Conectado")

it = pyfirmata.util.Iterator(board)
it.start()
'''
'''def _map(x, in_min, in_max, out_min, out_max):
    return int((x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min)
	
# TEST
y = _map(25, 1, 50, 50, 1)
print(y)
'''
