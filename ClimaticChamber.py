#gestione camere

from pymodbus.client.sync import ModbusTcpClient

class Chamber:
    def __init__(self,address):

        self.address = address
        client = ModbusTcpClient
        pass

    def readtemp(self):

        msg = ''

        #msg = self.chamber.read_float(0, 3, 2)
        print(msg)
        return msg

    def read_set_point(self):

        #msg = self.chamber.read_float(77, 3, 2)
        msg = ''
        print (msg)
        return msg

    def set_temp(self, value):
        try:

            # self.chamber.write_float(504, value, 2)

        except:

            pass
        pass
    pass