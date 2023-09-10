from pymodbus.client import ModbusTcpClient

client = ModbusTcpClient('127.0.0.1')

def mbRead():
    try:
        client.connect()
        result = client.read_coils(1,1)
        print(result.bits[0])
    except Exception :
        print('something unknown happened')
    finally:
        client.close()
        print('connection closed')
