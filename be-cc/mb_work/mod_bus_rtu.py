from pymodbus.client import ModbusSerialClient
from pymodbus.transaction import ModbusRtuFramer as ModbusFramer

client = ModbusSerialClient(
            # port='COM2', #for windows
            port='/dev/ttyRS485-1', #for wirenboard
            framer=ModbusFramer,
            # framer=framer,
            timeout=100,
            # retries=3,
            # retry_on_empty=False,
            # strict=True,
            method='rtu',
            baudrate=9600,
            bytesize=8,
            parity="N",
            stopbits=1,
            # handle_local_echo=False,
        )

def mbRTURead():
    print('something 25')
    client.connect()
    print('something 35')
    client.close()
    try:
        print('something 1')
        client.connect()
        print('something 2')
        while 1:
            result = client.read_holding_registers(0, 5, slave=1)
            print('something 3')
            print(result.registers)

    except Exception:
        print('something unknown happened')
    finally:
        client.close()
        print('connection closed')