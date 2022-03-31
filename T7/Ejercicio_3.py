import pyfirmata
import time

board = pyfirmata.Arduino('COM3')
it = pyfirmata.util.Iterator(board)
it.start()

analog_input = board.get_pin('a:1:i')
led = board.get_pin('d:10:o')

while True:
    analog_value = analog_input.read()
    if analog_value is not None:
        delay = analog_value + 0.01
        led.write(1)
        time.sleep(delay)
        led.write(0)
        time.sleep(delay)
    else:
        time.sleep(0.1)