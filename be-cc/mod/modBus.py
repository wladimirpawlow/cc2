from pymodbus.client import ModbusTcpClient

client = ModbusTcpClient('127.0.0.1')

def mbRead():
    client.connect()
    result = client.read_coils(1,1)
    print(result.bits[0])
    client.close()