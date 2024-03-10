from pymodbus.client import ModbusTcpClient

client = ModbusTcpClient('10.10.100.100', 8899)

def mbTCPRead():
    try:
        client.connect()
        result = client.read_holding_registers(0, 5,  slave=1)
        print(result.registers)

    except Exception :
        print('something unknown happened')
    finally:
        client.close()
        print('connection closed')