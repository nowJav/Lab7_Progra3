from pyqtgraph.Qt import QtGui, QtCore
import pyqtgraph as pg 
 
from pyfirmata import Arduino, util 
import time 
 
port='COM3' 
board=Arduino(port) 
Led1 = board.digital[10]

it=util.Iterator(board) 
it.start() 
 
app=QtGui.QApplication([]) 
win=pg.GraphicsWindow(title='Tiempo Real') 
p=win.addPlot(title='Grafica en tiempo real') 
curva=p.plot(pen='y') 
 
p.setRange(yRange=[0,100]) 
dataX=[] 
dataY=[] 
lastY=0 
 
analog0=board.get_pin('a:1:i') 
 
def Update(): 
    global curva, dataX, dataY, lastY, nuevoDato 

    dato=analog0.read() 
    if dato is not None: 
       nuevoDato=dato*100
       print (nuevoDato) 
       time.sleep(0.01) 
    else: 
        nuevoDato=0 

    dataX.append (nuevoDato) 
    dataY.append (lastY) 
    lastY+=1 

    if len(dataX)>200: 
        dataX=dataX[:-1] 
        dataY=dataY[:-1] 

        if nuevoDato > 50:
            while True:
                Led1.write(1)
                time.sleep(.5)
                Led1.write(0)
                time.sleep(.5)
        else:
            Led1.write(0)

    curva.setData(dataY, dataX) 
    QtGui.QApplication.processEvents() 


try: 
    while True: Update() 

except KeyboardInterrupt: 
    pg. QtGui. Application.exec() 
    board.exit()