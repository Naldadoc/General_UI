'''
Created on 25 nov 2016

@author: ITANNAL
'''
import pyvisa
import time

class Lambda():
    def __init__(self,addr):
        
        self.rm = pyvisa.ResourceManager()
        self.aliaddr = addr
        self.maxV = int()
        self.maxI = int()
        self.name = str()
        return

    def RMT(self, stat):
        '''
        Define the remote statu of unit:
            0 ---> Local Mode
            1 ---> Remote Mode
            2 ---> Local Lockout Mode (Latched Remote)
        '''
        gpib = self.rm.open_resource(self.aliaddr)
        gpib.query('SYSTEM:SET ' + str(stat))
        gpib.close()
        return

    def SetVolt(self,volts):
        gpib = self.rm.open_resource(self.aliaddr)
        if volts <= self.maxV:
            gpib.query('SOURCE:VOLTAGE ' + str(volts))
            time.sleep(0.5)
            print(gpib.query(':VOLTAGE?'))
            pass
        gpib.close()
        return

    def SetCurrent(self,amps):
        gpib = self.rm.open_resource(self.aliaddr)
        if amps <= self.maxI:
            gpib.write('SOURCE:CURRENT ' + str(amps))
            print(gpib.query(':CURRENT?'))
            pass
        gpib.close()
        return

    def SetOutput(self,stat):
        '''
        Enable/Disenable Output:
            1 ---> Enable
            0 ---> Disenable
        '''
        gpib = self.rm.open_resource(self.aliaddr)
        gpib.write('OUTPUT:STATE '+ str(stat))
        gpib.close()
        return
    pass


class Lambda_80_120(Lambda):
    def __init__(self, addr):
        super().__init__(addr)
        self.maxV = 80
        self.maxI = 120
        self.name = 'Lambda_80_120'
        return
    pass


class HP6032A():

    def __init__(self, addr):
        self.rm = pyvisa.ResourceManager()
        self.gpibaddr = addr
        return

    def SetVoltage(self, volts):
        gpib = self.rm.open_resource(self.gpibaddr)
        gpib.query('VSET' + str(volts))
        gpib.close()
        return

    def SetCurrent(self, amps):
        gpib = self.rm.open_resource(self.gpibaddr)
        gpib.query('ISET' + str(amps))
        gpib.close()
        return

    def ReadSet(self):
        gpib = self.rm.open_resource(self.gpibaddr)
        print("Voltage Set Point: " + gpib.query("VSET?"), "\n" + "Current Set Point: " + gpib.query("ISET?"))
        gpib.close()
        return

    def ReadOut(self):
        gpib = self.rm.open_resource(self.gpibaddr)
        print("Voltage Output: " + gpib.query("VOUT?"), "\n" + "Current Output: " + gpib.query("IOUT?"))
        gpib.close()
        return

    def OutSatus(self):
        return

    pass


class Chroma():
    pass