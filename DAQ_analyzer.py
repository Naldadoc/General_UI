#Library for Agilent and DAQ
import pyvisa

def get_rm_list():
    rm = pyvisa.ResourceManager()
    rm_list = rm.list_resources()
    instr_list = dict()
    for i in rm_list:
        if 'ASRL3' not in i:
            inst = rm.open_resource(i)
            name = inst.query('*IDN?')
            instr_list[i] = name
            inst.close()
            pass
        pass
    return instr_list

class DAQ:

    def __init__(self, addr):
        self.rm = pyvisa.ResourceManager()
        self.addr = addr
        self.name = ''
        return

    def temp_port_config(self,port,Ttype):
        '''

        :param portl: porta da configurare lista

        '''
        inst = self.rm.open_resource(self.addr)
        inst.close()

        return

    def volt_port_config(self, port,range = 'AUTO'):

        inst = self.rm.open_resource(self.addr)
        inst.close()

        return

    def res_port_config(self,port,range = 'AUTO'):
        inst = self.rm.open_resource(self.addr)
        inst.close()
        return

    def cap_port_config(self, port,range = 'AUTO'):
        inst = self.rm.open_resource(self.addr)
        inst.close()
        return

    def freq_port_config(self, port, range = 'AUTO'):
        inst = self.rm.open_resource(self.addr)
        inst.close()
        return

    def read_meas(self, port):
        inst = self.rm.open_resource(self.addr)
        meas = inst.query()
        inst.close()
        return meas

    def reset(self):
        '''
        Reset the DAQ
        :return:
        '''
        inst = self.rm.open_resource(self.addr)
        inst.write('*RST')
        inst.close()
        return

    def idn(self):
        inst = self.rm.open_resource(self.addr)
        self.name = inst.query('*IDN?')
        inst.close()
        return

    pass


class Daq_6510(DAQ):

    def temp_port_config(self, port, Ttype):
        '''

        :param portl: porta da configurare lista

        '''
        inst = self.rm.open_resource(self.addr)

        inst.write('SENS:FUNC \"TEMP\",(@{port})'.format(port=port))
        inst.write('SENS:TEMP:TRAN TC,(@{port})'.format(port=port))
        inst.write('SENS:TEMP:TC:TYPE {Ttype},(@{port})'.format(Ttype=Ttype, port=port))
        inst.close()

        return

    def volt_port_config(self, port, range='AUTO'):
        inst = self.rm.open_resource(self.addr)
        inst.query(':SENS:FUNC \"VOLT\",(@{port})'.format(port=port))
        inst.query(':SENS:VOLT:RANG:{range}, (@{port})'.format(range=range, port=port))
        inst.close()

        return

    def res_port_config(self, port, range='AUTO'):
        inst = self.rm.open_resource(self.addr)
        inst.write('SENS:FUNC \"RES\",(@{port})'.format(port=port))
        inst.write('SENS:RES:RANG:{range}, (@{port})'.format(range=range, port=port))
        inst.close()
        return

    def cap_port_config(self, port, range='AUTO'):
        inst = self.rm.open_resource(self.addr)
        inst.write('SENS:FUNC \"CAP\",(@{port})'.format(port=port))
        inst.write('SENS:CAP:RANG:{range}, (@{port})'.format(range=range, port=port))
        inst.close()
        return

    def freq_port_config(self, port, range='AUTO'):
        inst = self.rm.open_resource(self.addr)
        inst.write('SENS:FUNC \"FREQ\",(@{port})'.format(port=port))
        inst.write('SENS:FREQ:THR:RANG {range}, (@{port})'.format(range=range, port=port))
        inst.close()
        return

    def read_meas(self, port):
        inst = self.rm.open_resource(self.addr)
        inst.write('ROUT:CLOS (@{port})'.format(port=port))
        meas = inst.query('READ?')
        inst.write('ROUT:OPEN (@{port})'.format(port=port))
        inst.close()
        return meas

    def reset(self):
        '''
        Reset the DAQ
        :return:
        '''
        inst = self.rm.open_resource(self.addr)
        inst.write('*RST')
        inst.close()
        return

    def idn(self):
        inst = self.rm.open_resource(self.addr)
        self.name = inst.query('*IDN?')
        inst.close()
        return
    pass