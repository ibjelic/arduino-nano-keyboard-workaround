import serial
import win32com.client as comclt
wsh= comclt.Dispatch("WScript.Shell")
Arduino_Serial = serial.Serial('COM5', 9600)

while 1:
    smrad = (Arduino_Serial.readline()).decode("utf-8")
    #print(smrad)
    if 'A' in smrad: wsh.SendKeys('A')
    elif 'B' in smrad: wsh.SendKeys('B')
    elif 'C' in smrad: wsh.SendKeys('C')
    elif 'D' in smrad: wsh.SendKeys('D')
    elif 'Q' in smrad: wsh.SendKeys('E')
    elif 'F' in smrad: wsh.SendKeys('F')


        
