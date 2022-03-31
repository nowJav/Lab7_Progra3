import serial
import time
import matplotlib.pyplot as plt

# make sure the 'COM#' is set according the Windows Device Manager
ser = serial.Serial('COM3', 9600, timeout=1)
print('Conectado')
time.sleep(2)

data = []
for i in range(100):
    line = ser.readline()   # read a byte string
    if line:
        s = line.decode()  # convert the byte string to a unicode string
        num = int(s) # convert the unicode string to an int
        print(num)
        data.append(num) # add int to data list
ser.close()

# build the plot
plt.plot(data)
plt.xlabel('Tiempo')
plt.ylabel('Potenciometro Lecturas')
plt.title('Potenciometro Lectruas vs. Tiempo')
plt.show()
